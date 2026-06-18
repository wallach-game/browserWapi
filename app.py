import json
import os

from fastapi import FastAPI, HTTPException
from playwright.async_api import async_playwright

os.environ["DISPLAY"] = ":0"

app = FastAPI()
browser = None
playwright = None

DEFAULT_ROUTES = [
    {"path": "/open", "url": "https://example.com", "extract": "title"}
]


def load_scrape_routes():
    """Read route definitions from SCRAPE_ROUTES, falling back to the demo route."""
    raw = os.environ.get("SCRAPE_ROUTES")
    if not raw:
        return DEFAULT_ROUTES

    try:
        routes = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"SCRAPE_ROUTES is not valid JSON: {exc}") from exc

    if not isinstance(routes, list):
        raise ValueError("SCRAPE_ROUTES must be a JSON array of route configs")

    for route in routes:
        if "path" not in route or "url" not in route:
            raise ValueError(f"Route config missing 'path' or 'url': {route}")

    return routes


async def extract(page, config):
    extract_type = config.get("extract", "title")
    selector = config.get("selector")

    if extract_type == "title":
        return await page.title()
    if extract_type == "text":
        locator = page.locator(selector) if selector else page.locator("body")
        return await locator.inner_text()
    if extract_type == "html":
        locator = page.locator(selector) if selector else page.locator("html")
        return await locator.inner_html()
    if extract_type == "attribute":
        attribute = config.get("attribute")
        if not selector or not attribute:
            raise ValueError("'attribute' extraction requires 'selector' and 'attribute'")
        return await page.locator(selector).get_attribute(attribute)

    raise ValueError(f"Unknown extract type: {extract_type}")


def make_handler(config):
    async def handler():
        page = await browser.new_page()
        try:
            await page.goto(config["url"])
            result = await extract(page, config)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc
        # DO NOT close the page: it stays open so you can watch it over noVNC
        return {"result": result}

    return handler


@app.on_event("startup")
async def startup_event():
    global browser, playwright
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False, args=["--no-sandbox"])

    for config in load_scrape_routes():
        app.add_api_route(config["path"], make_handler(config), methods=["GET"])

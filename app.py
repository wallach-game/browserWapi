from fastapi import FastAPI
from playwright.async_api import async_playwright
import asyncio
import os

os.environ["DISPLAY"] = ":0"

app = FastAPI()
browser = None
playwright = None

@app.on_event("startup")
async def startup_event():
    global browser, playwright
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False, args=["--no-sandbox"])

@app.get("/open")
async def open_page():
    page = await browser.new_page()
    await page.goto("https://example.com")
    title = await page.title()
    # DO NOT close browser
    return {"title": title}

from fastapi import FastAPI
from playwright.async_api import async_playwright
import os

os.environ["DISPLAY"] = ":0"

app = FastAPI()
browser = None

@app.on_event("startup")
async def startup_event():
    global browser
    pw = await async_playwright().start()
    browser = await pw.chromium.launch(headless=False, args=["--no-sandbox"])
    try:
        from routes import router
        app.include_router(router)
    except ImportError:
        pass

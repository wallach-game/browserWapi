from fastapi import APIRouter
import app as core

router = APIRouter()


@router.get("/open")
async def open_page():
    page = await core.browser.new_page()
    await page.goto("https://example.com")
    title = await page.title()
    return {"title": title}

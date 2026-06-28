# Browser with api access

*how to use this tool:*

## Get the code

```bash
git clone https://github.com/wallach-game/browserWapi.git
```

## Set up your routes

Edit **`routes.py`** — no rebuild needed, just restart uvicorn inside the container (or `docker compose restart`).

```python
# routes.py
from fastapi import APIRouter
import app as core

router = APIRouter()

@router.get("/open")
async def open_page():
    page = await core.browser.new_page()
    # open any webpage
    await page.goto("https://example.com")
    # use any Playwright command
    title = await page.title()
    # return the data you want
    return {"title": title}
```

`core.browser` is the shared Playwright browser instance.

## Run the browser api

```bash
docker compose up -d
```

- API: [http://localhost:8000/open](http://localhost:8000/open)
- VNC (visual): [http://localhost:6080/vnc.html](http://localhost:6080/vnc.html)

enjoy this.

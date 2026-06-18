# Browser with api access

*how to use this tool:*

## Get the code


```bash
#clone this repo 
git clone https://github.com/wallach-game/browserWapi.git
```
## Set up your routes

Routes, target URLs and extraction logic are configured through the
`SCRAPE_ROUTES` environment variable (see `docker-compose.yaml`). It's a
JSON array, one object per route:

```json
[
  {"path": "/open", "url": "https://example.com", "extract": "title"},
  {"path": "/headline", "url": "https://news.example.com", "extract": "text", "selector": "h1"},
  {"path": "/link", "url": "https://example.com", "extract": "attribute", "selector": "a", "attribute": "href"}
]
```

Supported `extract` types:
- `title` - page title
- `text` - inner text of `selector` (or `body` if omitted)
- `html` - inner HTML of `selector` (or `html` if omitted)
- `attribute` - value of `attribute` on `selector` (both required)

If `SCRAPE_ROUTES` is not set, the demo `/open` route above is used.

## Run the browser api
```bash
docker compose up -d
```
you can now open [localhost:3000/open](localhost:3000/open) where is youer new api hosted

and also [http://localhost:6080/vnc.html](http://localhost:6080/vnc.html) where you can manualy click and do stuff 

enjoy this. 


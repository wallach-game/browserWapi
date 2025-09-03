# Browser with api access

*how to use this tool:*

## Get the code


```bash
#clone this repo 
git clone https://github.com/wallach-game/browserWapi.git
```
## Set up your routes

```python
# open file app.py
@app.get("/open")
async def open_page():
    page = await browser.new_page()
    #open any webpage
    await page.goto("https://example.com")
    #use any playwrithe cmd to do what ever you want
    title = await page.title()
    #return the data you want
    return {"title": title}
```

## Run the browser api
```bash
docker compose up -d
```
you can now open [localhost:3000/open](localhost:3000/open) where is youer new api hosted

and also [http://localhost:6080/vnc.html](http://localhost:6080/vnc.html) where you can manualy click and do stuff 

enjoy this. 


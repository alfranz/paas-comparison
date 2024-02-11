from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")
templates = Jinja2Templates(directory="assets")


@app.get("/")
async def service_index(request: Request):
    paas_urls = {
        "render": ("Render", "https://render.com"),
        "do": ("Digital Ocean", "https://heroku.com"),
        "local": ("Local", "#"),
    }

    current_env = os.getenv("PAAS", "local")
    paas_name, paas_url = paas_urls[current_env]

    return templates.TemplateResponse(
        "index.jinja",
        {
            "request": request,
            "variable": 10,
            "paas_name": paas_name,
            "paas_url": paas_url,
        },
    )

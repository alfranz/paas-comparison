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
        "RENDER": ("Render", "https://render.com"),
        "DO": ("Digital Ocean", "https://cloud.digitalocean.com/"),
        "FLY": ("FLY.IO", "https://fly.io"),
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

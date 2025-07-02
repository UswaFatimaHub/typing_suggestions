from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from fastapi.staticfiles import StaticFiles
import os

from fastapi.responses import HTMLResponse




app = FastAPI()

current_dir = os.path.dirname(__file__)
static_path = os.path.join(current_dir, "static")

# app.mount("/", StaticFiles(directory=static_path, html=True), name="st
# atic")
# app.mount("/static", StaticFiles(directory=static_path), name="static")
app.include_router(router)
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def serve_homepage():
    with open(os.path.join(static_path, "index.html")) as f:
        return f.read()
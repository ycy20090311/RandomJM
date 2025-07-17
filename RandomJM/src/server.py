from jm_api import call
from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="RandomJM", docs_url=None, redoc_url=None)

@app.get("/api")
def api():
    return call()

app.mount("/", StaticFiles(directory="dist", html=True), name="static")

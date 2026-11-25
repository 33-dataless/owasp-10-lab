from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).parent

templates = Jinja2Templates(directory=BASE_DIR / "templates")

class App:
    def __init__(self, *handlers):
        self.handlers = handlers

    def create(self) -> FastAPI:
        app = FastAPI()
        app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
        app.mount("/js", StaticFiles(directory=BASE_DIR / "js"), name="js")

        for handler in self.handlers:
            app.include_router(handler.router)

        return app

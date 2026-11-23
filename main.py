import uvicorn

from web.app import App, templates
from web.api.api import HelloApi
from web.src.handlers import PageHandler

app = App(PageHandler(templates), HelloApi()).create()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

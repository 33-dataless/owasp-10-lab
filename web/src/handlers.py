from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse


class PageHandler:
    def __init__(self, templates):
        self.templates = templates
        self.router = APIRouter()

        self.router.add_api_route("/", self.home, methods=["GET"], response_class=HTMLResponse)
        self.router.add_api_route("/send", self.send, methods=["POST"])

    async def home(self, request: Request):
        return self.templates.TemplateResponse(
            request, "index.html", {"title": "Home"}
        )

    async def send(self, name: str = Form(...)):
        return {"message": f"Hello, {name}!"}

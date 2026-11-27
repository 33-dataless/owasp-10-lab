from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse


class PageHandler:
    def __init__(self, templates):
        self.templates = templates
        self.router = APIRouter()

        self.router.add_api_route("/", self.home, methods=["GET"], response_class=HTMLResponse)
        self.router.add_api_route("/send", self.send, methods=["POST"])
        self.router.add_api_route("/login", self.login, methods=["POST"])
        self.router.add_api_route("/register", self.register, methods=["POST"])
        self.router.add_api_route("/logout", self.logout, methods=["POST"])

    async def home(self, request: Request):
        return self.templates.TemplateResponse(
            request, "index.html", {"title": "Home"}
        )

    async def send(self, name: str = Form(...)):
        return {"message": f"Hello, {name}!"}

    async def login(self, username: str = Form(...), password: str = Form(...)):
        # TODO: проверка через AuthService + установка сессионной cookie
        return {"message": f"Login attempt for {username}"}

    async def register(
        self,
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        password2: str = Form(...),
    ):
        if password != password2:
            return {"error": "Passwords do not match"}
        # TODO: создание пользователя через UserService
        return {"message": f"Registered {username} ({email})"}

    async def logout(self):
        # TODO: удаление сессии + очистка cookie
        return RedirectResponse(url="/", status_code=303)

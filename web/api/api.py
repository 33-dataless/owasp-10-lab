from fastapi import APIRouter


class HelloApi:
    def __init__(self):
        self.router = APIRouter(prefix="/api")

        self.router.add_api_route("/hello", self.hello, methods=["GET"])

    async def hello(self):
        return {"message": "Hello World!"}

from main import app
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "Главная"}
    )

@app.post("/send")
async def send(name: str = Form(...)):
    return {"message": f"Привет, {name}!"}

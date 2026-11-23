from web.app import app

@app.get("/api/hello")
async def hello():
    return {"message": "Hello World!"}
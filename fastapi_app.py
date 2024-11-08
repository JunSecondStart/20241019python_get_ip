from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/ip")
async def get_ip(request: Request):
    client_ip = request.client.host
    return {"client_ip": client_ip}


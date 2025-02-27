import logfire
from fastapi import FastAPI
from logfire import instrument_fastapi

from app.conf.config import settings

logfire.configure(
    token=settings.common.logfire_token,
    environment=settings.ENV,
)
app = FastAPI()
instrument_fastapi(app, capture_headers=True, record_send_receive=True)


@app.get("/ping")
async def ping():
    return {"message": "pong"}

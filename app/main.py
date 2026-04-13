from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
import os

from app.database import database, metadata, engine
from app.controllers.cashback import router as cashback_router

STATIC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")


@asynccontextmanager
async def lifespan(app: FastAPI):
    metadata.create_all(engine)
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(title="Cashback API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cashback_router)

# Serve arquivos estáticos (CSS, JS)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# Serve o index.html na raiz
@app.get("/")
async def serve_frontend():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

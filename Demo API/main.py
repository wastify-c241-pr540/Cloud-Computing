from fastapi import FastAPI
from app.api.v1.endpoints import users, garbage_stats, garbages_info, porters, predict

app = FastAPI()

app.include_router(users.router, prefix="/api/v1")
app.include_router(garbage_stats.router, prefix="/api/v1")
app.include_router(garbages_info.router, prefix="/api/v1")
app.include_router(porters.router, prefix="/api/v1")
app.include_router(predict.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Wastify REST-SERVER"}

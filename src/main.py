import uvicorn
from fastapi import FastAPI

from core.routes import router
from core.settings import DEBUG


def get_application() -> FastAPI:
    app = FastAPI(debug=DEBUG)

    app.include_router(router)
    return app


app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

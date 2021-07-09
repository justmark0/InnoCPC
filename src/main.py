import uvicorn
from fastapi import FastAPI

from core.routes import router
from core.settings import DB_SETTINGS, DEBUG
from models import db


def get_application() -> FastAPI:
    application = FastAPI(debug=DEBUG)

    db.bind(**DB_SETTINGS)
    db.generate_mapping(create_tables=True)

    application.include_router(router)
    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

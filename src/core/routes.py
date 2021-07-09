from fastapi import APIRouter

import views.login

router = APIRouter()
router.include_router(views.login.router)

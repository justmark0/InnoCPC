from fastapi import APIRouter

router = APIRouter()


@router.get("/login")
def root():
    return {"hello world": "hello"}

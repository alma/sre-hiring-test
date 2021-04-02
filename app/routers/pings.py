from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def ping():
    """Simple ping functionality: when given a ping, respond with a pong."""
    return {"ping": "pong"}

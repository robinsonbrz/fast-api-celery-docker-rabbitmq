from fastapi import APIRouter

from .root_router import router as main_router

router = APIRouter(prefix="/v1")
router.include_router(main_router)
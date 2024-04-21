""" Aggregates all API routers and starts the API.
"""

import os
from typing import Final

import uvicorn
from fastapi import APIRouter, FastAPI

# Allow versioning of the API via the URI path
BASE_PATH: Final[str] = '/v1'
app = FastAPI()
router = APIRouter()
router.prefix = BASE_PATH

# Add endpoints connected to other routers to this router.
app.include_router(router)

# Run the API
if __name__ == '__main__':
    port = int(os.getenv('PORT', '8080'))
    uvicorn.run(app=app, port=port)
import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Final

import pandas as pd
from fastapi import APIRouter, Depends, FastAPI
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader

from src.api.errors.errors import UnauthorizedError
from src.api.errors.error_response import new_error_response
from src.api.resources.satellite import Satellite
from src.api.resources.post_satellite_purpose_response import PostSatellitePurposeResponse
from src.model.model import Model
from src.utils.logging import setup_logger

MODEL_PATH: Final[str] = './model/ss-001.pkl'

_logger = setup_logger()
rf_model = None  # type: ignore
prediction_router = APIRouter(prefix='/satellite-purpose')


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:  # pylint: disable=unused-argument
    global rf_model
    rf_model = Model.load_trained_model(MODEL_PATH)
    yield


@prediction_router.post('', response_model=PostSatellitePurposeResponse, status_code=201)
async def predict_satellite_purpose(satellite: Satellite, api_key: str = Depends(APIKeyHeader(name='X-API-key'))) -> PostSatellitePurposeResponse | JSONResponse:  # pylint: disable=line-too-long
    if api_key != os.getenv('API_KEY'):
        return JSONResponse(
            content=new_error_response([UnauthorizedError()], status=UnauthorizedError.status_code),
            status_code=UnauthorizedError.status_code
        )
    return PostSatellitePurposeResponse(satellite_purpose=_get_satellite_purpose_prediction(satellite))


def _get_satellite_purpose_prediction(satellite: Satellite) -> float:
    return 6
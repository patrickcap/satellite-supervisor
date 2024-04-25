import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Final

import pandas as pd
import pickle

from fastapi import APIRouter, Depends, FastAPI
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader

from src.api.errors.errors import UnauthorizedError
from src.api.errors.error_response import new_error_response
from src.api.resources.satellite import Satellite
from src.api.resources.post_satellite_purpose_response import PostSatellitePurposeResponse
from src.model.model import Model
from src.utils.logging import setup_logger

MODEL_PATH: Final[str] = './models/ss_model_001.pkl'

_logger = setup_logger()
ss_model_001 = None  # type: ignore
prediction_router = APIRouter(prefix='/satellite-purpose')

with open(MODEL_PATH, 'rb') as f:
    ss_model_001 = pickle.load(f)


@prediction_router.post('', response_model=PostSatellitePurposeResponse, status_code=201)
async def predict_satellite_purpose(satellite: Satellite, api_key: str = Depends(APIKeyHeader(name='X-API-key'))) -> PostSatellitePurposeResponse | JSONResponse:  # pylint: disable=line-too-long
    if api_key != os.getenv('API_KEY'):
        return JSONResponse(
            content=new_error_response([UnauthorizedError()], status=UnauthorizedError.status_code),
            status_code=UnauthorizedError.status_code
        )
    return PostSatellitePurposeResponse(satellite_purpose=_get_satellite_purpose_prediction(satellite))


def _get_satellite_purpose_prediction(satellite: Satellite) -> float:

    input_df = pd.DataFrame({
        'Country of Operator/Owner': [0],
        'Operator/Owner': [0],
        'Users': [0],
        'Type of Orbit': [0],
        'Contractor': [0],
        'Class of Orbit': [0]
    })
    satellite_purpose = ss_model_001.predict(input_df)

    return satellite_purpose
from pydantic import BaseModel


class PostSatellitePurposeResponse(BaseModel):
    satellite_purpose: int
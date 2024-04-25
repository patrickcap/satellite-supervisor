from pydantic import BaseModel


class Satellite(BaseModel):
    country_operator_owner: int
    operator_owner: int
    users: int
    orbit_type: int
    contractor: int
    orbit_class: int
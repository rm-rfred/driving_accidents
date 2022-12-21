from pydantic import BaseModel


class Accident(BaseModel):
    id_accident: int
    vehicule_letter: str
    year: int
    place: str
    accident_type: str
    cnit: str
    vehicule_category: str
    vehicule_age: int

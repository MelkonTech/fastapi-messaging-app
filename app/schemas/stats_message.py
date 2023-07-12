from pydantic import BaseModel
from typing import List
from datetime import date


class StatsMessageBaseSchema(BaseModel):
    uuid: str
    customerId: int
    message_type: str
    amount: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class StatisticsEntry(BaseModel):
    message_type: str
    total_count: int
    date: date


class StatisticsResponse(BaseModel):
    status: str
    results: int
    data: List[StatisticsEntry]

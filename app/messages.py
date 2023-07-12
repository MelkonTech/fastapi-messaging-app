from fastapi import Depends, status, APIRouter, Query
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.schemas.stats_message import (
    StatsMessageBaseSchema,
    StatisticsEntry,
    StatisticsResponse,
)
from app.models.stats_message import StatsMessage
from app.configs.database import get_db

router = APIRouter()


@router.post("/message", status_code=status.HTTP_201_CREATED)
async def process_message(
    message: StatsMessageBaseSchema, db: Session = Depends(get_db)
) -> dict:  # Must be added response type.
    """
    Process a new message and store it in the database.
    """
    new_message = db.merge(StatsMessage(**message.dict()))
    db.commit()
    db.refresh(new_message)
    return {"status": "success", "message": new_message}


@router.get("/statistics", response_model=StatisticsResponse)
async def get_statistics(
    start_date: str = Query(
        ..., description="Start date in the format YYYY-MM-DD", example="2023-07-01"
    ),
    end_date: str = Query(
        ..., description="End date in the format YYYY-MM-DD", example="2023-07-10"
    ),
    message_type: str = Query(..., description="Type of the message", example="A"),
    db: Session = Depends(get_db),
    limit: int = 10,
    page: int = 1,
):
    """
    Retrieve statistics messages from the database.
    """
    skip = (page - 1) * limit

    query = db.query(
        StatsMessage.message_type,
        func.count().label("total_count"),
        func.date(StatsMessage.createdAt).label("date"),
    )

    if start_date:
        query = query.filter(func.date(StatsMessage.createdAt) >= start_date)
    if end_date:
        query = query.filter(func.date(StatsMessage.createdAt) <= end_date)
    if message_type:
        query = query.filter(StatsMessage.message_type == message_type)

    query = query.group_by(StatsMessage.message_type, func.date(StatsMessage.createdAt))
    query = query.limit(limit).offset(skip)

    result = query.all()
    data = [
        StatisticsEntry(
            message_type=row[0],
            total_count=row[1],
            date=row[2],
        )
        for row in result
    ]

    return {
        "status": "success",
        "results": len(result),
        "data": data,
    }

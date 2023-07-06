"""/getForecast API endpoint"""
from fastapi import APIRouter, HTTPException
from starlette import status

from app.service.get_data import get_data
from app.schemas import ForecastRequest, Geo

api_router = APIRouter(tags=["Forecast"])


@api_router.get("/getForecast",
                status_code=status.HTTP_200_OK)
async def get_forecast(from_ts, to_ts, lat, lon):
    r = ForecastRequest(from_ts=from_ts, to_ts=to_ts, g=Geo(lat=lat, lon=lon))
    data = await get_data(r.from_ts, r.to_ts, r.g)
    if data:
        return data
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="temperature data was not found",
    )

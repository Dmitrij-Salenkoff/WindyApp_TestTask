from app.endpoints.get_forecast import api_router as get_forecast
from app.endpoints.health_check import api_router as health_check_router

list_of_routes = [health_check_router, get_forecast]

__all__ = [
    "list_of_routes",
]

from django.urls import path
from . import views


urlpatterns = [
    path(r'<str:fro>-<str:dst>-<int:route_id>&date=<int:year>-<int:month>-<int:day>', views.show_available_buses),
    path(r'book/<int:id>', views.book)
]

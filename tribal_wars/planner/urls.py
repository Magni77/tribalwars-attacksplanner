from django.urls import path

from tribal_wars.planner.views import PlannerView

app_name = "users"
urlpatterns = [
    path("", view=PlannerView.as_view(), name="calculate-attack"),
]

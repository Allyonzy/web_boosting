from django.urls import path, re_path
from data_visualization import views as dv_views

urlpatterns = [
    path("", dv_views.home, name="home"),
    re_path(r"^eda", dv_views.eda, name="eda"),
    re_path(r"^test", dv_views.test, name="test"),
    path("result", dv_views.result, name="result"),
    re_path(r"^csv-upload", dv_views.csv_upload, name="csv_upload"),
]

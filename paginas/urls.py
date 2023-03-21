from django.urls import path
from .views import IndexView

urlpatterns = [

    path("pagina-inicial", IndexView.as_view(), name="pagina-inicial"),

]

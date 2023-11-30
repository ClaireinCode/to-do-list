from django.urls import path
from .views import All_Lists, A_List

urlpatterns = [
    path("", All_Lists.as_view(), name='all_lists'),
    path("<int:id>/", A_List.as_view(), name="a_list"),
]

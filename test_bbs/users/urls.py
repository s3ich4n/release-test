from django.urls import path

from test_bbs.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    hello,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("hello", hello),
    path("hello2", hello2),
]

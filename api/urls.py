from os import name
from django.urls import path, include

urlpatterns = [
    path("user/", include(("api.user.urls", "user"), namespace="user")),
    path("mission/", include(("api.mission.urls", "mission"), namespace="mission")),
    path("post/", include(("api.post.urls", "post"), namespace="post")),
    path("activitylog/", include(("api.activity_log.urls", "activity_log"), namespace="activity_log")),
]

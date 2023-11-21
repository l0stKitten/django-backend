from django.urls import path, include, re_path
from rest_framework import routers
from .views.User_view import UserView
from .views.UserPreference_view import UserPreferenceView
from .views.Preference_view import PreferenceView
from .views.Followers_view import FollowersView
from .views import login_view

router = routers.DefaultRouter()
router.register(r'users', UserView)

router1 = routers.DefaultRouter()
router1.register(r'userprefs', UserPreferenceView)

router2 = routers.DefaultRouter()
router2.register(r'preferences', PreferenceView)

router3 = routers.DefaultRouter()
router3.register(r'followers', FollowersView)

urlpatterns = [
    ## Usuarios ----------------------------------------------------
    re_path('signup', login_view.signup),
    re_path('login', login_view.login),
    re_path('test_token', login_view.test_token),
    path(include(router.urls)),
    path(include(router1.urls)),
    path(include(router2.urls)),
    path(include(router3.urls)),
]

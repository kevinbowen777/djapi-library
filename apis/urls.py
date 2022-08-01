from rest_framework.routers import SimpleRouter

from .views import BookViewSet, UserViewSet


router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", BookViewSet, basename="books")


urlpatterns = router.urls

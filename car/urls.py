from django.urls import path
from rest_framework.routers import SimpleRouter
from car.views import CarView

router = SimpleRouter()
router.register('list', CarView)

urlpatterns = [
]

urlpatterns += router.urls

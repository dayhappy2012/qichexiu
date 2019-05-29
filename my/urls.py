

from rest_framework.routers import SimpleRouter


from my.views import *

router = SimpleRouter()
router.register('user', UserView)


urlpatterns = []

urlpatterns += router.urls




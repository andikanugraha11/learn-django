from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api_example',views.Api_exampleViewSet, base_name='example-api')

# for url in router.urls:
#     print(url, '\n')

urlpatterns = [
    path('', include(router.urls))
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from agents.views import *

routers = DefaultRouter()
routers.register('nearest_agents', NewYorkCity, basename='nearest_agents')
routers.register('Boston', Boston, basename='Boston')
routers.register('los_angeles', LosAngeles, basename='los_angeles')
routers.register('chicago', Chicago, basename='chicago')
routers.register('houston', Houston, basename='houston')
routers.register('phoenix', Phoenix, basename='phoenix')
routers.register('san_diego', SanDiego, basename='san_diego')
routers.register('dallas', Dallas, basename='dallas')
routers.register('san_jose', SanJose, basename='san_jose')
routers.register('austin', Austin, basename='austin')
routers.register('columbus', Columbus, basename='columbus')
# routers.register('agents', Agents, basename='agents')
# routers.register('push_data', PushData, basename='push_data')


urlpatterns = [
    path('', include(routers.urls)),
]

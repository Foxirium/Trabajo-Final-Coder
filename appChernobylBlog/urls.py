
from django.urls import path, include
from .views import HomeView, PostCreate, PostDetail
from appChernobyl.views import inicio


urlpatterns = [
    path('appChernobyl/', include('appChernobyl.urls')),
    #url de clases basadas en vistas
    path('', HomeView.as_view(), name="home"),
    #pk (primary key, cada post tiene su id por asi decirlo, asi lo referenciamos en la url)
    path('postdetail/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('postadd/', PostCreate.as_view(), name='post_add'),

]
    
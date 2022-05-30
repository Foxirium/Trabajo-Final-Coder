
from django.urls import path, include
from .views import HomeView, PostCreate, PostDetail, PostUpdate, PostDelete, CategoryView, home 
from appChernobyl.views import inicio


urlpatterns = [
    path('appChernobyl/', include('appChernobyl.urls')),
    #url de clases basadas en vistas
    path('', HomeView.as_view(), name="post_home"),
    #pk (primary key, cada post tiene su id por asi decirlo, asi lo referenciamos en la url)
    path('postdetail/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('postadd/', PostCreate.as_view(), name='post_add'),
    path('postupdate/<int:pk>', PostUpdate.as_view(), name='post_update'),
    path('postdelete/<int:pk>', PostDelete.as_view(), name='post_delete'),
    path('post_category/<str:cats>/', CategoryView, name='post_category'),


    path('home', home, name="home"),

]
    
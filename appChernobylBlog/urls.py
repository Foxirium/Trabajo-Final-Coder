from django.urls import path, include
from .views import AboutMeList, HomeView, PostCreate, PostDetail, PostUpdate, PostDelete, CommentCreate, CategoryView, ProfileCreate, ProfileDetail, ProfileList, ProfileUpdate, ProfileDelete, home
from appChernobyl.views import inicio


urlpatterns = [
    path('appChernobyl/', include('appChernobyl.urls')),
    #url de clases basadas en vistas
    path('', inicio, name = 'inicio'),
    path('post/', HomeView.as_view(), name="post_home"),
    #pk (primary key, cada post tiene su id por asi decirlo, asi lo referenciamos en la url)

    #-----------------------Post Urls--------------------------------------#

    path('postdetail/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('postadd/', PostCreate.as_view(), name='post_add'),
    path('postupdate/<int:pk>', PostUpdate.as_view(), name='post_update'),
    path('postdelete/<int:pk>', PostDelete.as_view(), name='post_delete'),

    #-----------------------Category, Comments Urls--------------------------------------#
    path('post_category/<str:cats>/', CategoryView, name='post_category'),
    path('commentadd/<int:pk>', CommentCreate.as_view(), name='comment_add'),

    #-----------------------Profile Urls--------------------------------------#
    path('profile/list', ProfileList.as_view(), name='profile_list'),
    path('profile/<pk>', ProfileDetail.as_view(), name='profile_detail'),
    path('profile/new/', ProfileCreate.as_view(), name='profile_create'),
    path('profile/edit/<pk>', ProfileUpdate.as_view(), name='profile_update'),
    path('profile/delete/<pk>', ProfileDelete.as_view(), name='profile_delete'),

    #-----------------------About me--------------------------------------#
    path('about/list', AboutMeList.as_view(), name='aboutme_list'),






    path('home', home, name="home"),

]
    
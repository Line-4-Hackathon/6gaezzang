from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('postnew/', views.postnew, name='postnew'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('postshow/<int:post_id>', views.postshow, name='postshow'),
    path('postshow/postedit', views.postedit, name="postedit"),
    path('postshow/postupdate/<int:post_id>', views.postupdate, name='postupdate'),
    path('postshow/postdelete/<int:post_id>', views.postdelete, name='postdelete'),
    path('likes/<int:post_id>', views.likes, name="likes"),
    path('notice1', views.notice1, name='notice1'),
    path('notice2', views.notice2, name='notice2'),
]
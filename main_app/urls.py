from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('items/', views.item_index, name='item-index'),
    path('items/<int:item_id>/', views.item_detail, name='item-detail'),
    path('items/create/', views.ItemCreate.as_view(), name='item-create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='item-update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),
    path('items/<int:item_id>/add-maintaining', views.add_maintaining, name='add-maintaining'),
    path('tags/create/', views.TagCreate.as_view(), name='tag-create'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tag-detail'),
    path('tags/', views.TagList.as_view(), name='tag-index'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag-delete'),
    path('items/<int:item_id>/associate-tag/<int:tag_id>/', views.associate_tag, name='associate-tag'),
    path('items/<int:item_id>/remove-tag/<int:tag_id>/', views.remove_tag, name='remove-tag'),
    path('accounts/signup/', views.signup, name='signup'),
]
from django.urls import path
from blog.views import home, categories, posts, category_detail, post_detail, category_create, category_delete, \
    category_update, post_create, post_update, post_delete

urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories, name='categories'),
    path('posts/', posts, name='posts'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('category/create/', category_create, name='category_create'),
    path('category/update/<int:category_id>/', category_update, name='category_update'),
    path('category/delete/', category_delete, name='category_delete'),
    path('post/create/', post_create, name='post_create'),
    path('post/update/<int:post_id>/', post_update, name='post_update'),
    path('post/delete/', post_delete, name='post_delete'),
]
from django.urls import path
from main.views import home, post_detail, SignupPageView, TitleDescriptionResulsView, account, create_post, post_update, post_delete

urlpatterns = [
    path('', home, name='home'),
    path('posts/search_results', TitleDescriptionResulsView.as_view(), name='search_results'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('posts/<int:pk>/update/', post_update, name='post_update'),
    path('posts/<int:pk>/delete/', post_delete, name='post_delete'),
    path('posts/create-post/', create_post, name='create_post'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('account/<int:pk>/', account, name='account'),
]
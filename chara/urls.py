from django.urls import path
from . import views

app_name = 'chara'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('post/', views.CreateCharaView.as_view(), name='post'),
    path('edit/<int:pk>', views.EditView.as_view(), name='edit'),
    # path('comment/<int:pk>', views.CommentView.as_view(), name='comment'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('charas/<int:category>', views.CategoryView.as_view(), name='charas_cat'),
    path('user-list/<int:user>', views.UserView.as_view(), name='user_list'),
    path('chara-detail/<int:pk>', views.DetailView.as_view(), name='chara_detail'),
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('chara/<int:pk>/delete/', views.CharaDeleteView.as_view(), name='chara_delete'),
    path('chara/<int:pk>/chara_question/', views.CharaQuestionView.as_view(), name='chara_question'),
    path('chara_after/', views.CharaAfterView.as_view(), name='chara_after'),
]
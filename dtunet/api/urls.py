from django.conf.urls import url,include
from . import views
app_name='api'
urlpatterns=[url(r'login/',views.CustomAuthToken().as_view(),name="login_api"),
            url(r'^signup/$',views.SignupAPIView().as_view(),name="signup_api"),
            url(r'^user_list/$',views.UserListAPIView.as_view(),name='user_list_api'),
            url(r'^user_detail/(?P<u_id>\w+)/$',views.UserDetailAPIView.as_view(),name='user_detail_api'),
            ]

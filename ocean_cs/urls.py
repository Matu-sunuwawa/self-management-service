from django.urls import path
from . import views

from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

# from .views import Sample, SampleTwo, SavingaccCreate, SavingDetail

urlpatterns = [
    # path('', views.sample, name='sample'),
    # path('', Sample.as_view(), name='sample'),
    # path('see-form', SampleTwo.as_view(), name='see-form'),
    # path('superhomepage/', SavingaccCreate.as_view(), name='superhomepage'),
    # path('saving-detail', SavingDetail.as_view(), name='saving-detail'),

    # path('admin/', MyAccountManager.as_view(), name='admin'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', views.main, name='main'),
    path('home/', views.home, name='home'), #withdraw nothing do
    path('HomePage/', views.HomePage, name='HomePage'), #deposit
    path('creditdep/', views.creditdep, name='creditdep'), #withdraw nothing do
    path('creditwith/', views.creditwith, name='creditwith'), #deposit
    path('viewsav/', views.viewsav, name='viewsav'),
    path('viewcred/', views.viewcred, name='viewcred'),
    # path('home-page', views.home, name='home-page'),

]


# urlpatterns = [
#     path('', .as_view(), name='oceans')
# ]
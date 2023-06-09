from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),
    path('projects/', views.projects, name="projects"),
    path('faqs/', views.faqs, name="faqs"),
    path('watchus/', views.watchus, name="watchus"),
    path('investor/<str:pk_test>/', views.investor, name="investor"),

    path('make_investment/<str:pk>/', views.makeInvestment, name="make_investment"), 
    path('user_investment/', views.userInvestment, name="user_investment"),
    path('update_investment/<str:pk>/', views.updateInvestment, name="update_investment"),
    path('delete_investment/<str:pk>/', views.deleteInvestment, name="delete_investment"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),

    path('reset_password_sent/',
     auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),

    path('reset_password_complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),
]

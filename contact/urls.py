from django.urls import path
from contact import views

app_name = "contact"

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),

    # CONTACTS
    path("contact/<int:contact_id>/", views.contact, name="contact"),
    path("contact/create/", views.create, name="create"),
    path("contact/update/<int:contact_id>/", views.update, name = "update"),
    path("contact/delete/<int:contact_id>/", views.delete, name="delete"),

    # USERS
    path("user/create/", views.create_user, name="create_user"),
    path('user/login/', views.login_user, name='login_user'),
    path('user/logout/', views.logout_user, name='logout_user'),
]

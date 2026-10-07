from django.urls import path
from . import views

urlpatterns = [
    path("", views.books, name="books"),
    path("<int:book_id>/", views.book_detail, name="book_detail"),
    path("add/", views.add_book, name="add_book"),
    path("form-test/", views.form_test, name="form_test"),
    path("<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("<int:book_id>/delete/", views.delete_book, name="delete_book"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("api/hello/", views.hello_api, name="hello_api"),
    path("api/books/", views.book_api, name="book_api"),
    path("api/books/<int:book_id>/", views.book_detail_api, name="book_detail_api"),
]


# todo_list/todo_app/urls.py
from django.urls import path
from .views import (
    ListListView,
    ItemListView,
    ListCreate,
    ItemCreate,
    ItemUpdate,
    ListDelete,
    ItemDelete,
    TodoListAPIView,
    TodoDetailAPIView,
)

urlpatterns = [
    # Regular views
    path("", ListListView.as_view(), name="index"),
    path("list/<int:list_id>/", ItemListView.as_view(), name="list"),
    path("list/add/", ListCreate.as_view(), name="list-add"),

    # Update the URL pattern for deletion to include the object's primary key
    path("list/<int:pk>/delete/", ListDelete.as_view(), name="list-delete"),

    path("list/<int:list_id>/item/add/", ItemCreate.as_view(), name="item-add"),
    path("list/<int:list_id>/item/<int:pk>/", ItemUpdate.as_view(), name="item-update"),

    # Update the URL pattern for item deletion to include both list_id and pk
    path("list/<int:list_id>/item/<int:pk>/delete/", ItemDelete.as_view(), name="item-delete"),

    # DRF APIs
    path("api/lists/", TodoListAPIView.as_view(), name="api-lists"),
    path("api/items/<int:pk>/", TodoDetailAPIView.as_view(), name="api-items-detail"),
]

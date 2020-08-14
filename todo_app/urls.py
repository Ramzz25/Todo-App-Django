from django.urls import path,include
from todo_app import views

app_name = 'todo_app'

urlpatterns = [
    
    path('register/',views.register,name="register"),
    path('user_login/',views.user_login,name="user_login"),
    path('add_note/',views.add_note,name="add_note"),
    path('view_note/',views.view_note,name="view_note"),
    path('delete_todo/<int:todo_id>/',views.delete_item,name="delete_item"),

]

from dashboard.views import delete_metric, home_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path(
        'delete/<int:pk>/', delete_metric, name='delete_metric'
    ),  # <--- Added route with primary key
]

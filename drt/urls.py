from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
]

# from django.contrib import admin
# from django.urls import path, include
# from app import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('api/stores/', views.StoreList.as_view()),
#     # path('api/tasks/<int:pk>', views.TaskDetailUpdateDelete.as_view())
# ]

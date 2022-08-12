from django.contrib import admin
from django.urls import path

from account.views import Register, Login, MainView

urlpatterns = [
    path('admin/',admin.site.urls),
    path('login/', Login.as_view()),
    # path('logout/', views.logout, name="logout"),
     path('signup/', Register.as_view()),
    path('index/',MainView.as_view())
]
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from mainapp.views import ApplicationView, success_view, main_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ApplicationView.as_view()),
    path('done/', success_view),
    path('main/', main_page_view),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include
from maqola.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("maqola/", include("maqola.urls") )

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# github - kod ombori, ijtimoiy tarmoq | tugadi


# git - versiya boshqaruvi v1, v2, v3, v4, v5


# git bash
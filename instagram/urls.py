from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$' , views.get_image, name ='homepage'),
    url('^user/' , views.userpage , name='username'),
    url('^image/(?P<id>[0-9]+)$' , views.image_details , name ='image'),
    url('^comment' , views.p_detail , name='comment')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

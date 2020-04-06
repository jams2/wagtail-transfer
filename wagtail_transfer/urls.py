from django.conf.urls import url

from .vendor.wagtail_api_v2.router import WagtailAPIRouter

from wagtail_transfer import views
from wagtail_transfer.vendor.wagtail_api_v2.views import ModelsAPIViewSet

chooser_api = WagtailAPIRouter('wagtail_transfer_page_chooser_api')
chooser_api.register_endpoint('pages', views.PageChooserAPIViewSet)
chooser_api.register_endpoint('models', ModelsAPIViewSet)

urlpatterns = [
    url(r'^api/pages/(\d+)/$', views.pages_for_export, name='wagtail_transfer_pages'),
    url(r'^api/objects/$', views.objects_for_export, name='wagtail_transfer_objects'),
    url(r'^api/chooser/', chooser_api.urls),
]

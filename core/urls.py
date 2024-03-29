from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from graphene_file_upload.django import FileUploadGraphQLView

from core.middlewares import TokenValidationMiddleware

from .schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql", TokenValidationMiddleware(FileUploadGraphQLView.as_view(graphiql=True, schema=schema))),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

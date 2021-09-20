from django.urls import path

from columns.api.api_views import CreateKanban

urlpatterns = [
    path('/', CreateKanban.as_view(), name="create_kanban"),
]
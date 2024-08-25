from django.urls import path

from llmstack.sheets.apis import PromptlySheetViewSet

urlpatterns = [
    path("api/sheets", PromptlySheetViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "api/sheets/<str:sheet_uuid>",
        PromptlySheetViewSet.as_view({"get": "list", "patch": "patch", "delete": "delete"}),
    ),
    path(
        "api/sheets/<str:sheet_uuid>/run",
        PromptlySheetViewSet.as_view({"post": "run_async"}),
    ),
]
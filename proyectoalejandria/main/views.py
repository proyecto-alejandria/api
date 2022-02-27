from django.conf import settings

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class BootstrapView(APIView):

    def get(self, request: Request, *args, **kwargs) -> Response:
        return Response({
            'register': settings.REGISTER_ENABLED,
            'public': settings.PUBLIC_SITE,
        })

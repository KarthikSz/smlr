from django.http import JsonResponse
from django.views.generic import View


class IndexView(View):
    """
    Returns the index view response
    """
    def get(self, request):
        return JsonResponse({
            'status_code': 200,
            'message': 'You are not supposed to be here'
        })


class PingView(View):
    """
    Returns the app status
    """

    def get(self, request):
        return JsonResponse({
            'status_code': 200,
            'message': 'Pong'
        })

from django.shortcuts import reverse, redirect
from django.conf import settings
from decouple import config

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        path = request.META.get('PATH_INFO', "")
        query = request.META.get('QUERY_STRING', "")

        # With logged-in user, session will not be cleaned with manage.py clearsessions
        if config('MAINTENANCE_BYPASS_QUERY') in query:
            request.session['bypass_maintenance'] = True

        if not request.session.get('bypass_maintenance', False):
            if settings.MAINTENANCE_MODE and path != reverse('home:maintenance'):
                response = redirect(reverse('home:maintenance'))
                return response

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
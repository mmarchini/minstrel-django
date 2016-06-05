from django.conf import settings


def google_analytics(request):
    # return any necessary values
    return {
        'GOOGLE_ANALYTICS_KEY': getattr(settings, "GOOGLE_ANALYTICS_KEY", None)
    }

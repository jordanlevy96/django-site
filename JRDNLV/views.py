from django.http import HttpResponse

def acme_challenge(request):
    return HttpResponse(settings.ACME_CHALLENGE_CONTENT)
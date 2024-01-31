from django.contrib.sites.models import Site
from django.shortcuts import get_object_or_404


def get_current_site(request):

    current_host = request.get_host()

    current_site = get_object_or_404(Site, domain=current_host)

    return current_site

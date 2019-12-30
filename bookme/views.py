from django.shortcuts import render, HttpResponse
import logging

# Create your views here.
logger = logging.getLogger(__name__)

def my_views(request):
    bad_mojo = True
    if bad_mojo:
        # Log an error messages
        logger.error('Something went Wrong!')

    return HttpResponse("Done with Logging")

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from urllib.parse import urlencode

import json


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect(dashboard)
    else:
        return render(request, 'index.html')


@login_required
def dashboard(request):
    user = request.user
    sf_user = user.social_auth.get(provider='sfc')
    userdata = {
        'user_id': user.id,
        'user_urn': sf_user.uid,
        'org': sf_user.extra_data['organization_id'],
        'sf_user_id': sf_user.extra_data.get('user_id'),
        'email': user.email
    }

    return render(request, 'dashboard.html', {
        'user': user,
        'userdata': json.dumps(userdata, indent=4)
    })

def logout(request):
    log_out(request)
    return HttpResponseRedirect('/')

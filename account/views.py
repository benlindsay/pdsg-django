from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from wsgiref.util import FileWrapper
from django.utils.encoding import smart_str
import mimetypes
import os

from .models import Profile
from .forms import EditProfileForm
from .utils import get_or_create_profile
from penndsg.settings import MEDIA_ROOT


@login_required
def profile_detail_view(request):
    p = get_or_create_profile(request.user)
    context = {'profile': p}
    return render(request, 'profile/detail.html', context)


@login_required
def edit_profile_view(request):
    p = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Changes saved successfully'
            )
            return redirect('account:detail')
        else:
            messages.add_message(
                request, messages.ERROR, 'An error occurred'
            )
            return redirect('account:edit')
    else:
        form = EditProfileForm(instance=p)
    context = {'form': form}
    return render(request, 'profile/edit.html', context)


@login_required
def download_resume(request):
    try:
        file_path = request.user.profile.resume.name
    except:
        raise Http404("No resume found.")
    # https://stackoverflow.com/q/15246661/2680824
    file_name = os.path.basename(file_path)
    file_path = MEDIA_ROOT + '/' + file_path
    file_wrapper = FileWrapper(open(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = (
        'attachment; filename={}'.format(smart_str(file_name))
    )
    return response

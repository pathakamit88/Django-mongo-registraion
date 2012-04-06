from django.template.context import RequestContext
from django.shortcuts import redirect, render_to_response
from django.conf import settings

from forms import RegistrationForm
from auth import User as MongoUser

def save_user_in_mongo(**kwargs):
    new_user = MongoUser.create_user(kwargs['username'], kwargs['password1'], kwargs['email'])
    new_user.first_name = kwargs.get('first_name')
    new_user.last_name = kwargs.get('last_name')
    new_user.save()
    return new_user

def register(request, success_url=None, form_class=None,
             template_name='registration/registration_form.html',
             extra_context=None):

    if form_class is None:
        form_class = RegistrationForm
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            save_user_in_mongo(**form.cleaned_data)
            if success_url is None:
                success_url = settings.LOGIN_URL
            return redirect(success_url)
    else:
        form = form_class()

    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value

    return render_to_response(template_name,
            {'form': form},
        context_instance=context)

import uuid
from django.utils import timezone
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail
from django.conf import settings
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from .forms import SignUpForm, VerificationForm
from .models import Client
from .utils import send_twilio_message, this_send_email


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        request.session['authorizationcode'] = str(uuid.uuid4().get_hex().upper()[0:8])
        request.session['username']= user.username
        newphonenum = user.phone_number
        if len(newphonenum) == 10:
            newphonenum = '+254' + newphonenum[1:10]

        send_twilio_message(newphonenum, request.session['authorizationcode'])
        c = {}
        c.update(csrf(request))
        return render_to_response('verifytoken.html',c)
    else:
        return HttpResponseRedirect('invalid_login.html')


def verify_pass_token(request):
    if request.method == 'GET':
        c = {}
        c.update(csrf(request))
        return render_to_response('verifytoken.html',c)

    else:
        if request.session['authorizationcode'] == request.POST['verification_token']:
                current_user=Client.objects.get(username=request.session['username'])
                if current_user.is_active==True:

                    request.session['user_sysID']=current_user.username
                    return HttpResponseRedirect(reverse('loggedin'))

                else:

                    email_subject = 'Account confirmation'
                    email_body = "Hey %s, thanks for signing up. To activate your account, click this link within 48hours " % (current_user.username)

                    full_email_body= email_body + 'http://127.0.0.1:8000%s' % reverse('confirm_Registration', kwargs={'key': current_user.email_confirm_key })
                    print full_email_body
                    send_mail(email_subject, full_email_body, settings.EMAIL_HOST_USER, [current_user.email, settings.EMAIL_HOST_USER])

                    return HttpResponseRedirect(reverse('signup_success'))

def confirm_Registration(request, key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        request.session['user_sysID']=request.user.username
        HttpResponseRedirect(reverse('loggedin'))


    client_profile = get_object_or_404(Client, email_confirm_key=key)
    request.session['user_sysID'] = client_profile.username

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if client_profile.key_expires < timezone.now():
        return render_to_response('user_profile/confirm_expired.html')

    #if the key hasn't expired save user and set him as active and render some template to confirm activation

    client_profile.is_active = True
    client_profile.save()
    request.session['user_sysID']=client_profile.username
    return HttpResponseRedirect(reverse('loggedin'))


def loggedin(request):
    return render_to_response('loggedin.html', {'full_name': request.session['user_sysID']})


def invalid_login(request):
    return render_to_response('invalid_login.html')


class SignUp(FormView):
    form_class = SignUpForm
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render_to_response(self.template_name, {'form': form}, context_instance=RequestContext(request))

    def form_valid(self, form):
        form.instance.first_name = form.cleaned_data.get('first_name')
        form.instance.last_name = form.cleaned_data.get('last_name')
        form.instance.phone_number = form.cleaned_data.get('phone_number')
        form.instance.username = form.cleaned_data.get('username')
        form.instance.email = form.cleaned_data.get('email')
        form.instance.password1 = form.cleaned_data.get('password1')

        form.save()
        self.request.session['authorizationcode'] = str(uuid.uuid4().get_hex().upper()[0:8])
        self.request.session['username']= form.cleaned_data.get('username')
        newphonenum = form.cleaned_data.get('phone_number')
        if len(newphonenum) == 10:
            newphonenum = '+254' + newphonenum[1:10]

        send_twilio_message(newphonenum, self.request.session['authorizationcode'])


        return render_to_response('verifytoken.html', context_instance=RequestContext(self.request))




def signup_success(request):
    return render_to_response('signup_success.html')

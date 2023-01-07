from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile_Akpugo, Executive_Akpugo, Executive_National, Executive_Okija, Executive_Elele, \
    Profile_National, Profile_Okija, Profile_Elele, CustomUser, Campus
from about.models import About

User = CustomUser


# Create your views here =============================

class LoginView(View):
    def get(self, request):
        context = {}
        return render(request, 'authentication/login.html', context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        context = {}

        context = {'values': request.POST}
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, f'Welcome! {user.first_name} {user.last_name}, You are '
                                              f'now logged in.')
                print(request.POST, request.META['HTTP_REFERER'], '------------------')
                url = str(request.META['HTTP_REFERER'])
                if '/login/?next=' in url:
                    url = url.replace('/accounts/login/?next=', '')
                    print(url, '==============', request.META['HTTP_REFERER'])
                    return HttpResponseRedirect(url)
                else:
                    return redirect('home')

            if len(User.objects.filter(username=username)) == 0:
                context['username_errors'] = True
            else:
                context['username_errors'] = False
            if len(User.objects.filter(password=password)) == 0:
                context['pwd_errors'] = True
            else:
                context['pwd_errors'] = False
            messages.error(request, f'Invalid Credentials, Check Your details..')
            return render(request, 'authentication/login.html', context=context)

        messages.error(request, 'Please fill all fields')
        return render(request, 'authentication/login.html', context)


@login_required
def editprofile(request, username):
    if request.method == 'GET':
        try:
            campuses = Campus.objects.get(campus=request.user.campus)
        except Exception:
            campuses = 'None'
        try:
            profile = Profile_Elele.objects.get(campus=campuses, user=request.user)
            exco = Executive_Elele.objects.all()
            if campuses.campus != 'Elele':
                raise ValueError
        except Exception:
            try:
                profile = Profile_Akpugo.objects.get(campus=campuses, user=request.user)
                exco = Executive_Akpugo.objects.all()
                if campuses.campus != 'Akpugo':
                    raise ValueError
            except Exception:
                try:
                    profile = Profile_Okija.objects.get(campus=campuses, user=request.user)
                    exco = Executive_Okija.objects.all()
                    if campuses.campus != 'Okija':
                        raise ValueError
                except Exception:
                    profile = Profile_National.objects.get(campus=campuses, user=request.user)
                    exco = Executive_National.objects.all()
                    if campuses.campus != 'National':
                        raise ValueError
        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'profile': profile,
                   'exco': exco,
                   'about': about, }
        # print(campuses, profile, '================',profile.campus)
        return render(request, 'authentication/editprofile.html', context)

    elif request.method == 'POST':
        new_username = request.POST['username']
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']
        department = request.POST['department']
        email = request.POST['email']
        part = request.POST['part']
        state_of_origin = request.POST['state']
        phone_num = request.POST['phone_num']
        marital_status = request.POST['marital_status']
        try:
            file = request.FILES['file']
        except Exception:
            pass
        userinstance = User.objects.get(username=username)
        userinstance.username = new_username
        userinstance.email = email
        userinstance.save()
        try:
            instance = Profile_Akpugo.objects.get(user=userinstance)
        except Exception:
            try:
                instance = Profile_Elele.objects.get(user=userinstance)
            except Exception:
                try:
                    instance = Profile_Okija.objects.get(user=userinstance)
                except Exception:
                    instance = Profile_National.objects.get(user=userinstance)

        instance.user = userinstance
        instance.firstname = firstname
        instance.lastname = lastname
        instance.email = email
        instance.department = department
        instance.part = part
        instance.state = state_of_origin
        instance.phone_num = phone_num
        instance.marital_status = marital_status
        try:
            instance.image = file
        except Exception:
            pass
        instance.save()

        messages.success(request, f'You have successfully Updated Your profile')
        return redirect('editprofile', new_username)


@login_required
def profile(request, username):
    user = User.objects.get(username=username)

    try:
        profile = Profile_Akpugo.objects.get(user=user)
        exco = Executive_Akpugo.objects.filter(member=profile)

    except Exception:
        try:
            profile = Profile_Elele.objects.get(user=user)
            exco = Executive_Elele.objects.filter(member=profile)
        except Exception:
            try:
                profile = Profile_Okija.objects.get(user=user)
                exco = Executive_Okija.objects.filter(member=profile)
            except Exception:
                profile = Profile_National.objects.get(user=user)
                exco = Executive_National.objects.filter(member=profile)

    try:
        about = About.objects.get(title='About Madonna Central Choir')
    except Exception:
        about = ''
    context = {'user': user,
               'profile': profile,
               'exco': exco,
               'about': about, }
    return render(request, 'authentication/profile.html', context)

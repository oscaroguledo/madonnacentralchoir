from django.shortcuts import render, redirect
from .models import Gallery, Act_video
from about.models import About
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
import datetime
from django.contrib import messages


# Create your views here.
def activities(request):
    gal = Gallery.objects.filter()
    Act_vid = Act_video.objects.filter()
    try:
        about = About.objects.get(title='About Madonna Central Choir')
    except Exception:
        about = ''

    context = {'gal': gal,
               'gal_count': gal.count,
               'Act_vid_count': Act_vid.count,
               'about': about,
               }
    return render(request, 'activities/activities.html', context)


def gallery(request):
    if 'q' in request.GET:
        q = request.GET['q']
        gal = Gallery.objects.filter(uploaded_at__icontains=q, )

        paginator = Paginator(gal, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        search = 1
        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'gal': gal,
                   'page_obj': page_obj,
                   'search': search,
                   'about': about, }
        return render(request, 'activities/gallery.html', context)
    else:
        gal = Gallery.objects.filter()
        paginator = Paginator(gal, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        search = 0
        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'gal': gal,
                   'page_obj': page_obj,
                   'search': search,
                   'about': about,
                   }
        return render(request, 'activities/gallery.html', context)


def video(request):
    if 'q' in request.GET:
        q = request.GET['q']
        Act_vid = Act_video.objects.filter(uploaded_at__icontains=q, )
        paginator = Paginator(Act_vid, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'Act_vid': Act_vid,
                   'page_obj': page_obj,
                   'about': about, }
        return render(request, 'activities/videos.html', context)
    else:
        Act_vid = Act_video.objects.filter()
        paginator = Paginator(Act_vid, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'Act_vid': Act_vid,
                   'page_obj': page_obj,
                   'about': about, }
    return render(request, 'activities/videos.html', context)

@login_required()
def upload(request, type, media):
    if request.user.is_staff:
        if request.method == 'GET':
            try:
                about = About.objects.get(title='About Madonna Central Choir')
            except Exception:
                about = ''
            context = {'media': media,
                       'about': about, }
            print('-----------------', media)
            return render(request, 'activities/upload.html', context)

        elif request.method == 'POST':
            file = request.FILES['file']
            description = request.POST['description']
            shcount = 1
            title = str(datetime.datetime.now())
            if media == 'Act_Video':
                try:
                    instance = Act_video(title='VID' + title, description=description, uploader=request.user, file=file)
                    instance.save()
                except Exception:
                    pass
            elif media == 'Picture':
                try:
                    instance = Gallery(title='PIC' + title, description=description,
                                       uploader=request.user, file=file)
                    instance.save()
                except Exception:
                    pass
            messages.success(request, f'The {media} has been added successfully')
            return redirect('upload', media)
    else:
        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'media': media,
                   'about': about, }
        messages.error(request, 'Invalid Url')
        next = request.META['HTTP_REFERER']
        return HttpResponseRedirect(next)
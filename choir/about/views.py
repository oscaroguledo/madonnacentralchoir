from django.shortcuts import render
from django.core.paginator import Paginator
from .models import About
from django.contrib.auth.decorators import login_required
from account.models import Profile_Akpugo, Executive_Akpugo, Executive_Elele, Executive_Okija, Executive_National, \
    Campus, Position_Akpugo, Profile_Elele, Profile_Okija, \
    Profile_National
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


# Create your views here.
@login_required
def registers(request):
    global profile, exco
    if 'q' in request.GET:
        q = request.GET['q']
        try:
            campuses = Campus.objects.get(campus=request.user.campus)
        except Exception:
            campuses = 'None'
        try:
            profile = Profile_Elele.objects.filter(campus=campuses, firstname__icontains=q, ) | \
                      Profile_Elele.objects.filter(campus=campuses, lastname__icontains=q, )
            exco = Executive_Elele.objects.all()
            if campuses.campus != 'Elele':
                raise ValueError ## the line is just to trigger an error

        except Exception:
            try:
                profile = Profile_Akpugo.objects.filter(campus=campuses, firstname__icontains=q, ) | \
                          Profile_Akpugo.objects.filter(campus=campuses, lastname__icontains=q, )
                exco = Executive_Akpugo.objects.all()
                if campuses.campus != 'Akpugo':
                    raise ValueError ## the line is just to trigger an error

            except Exception:
                try:
                    profile = Profile_Okija.objects.filter(campus=campuses, firstname__icontains=q, ) | \
                              Profile_Okija.objects.filter(campus=campuses, lastname__icontains=q, )
                    exco = Executive_Okija.objects.all()
                    if campuses.campus != 'Okija':
                        raise ValueError ## the line is just to trigger an error
                except Exception:
                    try:
                        profile = Profile_National.objects.filter(campus=campuses, firstname__icontains=q, ) | \
                                  Profile_National.objects.filter(campus=campuses, lastname__icontains=q, )
                        exco = Executive_National.objects.all()
                        if campuses.campus != 'National':
                            raise ValueError ## the line is just to trigger an error
                    except Exception:
                        profile = ''
                        exco = ''

        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        paginator = Paginator(profile, 20)
        #print(profile, campuses, '======================')
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        context = {'campuses': campuses,
                   'about': about,
                   'exco': exco,
                   'profile': profile,
                   'page_obj': page_obj, }
        return render(request, 'about/register.html', context)
    else:
        try:
            campuses = Campus.objects.get(campus=request.user.campus)
        except Exception:
            campuses ='None'
        try:
            profile = Profile_Elele.objects.filter(campus=campuses)
            exco = Executive_Elele.objects.all()
            if campuses.campus != 'Elele':
                raise ValueError ## the line is just to trigger an error
        except Exception:
            try:
                profile = Profile_Akpugo.objects.filter(campus=campuses)
                exco = Executive_Akpugo.objects.all()
                if campuses.campus != 'Akpugo':
                    raise ValueError  ## the line is just to trigger an error
            except Exception:
                try:
                    profile = Profile_Okija.objects.filter(campus=campuses)
                    exco = Executive_Okija.objects.all()
                    if campuses.campus != 'Okija':
                        raise ValueError  ## the line is just to trigger an error
                except Exception:
                    try:
                        profile = Profile_National.objects.filter(campus=campuses)
                        exco = Executive_National.objects.all()
                        if campuses.campus != 'National':
                            raise ValueError  ## the line is just to trigger an error
                    except Exception:
                        try:
                            profile = Profile_Elele.objects.all() + Profile_Okija.objects.all() + Profile_Akpugo.objects.all() + \
                                      Profile_National.objects.all()

                            exco = Executive_National.objects.all() + Executive_Elele.objects.all() + Executive_Okija.objects.all() + \
                                   Executive_Akpugo.objects.all()
                            if campuses.campus != 'None':
                                raise ValueError  ## the line is just to trigger an error
                        except Exception:
                            profile = ''
                            exco = ''

        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        paginator = Paginator(profile, 20)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        context = {'campuses': campuses,
                   'about': about,
                   'exco': exco,
                   'profile': profile,
                   'page_obj': page_obj, }

        return render(request, 'about/register.html', context)


def history(request):
    about = About.objects.filter()
    paginator = Paginator(about, 1)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {'about': about,
               'page_obj': page_obj, }
    return render(request, 'about/history.html', context)


def about(request):
    context = {}
    try:
        about = About.objects.get(title='About Madonna Central Choir')
    except Exception:
        about = ''
    context['about'] = about
    try:
        about_akpugo = Campus.objects.get(campus='Akpugo')
        context['about_akpugo'] = about_akpugo
    except Exception:
        pass
    try:
        about_elele = Campus.objects.get(campus='Elele')
        context['about_elele'] = about_elele
    except Exception:
        pass
    try:
        about_okija = Campus.objects.get(campus='Okija')
        context['about_okija'] = about_okija
    except Exception:
        pass
    try:
        about_national = Campus.objects.get(campus='National')
        context['about_national'] = about_national
    except Exception:
        pass
    return render(request, 'about/about.html', context)


def campus(request, campus):
    # print(campus, '----------------')
    import datetime
    current_year = datetime.date.today().year
    context = {}

    context['campus'] = campus
    try:
        members = Profile_Akpugo.objects.filter(graduatedate__gte=datetime.date.today())
        excos = Executive_Akpugo.objects.all()
        context['members'] = members
        context['members_count'] = members.count
        context['excos'] = excos
        about = About.objects.filter()
        paginator = Paginator(members, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        context['page_obj'] = page_obj
        context['about'] = about
    except Exception:
        pass
    return render(request, 'about/campus.html', context)


def printexecute(session, campus, select):
    global profile, excos
    doc = SimpleDocTemplate("/tmp/simple_table_grid.pdf", pagesize=letter)
    # container for the 'Flowable' objects
    elements = []
    if campus == 'Elele':
        profile = Profile_Elele.objects.all()
        excos = Executive_Elele.objects.all()
    elif campus == 'Akpugo':
        profile = Profile_Akpugo.objects.all()
        excos = Executive_Akpugo.objects.all()
    elif campus == 'Okija':
        profile = Profile_Okija.objects.all()
        excos = Executive_Okija.objects.all()
    elif campus == 'National':
        profile = Profile_National.objects.all()
        excos = Executive_National.objects.all()

    data = [[select + ':', f'{campus}'.upper() + ' CAMPUS', session],
            ['S/N', 'Name of The Chorister', 'Part', 'Current Position Held', 'Department']]
    count = 0
    session_start = session[0:session.index('/')]
    session_end = session[session.index('/') + 1:]

    for p in profile:
        try:
            p.graduatedate_year = p.graduatedate.year
        except AttributeError:
            p.graduatedate_year = int(session_end)
        # print(p.graduatedate_year, p.joindate.year, session_start, session_end)
        if int(session_start) >= int(p.joindate.year) and int(session_end) <= int(p.graduatedate_year) or int(
                p.graduatedate_year) == 1999:
            if select == 'All':
                count += 1
                e = []
                for ex in excos:
                    if ex.member == p and ex.session == session:
                        e.append(ex)

                try:
                    data.append([count,
                                 p,
                                 p.part,
                                 str([ex.position.pos for ex in e]),
                                 p.department])
                    print(data)
                except Exception:
                    data.append([count, p, p.part, 'None', p.department])
                    print(data)
            else:

                if select == 'Excecutives':
                    e = []
                    for ex in excos:
                        print(ex, '---------------------------------', ex.session, session)
                        if p == ex.member and ex.session == session:
                            count += 1
                            e.append(ex)

                            try:
                                data.append([count,
                                             p,
                                             p.part,
                                             str([ex.position.pos for ex in e]),
                                             p.department])
                            except Exception:
                                data.append([count, p, p.part, 'None', p.department])
                elif select == 'Floor Members':
                    s = []
                    se = []
                    for ex in excos:
                        if ex.member == p and ex.session == session:
                            se.append(ex)
                    if s.count([p, se]) < 1:
                        s.append([p, len(se)])
                    for i in s:
                        if i[1] == 0:

                            count += 1
                            try:
                                d = [count,
                                     i[0],
                                     i[0].part,
                                     str('none'),
                                     i[0].department]
                                data.append(d)

                            except Exception:
                                data.append([count, i[0], i[0].part, 'None', i[0].department])
    t = Table(data)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.darkorchid),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.floralwhite)])
               )
    elements.append(t)
    # write the document to disk
    doc.build(elements)


@login_required
def print_(request, campus_print):
    import datetime
    today = datetime.date.today().year
    firstyear = 1999
    sessions = {}
    while True:
        sessions[f'{firstyear}/' + str(firstyear + 1)] = f'{firstyear}/' + str(firstyear + 1)
        if firstyear == today:
            break
        firstyear += 1
    if request.method == 'GET':
        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'campus': campus_print,
                   'sessions': sessions,
                   'about': about}
        return render(request, 'about/print.html', context)
    elif request.method == 'POST':
        campus_print = request.POST['campus']
        session = request.POST['session']
        Select = request.POST['Select']
        print(session[0:session.index('/')], '===============', session[session.index('/') + 1:], '======', )
        printexecute(session=session, campus=campus_print, select=Select)

        fs = FileSystemStorage("/tmp")
        with fs.open("simple_table_grid.pdf") as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="simple_table_grid.pdf"'
            return response

import json

from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView

USERID_MAP_FOR_DEMO = {
    'subangkar': 'Student',
    'araf': 'Student',
    'samin': 'Student',
    'joseph': 'Teacher',
    'andrew': 'Teacher',
}

SIMUID_MAP_FOR_DEMO = {
    1: 'Collision Lab Phet.html',
    2: 'Projectile Simulation.html',
}


def is_teacher(username):
    username = username.strip().lower()
    return username in USERID_MAP_FOR_DEMO and USERID_MAP_FOR_DEMO[username] == 'Teacher'


class Index(TemplateView):
    """
    Renders Home Page
    """
    template_name = 'coreapp/avilon/student-home.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and is_teacher(request.user.username):
            self.template_name = 'coreapp/avilon/teacher-home.html'
        return super().get(request, args, kwargs)


class Login(TemplateView):
    """
    Renders Home Page
    """

    template_name = 'coreapp/avilon/login.html'

    def get_context_data(self, **kwargs):
        ctx = {'loggedIn': self.request.user.is_authenticated}
        return ctx

    def post(self, request, *args, **kwargs):
        try:
            name = str(request.POST.get('name')).strip().lower()
            if name in USERID_MAP_FOR_DEMO:
                login(request, user=User.objects.get(username=name))
                return redirect('/')
        except:
            pass
        return HttpResponse("Invalid data")


def logout_user(request):
    logout(request)
    return redirect('/')


def lab(request):
    try:
        labname = str(request.GET.get('lab')).lower()
        exp_lists = {
            'physics': [
                ('Projectile',
                 'https://kaiserscience.files.wordpress.com/2015/08/horizontally-launched-projectiles.gif',
                 reverse('coreapp:experiment', kwargs={'id': 2})),
                ('Collision', 'https://xmphysics.files.wordpress.com/2019/03/collisiongraphs-a.gif',
                 reverse('coreapp:experiment', kwargs={'id': 1})),
                ("Series-Parallel Circuit",
                 "http://s4.thingpic.com/images/SC/yUMJVwbNDtnrffhX2HHUVH5e.gif"),
                ("Prism Experiment",
                 "https://media0.giphy.com/media/l0MYKMrQnwNvLjYhW/source.gif"),
                ("Young's Experiment",
                 "https://physicsforus.files.wordpress.com/2011/07/doubleslit_animation.gif"),
                ('Simple Pendulum', 'http://www.acs.psu.edu/drussell/Demos/Pendulum/compare-lengths.gif'),
            ],
            'chemistry': [('NaOH-H2SO4 Titration',
                           'https://www.buffaloschools.org/cms/lib/NY01913551/Centricity/Domain/6557/titration1.gif'),
                          ("Bunsen Burner",
                           "http://classroomclipart.com/images/gallery/Animations/Science/TN_bunsen_burner-4-12_cc.gif"),
                          ("Ion Test",
                           "https://pufflesandhoneyadventures.files.wordpress.com/2017/08/metal-ion-flame-test.gif"),
                          ("Precipitation Test",
                           "https://pa1.narvii.com/6417/27c8a8e37fa18bcbdf8b8a2f110020ab97d48f0c_hq.gif"),
                          ],
            'biology': [('Microscope',
                         'https://media.giphy.com/media/l41m3Dps5EQ8W1rZS/giphy.gif'),
                        ("Living Cell Observation",
                         "http://www.composites.ugent.be/movies/anim_Fatigue_online_microscopy.gif"),
                        ("Cockroach Dissection",
                         "http://3.bp.blogspot.com/-9CmeFcEtqIg/Uqbtn6sq6gI/AAAAAAAAAJY/sZXPDJDBzpc/s400/cockroach.gif"),
                        ("Cell Division",
                         "https://j.gifs.com/vMEWeX.gif"),
                        ],
        }
        return render(request, 'coreapp/avilon/student-lab-exp.html', context={'exp_list': exp_lists[labname]})
    except:
        pass
    return render(request, 'coreapp/avilon/student-lab.html')


def classview(request):
    try:
        labname = str(request.GET.get('class')).lower()
        exp_lists = {
            'physics': [
                ('Projectile',
                 'https://kaiserscience.files.wordpress.com/2015/08/horizontally-launched-projectiles.gif',
                 reverse('coreapp:experiment', kwargs={'id': 2})),
                ('Collision', 'https://xmphysics.files.wordpress.com/2019/03/collisiongraphs-a.gif',
                 reverse('coreapp:experiment', kwargs={'id': 1})),
                ("Series-Parallel Circuit",
                 "http://s4.thingpic.com/images/SC/yUMJVwbNDtnrffhX2HHUVH5e.gif"),
                ("Prism Experiment",
                 "https://media0.giphy.com/media/l0MYKMrQnwNvLjYhW/source.gif"),
                ("Young's Experiment",
                 "https://physicsforus.files.wordpress.com/2011/07/doubleslit_animation.gif"),
                ('Simple Pendulum', 'http://www.acs.psu.edu/drussell/Demos/Pendulum/compare-lengths.gif'),
            ],
            'chemistry': [('NaOH-H2SO4 Titration',
                           'https://www.buffaloschools.org/cms/lib/NY01913551/Centricity/Domain/6557/titration1.gif'),
                          ("Bunsen Burner",
                           "http://classroomclipart.com/images/gallery/Animations/Science/TN_bunsen_burner-4-12_cc.gif"),
                          ("Ion Test",
                           "https://pufflesandhoneyadventures.files.wordpress.com/2017/08/metal-ion-flame-test.gif"),
                          ("Precipitation Test",
                           "https://pa1.narvii.com/6417/27c8a8e37fa18bcbdf8b8a2f110020ab97d48f0c_hq.gif"),
                          ],
            'biology': [('Microscope',
                         'https://media.giphy.com/media/l41m3Dps5EQ8W1rZS/giphy.gif'),
                        ("Living Cell Observation",
                         "http://www.composites.ugent.be/movies/anim_Fatigue_online_microscopy.gif"),
                        ("Cockroach Dissection",
                         "http://3.bp.blogspot.com/-9CmeFcEtqIg/Uqbtn6sq6gI/AAAAAAAAAJY/sZXPDJDBzpc/s400/cockroach.gif"),
                        ("Cell Division",
                         "https://j.gifs.com/vMEWeX.gif"),
                        ],
        }
        return render(request, 'coreapp/avilon/student-lab-exp.html', context={'exp_list': exp_lists[labname]})
    except:
        pass
    return render(request, 'coreapp/avilon/student-class.html')


def experiment(request, id=None):
    if id is None:
        return redirect('/')
    name = SIMUID_MAP_FOR_DEMO[id]
    return render(request, 'coreapp/simulations/' + name)


def result(request):
    try:
        labname = str(request.GET.get('class')).lower()
        print(labname)
        if labname in ['physics', 'chemistry', 'biology', 'math', 'bengali', 'english']:
            return render(request, 'coreapp/avilon/student-activity.html')
    except:
        pass
    return render(request, 'coreapp/avilon/student-result.html')


def recording(request):
    try:
        labname = str(request.GET.get('class')).lower()
        print('>', labname)
        if labname in ['physics', 'chemistry', 'biology', 'math', 'bengali', 'english']:
            return render(request, 'coreapp/avilon/topic-activity.html',
                          context={'classname': labname.upper()})
    except:
        pass
    return render(request, 'coreapp/avilon/student-recording.html')

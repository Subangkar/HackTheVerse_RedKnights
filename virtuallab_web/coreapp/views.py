from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

USERID_MAP_FOR_DEMO = {
    'subangkar': 'Student',
    'araf': 'Student',
    'samin': 'Student',
    'joseph': 'Teacher',
    'andrew': 'Teacher',
}


class Index(TemplateView):
    """
    Renders Home Page
    """
    template_name = 'coreapp/avilon/student-home.html'

    def get_context_data(self, **kwargs):
        ctx = {'loggedIn': self.request.user.is_authenticated}
        return ctx


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
            'physics': [('Simple Pendulum', 'http://www.acs.psu.edu/drussell/Demos/Pendulum/compare-lengths.gif'),
                        ("Series-Parallel Circuit",
                         "http://s4.thingpic.com/images/SC/yUMJVwbNDtnrffhX2HHUVH5e.gif"),
                        ("Prism Experiment",
                         "https://media0.giphy.com/media/l0MYKMrQnwNvLjYhW/source.gif"),
                        ("Young's Experiment",
                         "https://physicsforus.files.wordpress.com/2011/07/doubleslit_animation.gif"),
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


def lab_detail(request):
    l = [('Simple Pendulum', 'http://www.acs.psu.edu/drussell/Demos/Pendulum/compare-lengths.gif'),
         ("Young's Experiment", "https://physicsforus.files.wordpress.com/2011/07/doubleslit_animation.gif")] * 6
    return render(request, 'coreapp/avilon/student-lab-exp.html', context={'exp_list': l})


def chart(request):
    return render(request, 'coreapp/avilon/hist-chart.html')
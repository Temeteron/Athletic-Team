from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.views import generic

from AthleticTeamApp.models import Player, Match, CoachingStaffMember, Team ,MatchPlayerStatistics

from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy


from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

# Create your views here.
class ShowCoachingStaffMembers(generic.ListView):
    model = CoachingStaffMember
    template_name = 'coaching_staff_member/showall.html'
    context_object_name = 'coachingstaffmember_list'


class ShowCoachingStaffMember(generic.DetailView):
    model = CoachingStaffMember
    template_name = 'coaching_staff_member/show.html'


class ShowPlayers(generic.ListView):
    model = Player
    template_name = 'player/showall.html'
    context_object_name = 'players_list'

class ShowPlayer(generic.DetailView):
    model = Player
    template_name = 'player/show.html'


class ShowMatches(generic.ListView):
    model = Match
    template_name = 'match/showall.html'
    context_object_name = 'matches_list'

class ShowMatch(generic.DetailView):
    model = Match
    template_name = 'match/show.html'


# Create your views here.
class ShowTeams(generic.ListView):
    model = Team
    template_name = 'team/showall.html'
    context_object_name = 'team_players_list'

class ShowTeam(generic.DetailView):
    model = Team
    template_name = 'team/show.html'

class IndexRanking(TemplateView):
    template_name = 'ranking/index.html'

def login_user(request):
    if 'login' in request.POST:
        logout(request)
        username = password = ''
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('AthleticTeamApp:home'))
    elif 'visitor' in request.POST:
        return HttpResponseRedirect(reverse('AthleticTeamApp:home'))
    return HttpResponseRedirect(reverse('AthleticTeamApp:index'))

    #, context_instance=RequestContext(request)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('AthleticTeamApp:index'))

#@login_required(login_url='/login/')
#@method_decorator(login_required, name='login_user')
class HomeView(TemplateView):
    template_name = 'home/base_site.html'

    #U can come here only if u are logged in
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(HomeView, self).dispatch(*args, **kwargs)

class IndexView(TemplateView):
    #model = User
    template_name = 'Login/index.html'

class AboutUs(TemplateView):
    template_name = 'home/about.html'


class ProfileView(TemplateView):
    template_name = 'home/profile.html'
    
    #U can come here only if u are logged in
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)


class ChangePassView(TemplateView):
    template_name = 'home/change_pass.html'

    #U can come here only if u are logged in
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChangePassView, self).dispatch(*args, **kwargs)


def change_pass(request):
    logged_user = request.user
    text_a = request.POST['text_a']
    text_b = request.POST['text_b']

    if text_a == text_b:
        #change password
        logged_user.set_password(text_b) 
        logged_user.save()
        logout(request)
        return HttpResponseRedirect(reverse('AthleticTeamApp:index'))
    else:
        #prin error mesg MESSAGES DJANGO
        return HttpResponseRedirect(reverse('AthleticTeamApp:changePass'))
      
class Players_stats(generic.DetailView):
    model = Match
    template_name = 'match/players_stats.html'
    
def all_stats(request):
  
  agwnas = request.POST['match']
  name1 = request.POST.getlist('player1')
  name2 = request.POST.getlist('player2')
  minutes = request.POST.getlist('min')
  two_a = request.POST.getlist('2pt-a')
  two_m = request.POST.getlist('2pt_m')
  threept_a = request.POST.getlist('3pt-a')
  threept_m = request.POST.getlist('3pt-m')
  f_a = request.POST.getlist('f-a')
  f_m = request.POST.getlist('f-m')
  to = request.POST.getlist('to')
  off = request.POST.getlist('off')
  defreb = request.POST.getlist('def')
  blk = request.POST.getlist('blk')
  pf = request.POST.getlist('pf')
  pts = request.POST.getlist('pts')
  player = request.POST.getlist('players')
  ass = request.POST.getlist('ass')
  st = request.POST.getlist('st')
  
  
  for i in range(len(name1)):
    
    paiktis = Player.objects.get(first_name = name1[i] , last_name = name2[i]) 
    match1 = Match.objects.get(pk = agwnas)  
    temp = MatchPlayerStatistics(match=match1 ,player=paiktis,started=1)
    temp.time_played = int(minutes[i]) 
    temp.pts = int(pts[i])
    temp.two_pa = int(two_a[i])
    temp.two_pm = int(two_m[i])
    temp.three_pa = int(threept_a[i])
    temp.three_pm = int(threept_m[i])
    temp.fta = int(f_a[i])
    temp.ftm = int(f_m[i])
    temp.tov = int(to[i])
    temp.oreb = int(off[i])
    temp.dreb = int(defreb[i])
    temp.ast = int(ass[i])
    temp.stl = int(st[i])
    temp.blk = int(blk[i])
    temp.pf = int(pf[i])
    
    temp.save()

  return HttpResponseRedirect(reverse('AthleticTeamApp:ShowMatches'))



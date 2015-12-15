from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.views import generic

from AthleticTeamApp.models import Player, Match, CoachingStaffMember, Team, Ranking

from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy

from django.views.generic.detail import SingleObjectMixin
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

import datetime
from django.utils import timezone

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

    def get_queryset(self):
        """
        Return the last three published Match (not including those set to be
        published in the future).
        """
        return Match.objects.filter(
            date__lte=timezone.now()
        ).order_by('-date')

class ShowMatch(generic.DetailView):
    model = Match
    template_name = 'match/show.html'


class CreateMatch(generic.ListView):
    model = Team
    template_name = 'match/create_match.html'
    context_object_name = "teams_list"

# Create your views here.
class ShowTeams(generic.ListView):
    model = Team
    template_name = 'team/showall.html'
    context_object_name = 'team_players_list'

class ShowTeam(generic.DetailView):
    model = Team
    template_name = 'team/show.html'


def match_creator(request):
    team_a_id = request.POST['team_a']
    team_a = get_object_or_404(Team, pk=team_a_id)

    team_b = request.POST['team_b']

    points_a = int(request.POST.get('points_a', False))
    points_b = int(request.POST.get('points_b', False))
    

    stadium = request.POST['stadium']
    info = request.POST['info']

    home_away_team = request.POST['home_away']
    print "PAOK"
    match_to_send = Match(home_pts=points_a, away_pts=points_b, stadium=stadium, date=datetime.datetime.now(), time=timezone.now(), info=info, home_team=team_a, away_team=team_b, home_away=home_away_team)
    
    match_to_send.save()  

    return HttpResponseRedirect(reverse('AthleticTeamApp:home'))


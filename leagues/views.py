from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"all": League.objects.all(),
		"baseballLeagues": League.objects.filter(sport="Baseball"),
		"womensLeagues": League.objects.filter(name__contains="Women"),
		"hockeyLeagues": League.objects.filter(sport__contains="Hockey"),
		"nonFootballLeagues": League.objects.exclude(sport="Football"),
		"conferences": League.objects.filter(name__contains="Conference"),
		"atlantic": League.objects.filter(name__contains="Atlantic"),
		"teams": Team.objects.all(),
		"dallasTeams": Team.objects.filter(location="Dallas"),
		"raptorTeams": Team.objects.filter(team_name="Raptors"),
		"cityTeams": Team.objects.filter(location__contains="City"),
		"tTeams": Team.objects.filter(team_name__startswith="T"),
		"orderedByLocation": Team.objects.all().order_by("location"),
		"reverseOrderTeam": Team.objects.all().order_by("team_name").reverse(),
		"players": Player.objects.all().order_by("last_name"),
		"cooperPlayers": Player.objects.filter(last_name="Cooper"),
		"joshuaPlayers": Player.objects.filter(first_name="Joshua"),
		"cooperNotJoshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"alexanderOrWyatt": Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt")
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
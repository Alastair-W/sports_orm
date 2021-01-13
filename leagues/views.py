from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

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
		"teams": Team.objects.all().order_by("location", "team_name"),
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
		"alexanderOrWyatt": Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt"),
		"atlanticHockey": League.objects.filter(name__contains="Atlantic", sport__contains="Hockey"),
		"teamBosSta": Team.objects.filter(location="Boston", team_name="Stallions"),
		"intBaseConf": Team.objects.filter(league=League.objects.get(name="International Baseball Conference")),
		"amFedSoc": Team.objects.filter(league=League.objects.get(name="Atlantic League of Ice Hockey")),
		"footballLeagues": League.objects.filter(sport="Football"),
		"teamsSophia": Player.objects.filter(first_name="Sophia"),
		"teamsGonzales": Player.objects.filter(last_name="Gonzales"),
		"johnHarris": Player.objects.get(first_name="John", last_name="Harris"),
		"ontarioColts": Team.objects.get(location="Ontario", team_name="Colts"),
		"nevadaBJ": Team.objects.get(location="Nevada", team_name="Blue Jays"),
		"jacksonWhite": Player.objects.get(first_name="Jackson", last_name="White"),
		"teamPlayerCount": Team.objects.annotate(player_count=Count('all_players')).order_by('-player_count'),
		"allPlayers": Player.objects.annotate(numTeams=Count('all_teams')).order_by('-numTeams')

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
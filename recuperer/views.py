from django.shortcuts import render, HttpResponse
from math import pow
from recuperer.models import coordonnee

def affiche_data(request,id1,id2, id3, id4, id5, id6, year, month, day,hours, m, sec):
	def Longitude(id1,id2):
		return int(id1) + int(id2)*10**-(len(id2))
	def Latitude(id3,id4):
		return int(id3) + int(id4)*10**-(len(id4))
	def Vitesse(id5,id6):
		return int(id5) + int(id6)*10**-(len(id6))
	def Time(year, month, day, m, sec):
		return str(year) + '-' + str(month) + '-' + str(day) + ' ' + str(hours) + ':' + str(m) + ':' + str(sec)
	enregistrement = coordonnee(longitude = Longitude(id1,id2),latitude = Latitude(id3,id4), vitesse = Vitesse(id5,id6), date = Time(year, month, day, m, sec) )
	enregistrement.save()
	return HttpResponse(f"{Longitude(id1,id2)} {Latitude(id3,id4)} {Vitesse(id5,id6)} {Time(year,month,day,m,sec)}")


# Create your views here.

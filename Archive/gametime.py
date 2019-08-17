#!/usr/bin/env python

from igdb_api_python.igdb import igdb
import sys
import random

igdb = igdb("a3a100cec5fd39c002aad011e85d2dea")

def gameslist_genres(genres):
	for i in range(len(genres)):
		result = igdb.genres({
			'ids': genres[i],
			'fields': 'games',
			})
		gameslist = []
		for game in result.body:
			gameslist.append(game['games'])
		gameslist = gameslist[0]
		return(gameslist)


def ids(fav1, fav2, fav3):
	favgames = [fav1, fav2, fav3]
	id = []
	result = igdb.games({
		'search': fav1,
		'fields': 'id',
		})
	for game in result.body:
		id.append(game['id'])
		break

	result1 = igdb.games({
		'search': fav2,
		'fields': 'id',
		})
	for game in result1.body:
		id.append(game['id'])
		break

	result2 = igdb.games({
		'search': fav3,
		'fields': 'id',
		})
	for game in result2.body:
		id.append(game['id'])
		break

	return(id)
	
def genres(fav1, fav2, fav3, id):
	id = ids(fav1, fav2, fav3)
	k = 0
	genre = []
	for i in range(3):
		try:
			result = igdb.games({
			'ids': id[i],
			'fields': 'genres',
			})
			for game in result.body:
				genre.append(game['genres'])
		except:
			k += 1
			print("Unable to complete: " + str(id[i]))
	genres = []
	for elem in genre:
		for j in range (len(elem)):
			if elem[j] not in genres:
				genres.append(elem[j])
	return(genres)

def keywords(id):
	k = 0
	keys = []
	for i in range(3):
		try:
			result = igdb.games({
			'ids': id[i],
			'fields': 'keywords',
			})
			for game in result.body:
				keys.append(game['keywords'])
		except:
			k += 1
			print("Unable to complete: " + str(id[i]))
	keys1 = []
	for elem in keys:
		for j in range (len(elem)):
			if elem[j] not in keys1:
				keys1.append(elem[j])
	random.shuffle(keys1)
	return(keys1[0:4])

def gameslist_keywords(gameslist, keywords):
	for i in range(len(keywords)):
		result = igdb.keywords({
			'ids': keywords[i],
			'fields': 'games',
			})
		keylist = []
		for game in result.body:
			keylist.append(game['games'])
		keylist = keylist[0]
		return(keylist)

def compare_gameslist(gameslist1, gameslist2):
	gameslist3 = []
	for elem in gameslist1:
		if elem in gameslist2:
			if elem not in gameslist3:
				gameslist3.append(elem)
	return(gameslist3)

def finalgames(gameslist):
	#gameslist1 = gameslist[0:len(gameslist):len(gameslist)//4]
	random.shuffle(gameslist)
	gameslist = gameslist[0:5]
	#gameslist1.append(gameslist[1:2])
	#gameslist1.append(gameslist[((len(gameslist)//2)-1), len(gameslist)//2])
	#gameslist1.append(gameslist[len(gameslist)-2, len(gameslist)-1])
	#gameslist1.append(gameslist[((len(gameslist)//3)-1), len(gameslist)//3])
	#gameslist1.append(gameslist[((len(gameslist)//4)-1), len(gameslist)//4])
	result = igdb.games ({
		"ids": gameslist,
		"fields": "name"
		})
	gnames = []
	for gamename in result.body:
		gnames.append(gamename["name"])
	return(gnames)


def main(fav1, fav2, fav3):
	id = ids(fav1, fav2, fav3)
	genres1 = genres(fav1, fav2, fav3, id)
	keys = keywords(id)
	gameslist1 = gameslist_genres(genres1)
	gameslist2 = gameslist_keywords(gameslist1, keys)
	gameslist3 = compare_gameslist(gameslist1, gameslist2)
	finalgnames = finalgames(gameslist3)
	print ("")
	for game in finalgnames:
		print(game)

main(sys.argv[1], sys.argv[2], sys.argv[3])

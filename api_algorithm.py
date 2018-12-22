from igdb_api_python.igdb import igdb
import sys
import random

# In order for the algorithm to work, you must sign up for the API on https://api.igdb.com/
# You will receive a key to the API once you sign up. Next, type the key in between the quotations on line 9.
# This activates the API and stores the data from it in variable igdb. The algorithm will correctly work now.

igdb = igdb("")

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
	random.shuffle(gameslist)
	gameslist = gameslist[0:5]
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
	print (finalgnames[0] + " | " + finalgnames[1] 
           + " | " + finalgnames[2] + " | " + finalgnames[3] + " | " + finalgnames[4])
	# print ("1. " + finalgnames[0])
	# print ("2. " + finalgnames[1])
	# print ("3. " + finalgnames[2])
	# print ("4. " + finalgnames[3])
	# print ("5. " + finalgnames[4])
  
main(sys.argv[1], sys.argv[2], sys.argv[3])

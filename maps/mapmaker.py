import random
import json

tmap = []
bases = []

def randomize(x, y):
	result = []
	for i in range(x):
		temp = []
		for j in range(y // 2):
			temp.append(random.uniform(0.2, 1.0))
		for j in temp[::-1]:
			temp.append(j)
		result.append(temp)
	return result

def add_base(x, y, team, energy=150):
	if team == "A":
		bases.append({"x":x, "y":y, "team":"A", "energy":150})
		bases.append({"x":x, "y":len(tmap[0]) - y, "team":"B", "energy":150})
	if team == "B":
		bases.append({"x":x, "y":y, "team":"B", "energy":150})
		bases.append({"x":x, "y":len(tmap[0]) - y, "team":"B", "energy":150})
	if team == "Neutral":
		bases.append({"x":x, "y":y, "team":"Neutral", "energy":energy})
		bases.append({"x":x, "y":len(tmap[0]) - y, "team":"Neutral", "energy":energy})

tmap = randomize(32, 32)
add_base(6, 6, "A")
f = open("maptestsmall.json", "w", encoding="utf-8")
f.write(json.dumps({"map":tmap, "bases":bases}))
f.close()
import json
import os
import random
import bottle
from math import *
def food_location():
	data = bottle.request.json
	food_locations = data["board"]["food"]
	head_location = data["you"]["body"][0]
	dist = 1000
	loc = [-1,-1]
	for i in food_locations:
		temp = sqrt((i["x"]-head_location["x"])**2+(i["y"]-head_location["y"])**2)
		if temp<dist:
			loc[0] = i["x"]
			loc[1] = i["y"]
			dist = temp 
	print(loc[0], loc[1])
	return loc
	#(x,y) is the location of the 
def food_direction():
	data = bottle.request.json
	food_loc = food_location()
	print(food_loc)
	head_loc = data["you"]["body"][0]
	print(head_loc)
	body_loc = data["you"]["body"][1]
	print(body_loc)
	if data["turn"] > 1:
		if food_loc[0]< head_loc["x"] and body_loc["x"]>=head_loc["x"]:
			return "left"
		elif food_loc[0]>head_loc["x"] and body_loc["x"]<=head_loc["x"]:
			return "right"
		elif food_loc[1]<head_loc["y"] and body_loc["y"]>=head_loc["y"]:
			return "up"
		elif food_loc[1]>head_loc["y"] and body_loc["y"]<=head_loc["y"]:
			return "down"
	else:
		return "down"
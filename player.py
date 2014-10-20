from items import *
from map import places

inventory = []

stats = {
	"Health": 100,

	"Strength": 10,

	"Defence": 10,

	"Speed": 10
}

# Start game at the reception
current_place = places["Home"]

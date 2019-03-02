import json
import os
import random
import bottle

from api import ping_response, start_response, move_response, end_response

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start(): #comment was herr
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))

    color = "#00FF00"

    return start_response(color)


@bottle.post('/move')

def nearestSnakeDirection():
    data = bottle.request.json
    you = data["you"]
    id = you["id"]
    snakes = data["snakes"]
    own_coordinates = you["body"]
    ownHead = own_coordinates[0]
    headX = ownHead["x"]
    headY = ownHead["y"]
    other_snakes = deleteOwnSnake(snakes,id)
    other_snakes_x = []
    other_snakes_y = []
    for z in range(0,len(other_snakes)):
        info = other_snakes[z]
        other_snakes_x.append(info["body"][z]["x"])
        other_snakes_y.append(info["body"][z]["y"])

    nearestX = None #exagerated number   #### NOTE: nearestX and nearestY both refer to a single body part of a specific enemy snake
    nearestY = None
    """
    for p in range(0,len(other_snakes)): ### need only care about the snakes that are on the same y and x as us
        if(other_snakes_x[p]<nearestX):
            nearestX = other_snakes_x
        if(other_snakes_y[p]<nearestY):
            nearestY
    """

    bodies_on_our_x = []
    bodies_on_our_y = []
    for o in range(0,len(other_snakes)):
        if(other_snakes_x[o]==headX):
            bodies_on_our_x.append(other_snakes_x[o])
        if(other_snakes_y[o]==headY):
            bodies_on_our_x.append(other_snakes_y[o])

    nearestX = min(bodies_on_our_x, key=lambda x:abs(x-headX))
    nearestY = min(bodies_on_our_y, key=lambda x:abs(x-headY))

    if(nearestX<nearestY):
        return "straight"
    if(nearestY<nearestX):
        return "left"

    #print(data)



def deleteOwnSnake(snakes, own_id): #deletes the location of our snake from the list of snakes
    for x in range(0,len(snakes)):
        i = snakes[x]
        if(i["id"]==own_id):
            del snakes[x]
            return snakes





def move():
    data = bottle.request.json
    last = "unknown"

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    # print(json.dumps(data))
    print(json.dumps(data["board"]["snakes"][0]["body"][0]["y"]))
    if data["board"]["snakes"][0]["body"][0]["y"] <= 2:
        return move_response("left")
        last = "left"

    elif data["board"]["snakes"][0]["body"][0]["y"]>= 2:
        return move_response("up")


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
        nearestSnakeDirection()
        print("HIIIII")
    )

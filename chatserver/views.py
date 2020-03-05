async_mode = None

import os

from django.http import HttpResponse
import socketio

basedir = os.path.dirname(os.path.realpath(__file__))
sio = socketio.Server(async_mode=async_mode)

users = [];

def index(request):
    return HttpResponse(open(os.path.join(basedir, 'static/index.html')))

@sio.event
def join(sid, message):
    global users
    newUser = message['name']
    if(newUser in users):
        sio.emit('welcome', {'error': 'EXISTING_NAME'}, room=sid)
    else:
        users.append(message['name'])
        sio.emit('welcome', {'users': users, 'name':newUser}, room=sid)

@sio.event
def rejoin(sid, message):
    global users
    existingUser = message['name']
    if (existingUser in users):
        sio.emit('welcome', {'users': users, 'name':existingUser}, room=sid)
    else:
        sio.emit('welcome', {'error': 'EXPIRED'}, room=sid)

@sio.event
def say(sid, message):
    print(message)
    sio.emit('heard', message)

@sio.event
def leave(sid, message):
    sio.leave_room(sid, message['room'])
    sio.emit('my_response', {'data': 'Left room: ' + message['room']},
             room=sid)


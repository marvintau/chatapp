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
        sio.emit('logged', {'error': 'EXISTING_NAME'}, room=sid)
    else:
        users.append(message['name'])
        
        # server should broadcast the userlist when new user joins, since
        # other users doesn't know the updated list.
        sio.emit('welcome', {'users': users}, skip_sid=sid)

        # and send the user list to the one who just logged in
        sio.emit('logged', {'users': users, 'name':newUser}, room=sid)

@sio.event
def rejoin(sid, message):
    global users
    existingUser = message['name']
    if (existingUser in users):
        sio.emit('logged', {'users': users, 'name':existingUser}, room=sid)
    else:
        # Typically when server is restarted yet we are not using a database
        # to store users.
        sio.emit('logged', {'error': 'EXPIRED'}, room=sid)

@sio.event
def say(sid, message):
    print(message)
    sio.emit('heard', message)

@sio.event
def leave(sid, message):
    sio.leave_room(sid, message['room'])
    sio.emit('my_response', {'data': 'Left room: ' + message['room']},
             room=sid)


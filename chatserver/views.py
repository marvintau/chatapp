async_mode = None

import os

from django.http import HttpResponse
import socketio

basedir = os.path.dirname(os.path.realpath(__file__))
sio = socketio.Server(async_mode=async_mode)

users = {};

def index(request):
    return HttpResponse(open(os.path.join(basedir, 'static/index.html')))

@sio.event
def join(sid, message):
    global users
    users[sid] = message['name']
    print(users)
    sio.emit('join', users)


@sio.event
def leave(sid, message):
    sio.leave_room(sid, message['room'])
    sio.emit('my_response', {'data': 'Left room: ' + message['room']},
             room=sid)


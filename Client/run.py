import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    while 0 < 10:
         message = input("Mande a mensagem: ")
         sio.emit('message', {'mensagem': message})
         print('Eu: ' ,message)

@sio.on('message')
def on_message(data):
    print('Mensagem' ,data)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://127.0.0.1:5000')
sio.wait()


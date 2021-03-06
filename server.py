from pykeyboard import PyKeyboard
import select, socket

BROADCAST = '<broadcast>'
IP_BROADCAST = '192.168.0.255'

port = 12345  # where do you expect to get a msg?
bufferSize = 1024 # whatever you need
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((BROADCAST, port))
# s.setblocking(0)
k = PyKeyboard()

while True:
    # data, addr = s.recvfrom(1024)
    result = select.select([s],[],[])
    msg = result[0][0].recv(bufferSize)
    # print msg
    print msg

    if msg == 'octava5':
        k.tap_key(',')
    if msg == 'octava4':
        k.tap_key('.')
    if msg == 'octava3':
        k.tap_key('/')
    if msg == 'octava2':
        k.tap_key('=')
    if msg == 'octava0':
        k.tap_key('[')
    if msg == 'octava-1':
        k.tap_key(']')
    if msg == 'octava-2':
        k.tap_key('\\')
    if msg == 'play':
        k.type_string('play')
    if msg == 'stop':
        k.type_string('stop')
    if msg == 'pause':
        k.type_string('pause')
    if msg == 'tap':
        k.type_string('tap')

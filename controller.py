
from socketIO_client import SocketIO,BaseNamespace
import config
import ai
import time
logic=ai.AI()
io=SocketIO('localhost',5000)

class Game(BaseNamespace):
    def on_connect(self):
        print('[Connected]')
        self.emit('init',config.token)

    def on_reconnect(self):
        print('[Reconnected]')

    def on_disconnect(self):
        print('[Disconnected]')

    def on_result(self,map):
        # print map['data']
        result=logic.turn(map['data'])
        # time.sleep(1)
        self.emit('touch',config.token,result[0],result[1])

game = io.define(Game, '/game')
# game.emit('init',config.token)
io.wait()

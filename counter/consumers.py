import json
import time
from channels.generic.websocket import WebsocketConsumer

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        number = 0

        for i in range(100):
            number += 1
            self.send(json.dumps({'message': number}))
            time.sleep(1)
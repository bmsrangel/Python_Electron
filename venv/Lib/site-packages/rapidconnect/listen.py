import requests
import websocket
import json
import threading

class Listen():
    def __init__(self, project, token, package, event, params,
               on_join=None, on_message=None, on_close=None, on_error=None):
        self.project = project
        self.token = token
        self.on_join = on_join
        self.on_message = on_message
        self.on_close = on_close
        self.on_error = on_error
        self.webhook_params = params
        self.user_id = "%s.%s_%s:%s" % (package, event, self.project, self.token)

    def tokenUrl(self, user_id):
        return "https://webhooks.rapidapi.com/api/get_token?user_id=%s" % (user_id)

    def socketUrl(self, token):
        return "wss://webhooks.rapidapi.com/socket/websocket?token=%s" % (token)

    def on_open(self, ws):
        users_socket = "users_socket:%s" % (self.socket_token)
        connect = {'topic': users_socket, 'event': 'phx_join', 'ref': '1', 'payload': self.webhook_params}
        self.ws.send(json.dumps(connect))

    def on_msg_received(self, ws, message):
        decoded = json.loads(message)
        if decoded["event"] == "phx_reply" and decoded["payload"]["status"] == "ok" and self.on_join:
            self.on_join()
        if decoded["event"] == "new_msg" and decoded.get("payload").get("token") == None:
            self.on_error(decoded["payload"]["body"])
        elif decoded["event"] == "new_msg" and self.on_message:
            self.on_message(decoded["payload"]["body"])
        elif self.on_error:
            self.on_error(decoded["payload"]["body"])
        return

    def send_heartbeat(self):
        heartbeat = {"topic": "phoenix", "event": "heartbeat", "ref": "1", "payload": {}}
        self.ws.send(json.dumps(heartbeat))

    def on_closed(self, ws):
        self.on_close()
        
    def listen(self):
        response = requests.get(self.tokenUrl(self.user_id), auth=(self.project, self.token))
        decoded = response.json()
        self.socket_token = decoded["token"]
        self.ws = websocket.WebSocketApp(self.socketUrl(self.socket_token),
                                         on_open = self.on_open,
                                         on_error = self.on_closed,
                                         on_message = self.on_msg_received,
                                         on_close = self.on_closed,
                                         on_ping=self.send_heartbeat)
        wst = threading.Thread(target=self.ws.run_forever, kwargs={'ping_interval': 30})
        wst.start()

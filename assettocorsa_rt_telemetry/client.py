from socket import socket, AF_INET, SOCK_DGRAM
from select import select
from actypes import *


class ACClient:
    def __init__(self, hostname="127.0.0.1", blocking=True):
        self.server = (hostname, 9996)
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.setblocking(blocking)
        self.handShakerResponse = None
        self.lastCarInfo = None

    def close(self):
        self._send_message(HandShaker.pack(1, 1, 3))
        self.socket.close()
        print("Closure")

    def __exit__(self):
        self.close()

    def _send_message(self, message):
        try:
            self.socket.sendto(message, self.server)
        except TimeoutError:
            print("Tried too much for too long")

    def _get_message(self):
        message = None
        try:
            message = self.socket.recv(1024)
        except ConnectionResetError:
            print("This connection was reset")
        return message

    def start(self):
        self._send_message(HandShaker.pack(1, 1, 0))
        message = resolve_handshake_response(self._get_message())
        if message.identifier == 4242 and message.version == 1:
            print("Nice handshake")
        self.handShakerResponse = message

    def enable_realtime_car_info(self):
        self._send_message(HandShaker.pack(1, 1, 1))

    def _get_last_message(self):
        message = None
        while select([self.socket], [], [], 0.01)[0]:
            message = self.socket.recv(1024)
        return message

    def get_car_info(self):
        message = None
        tries = 0
        while message is None:
            message = self._get_last_message()
            tries += 1
            if tries > 5:
                print("No message received, returning last known value")
                return self.lastCarInfo

        _car_info = resolve_car_info(message)
        if _car_info is not None:
            self.lastCarInfo = _car_info
        return self.lastCarInfo


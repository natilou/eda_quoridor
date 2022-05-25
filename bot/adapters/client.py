from abc import ABC, abstractmethod

class Client(ABC):
    
    @abstractmethod
    def __init__(self, client):
        pass
    
    @abstractmethod
    async def send(self, action, data):
        pass

    @abstractmethod
    async def send_message(self, request_data, move):
        pass

    @abstractmethod
    async def receive_request(self):
        pass

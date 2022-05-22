from abc import ABC, abstractmethod
import asyncio

class Handler(ABC):

    def set_next(self, handler):
        pass
    
    @abstractmethod
    async def perform_an_action(request_data):
        pass
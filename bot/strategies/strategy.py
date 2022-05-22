from .handler import Handler
import asyncio
from abc import ABC, abstractmethod

# Strategy interface
class Strategy(Handler):
    next_handler: Handler = None

    @abstractmethod 
    async def perform_an_action(request_data):
        pass
    
    def set_next(self, handler: Handler) -> Handler:
        self.next_handler = handler
        return handler

    def get_next_strategy(self):
        return self.next_handler
    
    
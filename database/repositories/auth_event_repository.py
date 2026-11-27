from base_repository import BaseRepository
from tables import AuthEvent

class AuthEventRepository(BaseRepository[AuthEvent]):
    def __init__(self, session):
        super().__init__(session, AuthEvent)

    async def add_event(self, name: str):
        ...
        

from base_repository import BaseRepository
from tables import Sessions

class SessionsRepository(BaseRepository[Sessions]):
    def __init__(self, session):
        super().__init__(session, Sessions)

    async def get_by_user(self, user_id):
        ...

    async def revoke(self, session_id):
        ...
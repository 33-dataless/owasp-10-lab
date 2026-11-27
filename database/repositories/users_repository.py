from base_repository import BaseRepository
from tables import Users

class UsersRepository(BaseRepository[Users]):
    def __init__(self, session):
        super().__init__(session, Users)

    async def get_by_username(self, username: str):
        ...

    async def get_by_email(self, email: str):
        ...
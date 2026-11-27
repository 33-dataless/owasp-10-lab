from base_repository import BaseRepository
from tables import Roles

class RolesRepository(BaseRepository[Roles]):
    def __init__(self, session):
        super().__init__(session, Roles)

    async def get_by_name(self, name: str):
        ...
        

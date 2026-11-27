from base_repository import BaseRepository
from tables import UserPreferences

class UserPreferencesRepository(BaseRepository[UserPreferences]):
    def __init__(self, session):
        super().__init__(session, UserPreferences)

    async def get_by_user(self, user_id):
        ...
from base_repository import BaseRepository
from tables import PasswordResetTokens

class PasswordResetTokenRepository(BaseRepository[PasswordResetTokens]):
    def __init__(self, session):
        super().__init__(session, PasswordResetTokens)

    async def get_by_token_hash(self, token_hash: str):
        ...
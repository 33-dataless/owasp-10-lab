from base_repository import BaseRepository
from tables import RequestLogs

class RequestLogsRepository(BaseRepository[RequestLogs]):
    def __init__(self, session):
        super().__init__(session, RequestLogs)

    async def get_by_user(self, user_id):
        ...
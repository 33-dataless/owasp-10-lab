from typing import Generic, TypeVar

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base

ModelType = TypeVar("ModelType", bound=Base)
class BaseRepository(Generic[ModelType]):
    def __init__(self, session: AsyncSession, model: type[ModelType]):
        self.session = session
        self.model = model

    async def create(self, data: dict) -> ModelType:
        ...

    async def get_by_id(self, id: int | str) -> ModelType | None:
        ...

    async def get_all(self) -> list[ModelType]:
        ...

    async def delete(self, id: int | str) -> bool:
        ...

    async def exists(self, id: int | str) -> bool:
        ...



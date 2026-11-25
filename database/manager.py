from .database import Database
from .connection import DatabaseConnection

database = Database()
db = DatabaseConnection(database)

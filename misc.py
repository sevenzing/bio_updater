from config import credentials
from client import Client

__all__ = ("client_account",)

client_account = Client(**credentials, try_logging_in=True)

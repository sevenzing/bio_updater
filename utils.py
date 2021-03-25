import socket
from config import INTERNET_CHECK_URL

def is_connected():
    """
    Return true if script 
    have connection to internet
    """
    try:
        socket.create_connection((INTERNET_CHECK_URL, 53))
        return True
    except OSError:
        return False
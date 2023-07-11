from aiohttp import ClientSession

from .coind import CoindImplementation
from .http import HttpProvider


class CoindSession:
    """
    Coind session context manager.

    Attributes:
        http_provider (HttpProvider): HTTP provider for Coind.
        session (ClientSession): AIOHTTP client session.
    """

    def __init__(self, username, password, port=5996, host='127.0.0.1'):
        """
        Initialize the CoindSession instance.

        Args:
            username (str): Coind username.
            password (str): Coind password.
            port (int): Coind port (default is 5996).
            host (str): Coind host (default is '127.0.0.1').
        """
        self.http_provider = HttpProvider(f'http://{username}:{password}@{host}:{port}')
        self.session = None

    async def __aenter__(self):
        """
        Enter the CoindSession context.

        Returns:
            CoindImplementation instance.
        """
        self.session = ClientSession()
        return CoindImplementation(self.http_provider, self.session)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the CoindSession context.

        Args:
            exc_type: Exception type.
            exc_val: Exception value.
            exc_tb: Exception traceback.
        """
        await self.session.close()

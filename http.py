import json
from aiohttp import ClientSession

from .exceptions import CoindError


class HttpProvider:
    """
    HTTP provider for Coind.

    Attributes:
        client (HttpClient): HTTP client for making requests.
    """

    def __init__(self, url):
        """
        Initialize the HttpProvider instance.

        Args:
            url (str): URL of the Coind server.
        """
        self.client = HttpClient(url)

    async def request(self, method, params, session=None):
        """
        Make an HTTP request to Coind.

        Args:
            method (str): Coind method.
            params (list): Method parameters.
            session (ClientSession): AIOHTTP client session.

        Returns:
            Result of the Coind request.
        """
        async with ClientSession() as new_session:
            return await self.client.request(method, params, session or new_session)


class HttpClient:
    """
    HTTP client for making requests to Coind.

    Attributes:
        url (str): URL of the Coind server.
        id (int): Request ID counter.
    """

    def __init__(self, url):
        """
        Initialize the HttpClient instance.

        Args:
            url (str): URL of the Coind server.
        """
        self.url = url
        self.id = 0

    async def request(self, method, params, session):
        """
        Make an HTTP request to Coind.

        Args:
            method (str): Coind method.
            params (list): Method parameters.
            session (ClientSession): AIOHTTP client session.

        Returns:
            Result of the Coind request.

        Raises:
            CoindError: If the Coind request returns an error.
        """
        self.id += 1
        data = {
            'method': method,
            'params': params,
            'id': self.id,
            'jsonrpc': '2.0',
        }
        async with session.post(
            self.url,
            headers={'Content-Type': 'application/json'},
            data=json.dumps(data),
        ) as resp:
            json_obj = await resp.json()
            if json_obj.get('error', None):
                raise CoindError(
                    json_obj['error']['code'],
                    json_obj['error']['message'],
                )
            else:
                return json_obj['result']

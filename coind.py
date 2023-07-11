from abc import ABC, abstractmethod

from aiohttp import ClientSession

from .modules.blockchain import Blockchain
from .modules.control import Control
from .modules.generating import Generating
from .modules.mining import Mining
from .modules.network import Network
from .modules.rawtransactions import RawTransactions
from .modules.util import Util
from .modules.wallet import Wallet
from .modules.zmq import Zmq


class Coind(ABC):
    """
    Абстрактный базовый класс для Coind.

    Атрибуты:
        provider (HttpProvider): HTTP-провайдер для Coind.
        session (ClientSession): AIOHTTP-сессия клиента.
        id (int): Счетчик ID запросов.
    """

    def __init__(self, http_provider, session):
        """
        Инициализирует экземпляр Coind.

        Args:
            http_provider (HttpProvider): HTTP-провайдер для Coind.
            session (ClientSession): AIOHTTP-сессия клиента.
        """
        self.provider = http_provider
        self.session = session
        self.id = 0

    @abstractmethod
    async def fetch(self, method, params):
        """
        Абстрактный метод для получения данных от Coind.

        Args:
            method (str): Метод Coind.
            params (list): Параметры метода.

        Returns:
            Результат запроса к Coind.
        """
        pass


class CoindImplementation(Coind):
    """
    Реализация абстрактного класса Coind.

    Атрибуты:
        provider (HttpProvider): HTTP-провайдер для Coind.
        session (ClientSession): AIOHTTP-сессия клиента.
        blockchain (Blockchain): Экземпляр модуля Blockchain.
        control (Control): Экземпляр модуля Control.
        generating (Generating): Экземпляр модуля Generating.
        mining (Mining): Экземпляр модуля Mining.
        network (Network): Экземпляр модуля Network.
        raw_transactions (RawTransactions): Экземпляр модуля RawTransactions.
        util (Util): Экземпляр модуля Util.
        wallet (Wallet): Экземпляр модуля Wallet.
        zmq (Zmq): Экземпляр модуля Zmq.
    """

    def __init__(self, http_provider, session):
        super().__init__(http_provider, session)
        self.blockchain = Blockchain(self)
        self.control = Control(self)
        self.generating = Generating(self)
        self.mining = Mining(self)
        self.network = Network(self)
        self.raw_transactions = RawTransactions(self)
        self.util = Util(self)
        self.wallet = Wallet(self)
        self.zmq = Zmq(self)

    async def fetch(self, method, params=None):
        """
        Получает данные от Coind.

        Args:
            method (str): Метод Coind.
            params (list): Параметры метода (по умолчанию None).

        Returns:
            Результат запроса к Coind.
        """
        if params is None:
            params = []
        return await self.provider.request(method, params, session=self.session)

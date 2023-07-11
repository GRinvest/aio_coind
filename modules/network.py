from typing import Optional


class Network:

    def __init__(self, coind_implementation):
        self.coind_implementation = coind_implementation

    async def add_node(self, node: str, action: str):
        """Добавляет, удаляет или выполняет одноразовое подключение к узлу.

        Args:
            node (str): Адрес узла.
            action (str): Действие, которое нужно выполнить ("add", "remove" или "onetry").
        """
        return await self.coind_implementation.fetch('addnode', [node, action])

    async def capd(self):
        """Включает CAP демона."""
        return await self.coind_implementation.fetch('capd')

    async def clear_banned(self):
        """Очищает список заблокированных адресов."""
        return await self.coind_implementation.fetch('clearbanned')

    async def clear_block_stats(self):
        """Очищает статистику блоков."""
        return await self.coind_implementation.fetch('clearblockstats')

    async def disconnect_node(self, node: str):
        """Отключает указанный узел.

        Args:
            node (str): Адрес узла.
        """
        return await self.coind_implementation.fetch('disconnectnode', [node])

    async def expedited(self, item: str, node_ip: str, state: str):
        """Устанавливает ускоренный режим передачи блоков или транзакций для указанного узла.

        Args:
            item (str): Элемент, для которого нужно установить ускоренный режим ("block" или "tx").
            node_ip (str): IP-адрес узла.
            state (str): Состояние ускоренного режима ("on" или "off").
        """
        return await self.coind_implementation.fetch('expedited', [item, node_ip, state])

    async def get_added_node_info(self, dns: bool, node: Optional[str] = None):
        """Возвращает информацию о добавленных узлах.

        Args:
            dns (bool): Использовать DNS для идентификаторов узлов.
            node (Optional[str]): Идентификатор узла (опционально).

        Returns:
            dict: Информация о добавленных узлах.
        """
        if node is not None:
            return await self.coind_implementation.fetch('getaddednodeinfo', [dns, node])
        else:
            return await self.coind_implementation.fetch('getaddednodeinfo', [dns])

    async def get_connection_count(self) -> int:
        """Возвращает количество активных подключений к узлу."""
        return await self.coind_implementation.fetch('getconnectioncount')

    async def get_net_totals(self):
        """Возвращает статистику сетевого трафика."""
        return await self.coind_implementation.fetch('getnettotals')

    async def get_network_info(self):
        """Возвращает информацию о сети."""
        return await self.coind_implementation.fetch('getnetworkinfo')

    async def get_peer_info(self, peer_ip: Optional[str] = None):
        """Возвращает информацию о пирах.

        Args:
            peer_ip (Optional[str]): IP-адрес пира (опционально).

        Returns:
            List[dict]: Список информации о пирах.
        """
        if peer_ip is not None:
            return await self.coind_implementation.fetch('getpeerinfo', [peer_ip])
        else:
            return await self.coind_implementation.fetch('getpeerinfo')

    async def get_traffic_shaping(self):
        """Возвращает информацию о настройках ограничения трафика."""
        return await self.coind_implementation.fetch('gettrafficshaping')

    async def list_banned(self):
        """Возвращает список заблокированных адресов."""
        return await self.coind_implementation.fetch('listbanned')

    async def ping(self):
        """Отправляет ping-запрос к узлу."""
        return await self.coind_implementation.fetch('ping')

    async def push_tx(self, node: str):
        """Отправляет транзакцию узлу.

        Args:
            node (str): Адрес узла.
        """
        return await self.coind_implementation.fetch('pushtx', [node])

    async def save_msg_pool(self):
        """Сохраняет пул сообщений в файл."""
        return await self.coind_implementation.fetch('savemsgpool')

    async def set_ban(self, ip: str, action: str, bantime: Optional[int] = None, absolute: Optional[bool] = False):
        """Блокирует или разблокирует адрес источника.

        Args:
            ip (str): IP-адрес или подсеть.
            action (str): Действие ("add" или "remove").
            bantime (Optional[int]): Время блокировки в секундах (опционально).
            absolute (Optional[bool]): Использовать абсолютное время блокировки (опционально).
        """
        if bantime is not None and absolute:
            return await self.coind_implementation.fetch('setban', [ip, action, bantime, absolute])
        elif bantime is not None:
            return await self.coind_implementation.fetch('setban', [ip, action, bantime])
        else:
            return await self.coind_implementation.fetch('setban', [ip, action])

    async def set_traffic_shaping(self, direction: str, burst_kb: str, average_kb: str):
        """Устанавливает ограничение трафика.

        Args:
            direction (str): Направление трафика ("send" или "receive").
            burst_kb (str): Максимальная скорость в КБ/с на пике.
            average_kb (str): Средняя скорость в КБ/с.
        """
        return await self.coind_implementation.fetch('settrafficshaping', [direction, burst_kb, average_kb])

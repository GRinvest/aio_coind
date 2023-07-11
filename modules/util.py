from typing import List, Optional


class Util:

    def __init__(self, coind_implementation):
        self.coind_implementation = coind_implementation

    async def create_multi_sig(self, nrequired: int, keys: List[str]) -> dict:
        """Создает мультиподпись.

        Args:
            nrequired (int): Минимальное количество необходимых подписей.
            keys (List[str]): Список публичных ключей.

        Returns:
            dict: Информация о мультиподписи.
        """
        return await self._fetch('createmultisig', [nrequired, keys])

    async def estimate_fee(self, nblocks: int) -> float:
        """Оценивает комиссию за транзакцию для указанного количества блоков.

        Args:
            nblocks (int): Количество блоков.

        Returns:
            float: Оценочная комиссия за транзакцию.
        """
        return await self._fetch('estimatefee', [nblocks])

    async def estimate_smart_fee(self, nblocks: int) -> dict:
        """Оценивает умную комиссию за транзакцию для указанного количества блоков.

        Args:
            nblocks (int): Количество блоков.

        Returns:
            dict: Информация об оценочной умной комиссии за транзакцию.
        """
        return await self._fetch('estimatesmartfee', [nblocks])

    async def get(self):
        """Возвращает информацию об утилите."""
        return await self._fetch('get')

    async def get_address_forms(self, address: str) -> dict:
        """Возвращает различные формы указанного адреса.

        Args:
            address (str): Адрес.

        Returns:
            dict: Различные формы адреса.
        """
        return await self._fetch('getaddressforms', [address])

    async def get_stat(self):
        """Возвращает статистику утилиты."""
        return await self._fetch('getstat')

    async def get_stat_list(self):
        """Возвращает список статистик утилиты."""
        return await self._fetch('getstatlist')

    async def issue_alert(self, alert: str):
        """Выпускает предупреждение.

        Args:
            alert (str): Предупреждение.
        """
        return await self._fetch('issuealert', [alert])

    async def log(self, category: str, state: str):
        """Включает или отключает журналирование.

        Args:
            category (str): Категория журналирования или "all" для всех категорий.
            state (str): Состояние ("on" или "off").
        """
        return await self._fetch('log', [category, state])

    async def log_line(self, string: str):
        """Записывает строку в журнал.

        Args:
            string (str): Строка для записи в журнал.
        """
        return await self._fetch('logline', [string])

    async def set(self):
        """Устанавливает параметры утилиты."""
        return await self._fetch('set')

    async def validate_address(self, address: str) -> dict:
        """Проверяет валидность указанного адреса.

        Args:
            address (str): Адрес.

        Returns:
            dict: Информация о валидности адреса.
        """
        return await self._fetch('validateaddress', [address])

    async def validate_chain_history(self, hash: Optional[str] = None) -> dict:
        """Проверяет цепочку истории блоков на валидность.

        Args:
            hash (Optional[str]): Хэш блока (опционально).

        Returns:
            dict: Информация о валидности цепочки истории блоков.
        """
        if hash is not None:
            return await self._fetch('validatechainhistory', [hash])
        else:
            return await self._fetch('validatechainhistory')

    async def verify_message(self, address: str, signature: str, message: str) -> bool:
        """Проверяет подпись сообщения.

        Args:
            address (str): Адрес.
            signature (str): Подпись.
            message (str): Сообщение.

        Returns:
            bool: True, если подпись верна, False в противном случае.
        """
        return await self._fetch('verifymessage', [address, signature, message])

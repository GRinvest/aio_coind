from typing import List, Union


class Blockchain:

    def __init__(self, coind_implementation):
        self.coind_implementation = coind_implementation

    async def evict_transaction(self, txid: str):
        """Удаляет транзакцию из памяти пула.

        Args:
            txid (str): Идентификатор транзакции для удаления.
        """
        return await self.coind_implementation.fetch('evicttransaction', [txid])

    async def get_best_block_hash(self) -> str:
        """
        Возвращает хэш самого последнего блока в блокчейне.

        Returns:
            str: Хэш последнего блока.
        """
        return await self.coind_implementation.fetch('getbestblockhash')

    async def get_block(self, hash_or_height: Union[str, int], verbosity: int = 1, tx_count: int = 0):
        """Возвращает информацию о блоке по заданному хэшу или высоте блока.

        Args:
            hash_or_height (Union[str, int]): Хэш или высота блока.
            verbosity (int): Уровень подробности (по умолчанию 1).
            tx_count (int): Количество транзакций для включения (по умолчанию 0).

        Returns:
            dict: Информация о блоке.
        """
        return await self.coind_implementation.fetch('getblock', [hash_or_height, verbosity, tx_count])

    async def get_blockchain_info(self) -> dict:
        """Возвращает информацию о блокчейне.

        Returns:
            dict: Информация о блокчейне.
        """
        return await self.coind_implementation.fetch('getblockchaininfo')

    async def get_block_count(self) -> int:
        """Возвращает количество блоков в блокчейне.

        Returns:
            int: Количество блоков в блокчейне.
        """
        return await self.coind_implementation.fetch('getblockcount')

    async def get_block_hash(self, index: int) -> str:
        """Возвращает хэш блока по заданному индексу.

        Args:
            index (int): Индекс блока.

        Returns:
            str: Хэш блока.
        """
        return await self.coind_implementation.fetch('getblockhash', [index])

    async def get_block_header(self, hash_or_height: Union[str, int], verbose: bool = True):
        """Возвращает заголовок блока по заданному хэшу или высоте блока.

        Args:
            hash_or_height (Union[str, int]): Хэш или высота блока.
            verbose (bool): Включить подробный вывод (по умолчанию True).

        Returns:
            dict: Заголовок блока.
        """
        return await self.coind_implementation.fetch('getblockheader', [hash_or_height, verbose])

    async def get_block_stats(self, hash_or_height: Union[str, int], stats: List[str]):
        """Возвращает статистику блока по заданному хэшу или высоте блока.

        Args:
            hash_or_height (Union[str, int]): Хэш или высота блока.
            stats (List[str]): Список запрашиваемых статистических данных.

        Returns:
            dict: Статистика блока.
        """
        return await self.coind_implementation.fetch('getblockstats', [hash_or_height, stats])

    async def get_chain_tips(self) -> List[dict]:
        """Возвращает список самых длинных цепей блоков.

        Returns:
            List[dict]: Список самых длинных цепей блоков.
        """
        return await self.coind_implementation.fetch('getchaintips')

    async def get_chain_tx_stats(self, nblocks: int = None, blockhash: str = None):
        """Возвращает статистику транзакций для указанного количества блоков или заданного хэша блока.

        Args:
            nblocks (int): Количество блоков для статистики.
            blockhash (str): Хэш блока для статистики.

        Returns:
            dict: Статистика транзакций.
        """
        return await self.coind_implementation.fetch('getchaintxstats', [nblocks, blockhash])

    async def get_difficulty(self) -> float:
        """Возвращает текущую сложность блокчейна.

        Returns:
            float: Текущая сложность блокчейна.
        """
        return await self.coind_implementation.fetch('getdifficulty')

    async def get_orphan_pool_info(self) -> dict:
        """Возвращает информацию о пуле орфанных блоков.

        Returns:
            dict: Информация о пуле орфанных блоков.
        """
        return await self.coind_implementation.fetch('getorphanpoolinfo')

    async def get_raw_orphan_pool(self):
        """Возвращает содержимое пула орфанных блоков в виде сериализованных данных.

        Returns:
            bytes: Сериализованные данные пула орфанных блоков.
        """
        return await self.coind_implementation.fetch('getraworphanpool')

    async def get_raw_tx_pool(self, verbose: bool = False, id: str = None):
        """Возвращает содержимое пула транзакций в виде сериализованных данных.

        Args:
            verbose (bool): Включить подробный вывод (по умолчанию False).
            id (str): Идентификатор транзакции (опционально).

        Returns:
            bytes or dict: Сериализованные данные пула транзакций или информация о конкретной транзакции.
        """
        if id:
            return await self.coind_implementation.fetch('getrawtxpool', [verbose, id])
        else:
            return await self.coind_implementation.fetch('getrawtxpool', [verbose])

    async def get_tx_out(self, txid: str, n: int, includetxpool: bool = True):
        """Возвращает выход транзакции по заданному идентификатору транзакции и номеру выхода.

        Args:
            txid (str): Идентификатор транзакции.
            n (int): Номер выхода.
            includetxpool (bool: Включить выходы из пула транзакций (по умолчанию True).

        Returns:
            dict or None: Информация о выходе транзакции или None, если выход не найден.
        """
        return await self.coind_implementation.fetch('gettxout', [txid, n, includetxpool])

    async def get_tx_out_proof(self, txids: List[str], blockhash: str = None):
        """Возвращает доказательство наличия транзакций в блоке.

        Args:
            txids (List[str]): Список идентификаторов транзакций.
            blockhash (str): Хэш блока (опционально).

        Returns:
            str: Доказательство наличия транзакций в блоке.
        """
        if blockhash:
            return await self.coind_implementation.fetch('gettxoutproof', [txids, blockhash])
        else:
            return await self.coind_implementation.fetch('gettxoutproof', [txids])

    async def get_tx_out_proofs(self, txids: List[str], blockhash: str = None):
        """Возвращает доказательства наличия транзакций в блоке для каждой транзакции.

        Args:
            txids (List[str]): Список идентификаторов транзакций.
            blockhash (str): Хэш блока (опционально).

        Returns:
            List[str]: Список доказательств наличия транзакций в блоке.
        """
        if blockhash:
            return await self.coind_implementation.fetch('gettxoutproofs', [txids, blockhash])
        else:
            return await self.coind_implementation.fetch('gettxoutproofs', [txids])

    async def get_tx_outset_info(self) -> dict:
        """Возвращает информацию о наборе выходов транзакций.

        Returns:
            dict: Информация о наборе выходов транзакций.
        """
        return await self.coind_implementation.fetch('gettxoutsetinfo')

    async def get_tx_pool_ancestors(self, txid: str, verbose: bool = False):
        """Возвращает предковую цепочку транзакции в пуле транзакций.

        Args:
            txid (str): Идентификатор транзакции.
            verbose (bool): Включить подробный вывод (по умолчанию False).

        Returns:
            dict: Предковая цепочка транзакции в пуле транзакций.
        """
        return await self.coind_implementation.fetch('gettxpoolancestors', [txid, verbose])

    async def get_tx_pool_descendants(self, txid: str, verbose: bool = False):
        """Возвращает потомковую цепочку транзакции в пуле транзакций.

        Args:
            txid (str): Идентификатор транзакции.
            verbose (bool): Включить подробный вывод (по умолчанию False).

        Returns:
            dict: Потомковая цепочка транзакции в пуле транзакций.
        """
        return await self.coind_implementation.fetch('gettxpooldescendants', [txid, verbose])

    async def get_tx_pool_entry(self, txid: str) -> dict:
        """Возвращает информацию о транзакции в пуле транзакций.

        Args:
            txid (str): Идентификатор транзакции.

        Returns:
            dict: Информация о транзакции в пуле транзакций.
        """
        return await self.coind_implementation.fetch('gettxpoolentry', [txid])

    async def get_tx_pool_info(self) -> dict:
        """Возвращает информацию о пуле транзакций.

        Returns:
            dict: Информация о пуле транзакций.
        """
        return await self.coind_implementation.fetch('gettxpoolinfo')

    async def save_orphan_pool(self):
        """Сохраняет пул орфанных блоков в файл."""
        return await self.coind_implementation.fetch('saveorphanpool')

    async def save_tx_pool(self):
        """Сохраняет пул транзакций в файл."""
        return await self.coind_implementation.fetch('savetxpool')

    async def scan_tokens(self, action: str, scan_objects: List[str] = None):
        """Сканирует токены в блокчейне.

        Args:
            action (str): Действие сканирования (например, "start" или "stop").
            scan_objects (List[str]): Список объектов для сканирования (опционально).

        Returns:
            str: Результат сканирования.
        """
        if scan_objects:
            return await self.coind_implementation.fetch('scantokens', [action, scan_objects])
        else:
            return await self.coind_implementation.fetch('scantokens', [action])

    async def verify_chain(self, checklevel: int = 3, numblocks: int = 6) -> bool:
        """Проверяет целостность блокчейна.

        Args:
            checklevel (int): Уровень проверки (по умолчанию 3).
            numblocks (int): Количество последних блоков для проверки (по умолчанию 6).

        Returns:
            bool: Результат проверки целостности блокчейна.
        """
        return await self.coind_implementation.fetch('verifychain', [checklevel, numblocks])

    async def verify_tx_out_proof(self, proof: str) -> List[str]:
        """Проверяет доказательство наличия транзакций в блоке.

        Args:
            proof (str): Доказательство наличия транзакций в блоке.

        Returns:
            List[str]: Список идентификаторов транзакций, для которых доказательство верно.
        """
        return await self.coind_implementation.fetch('verifytxoutproof', [proof])

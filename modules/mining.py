from typing import Optional


class Mining:

    def __init__(self, coind_implementation):
        self.coind_implementation = coind_implementation

    async def genesis(self):
        """Генерирует блок генезиса (первый блок в блокчейне)."""
        return await self.coind_implementation.fetch('genesis')

    async def get_block_template(self, jsonrequestobject: Optional[str] = None):
        """Возвращает шаблон блока для майнинга.

        Args:
            jsonrequestobject (Optional[str]): Объект JSON с параметрами запроса (опционально).

        Returns:
            dict: Шаблон блока для майнинга.
        """
        if jsonrequestobject is not None:
            return await self.coind_implementation.fetch('getblocktemplate', [jsonrequestobject])
        else:
            return await self.coind_implementation.fetch('getblocktemplate')

    async def get_block_version(self) -> int:
        """Возвращает текущую версию блока."""
        return await self.coind_implementation.fetch('getblockversion')

    async def get_miner_comment(self) -> str:
        """Возвращает комментарий майнера, если он задан."""
        return await self.coind_implementation.fetch('getminercomment')

    async def get_mining_candidate(self):
        """Возвращает данные о текущем кандидате для майнинга."""
        return await self.coind_implementation.fetch('getminingcandidate')

    async def get_mining_info(self):
        """Возвращает информацию о текущем состоянии майнинга."""
        return await self.coind_implementation.fetch('getmininginfo')

    async def get_mining_max_block(self) -> int:
        """Возвращает максимальный размер блока для майнинга."""
        return await self.coind_implementation.fetch('getminingmaxblock')

    async def get_network_hashrate(self, blocks: Optional[int] = None, height: Optional[int] = None) -> int:
        """Возвращает скорость хеширования сети.

        Args:
            blocks (Optional[int]): Количество блоков для усреднения (опционально).
            height (Optional[int]): Высота блока для расчета скорости хеширования (опционально).

        Returns:
            int: Скорость хеширования сети в хешах в секунду.
        """
        if blocks is not None and height is not None:
            return await self.coind_implementation.fetch('getnetworkhashps', [blocks, height])
        elif blocks is not None:
            return await self.coind_implementation.fetch('getnetworkhashps', [blocks])
        elif height is not None:
            return await self.coind_implementation.fetch('getnetworkhashps', [None, height])
        else:
            return await self.coind_implementation.fetch('getnetworkhashps')

    async def prioritise_transaction(self, txid: str, priority_delta: float, fee_delta: float):
        """Устанавливает приоритет и комиссию для указанной транзакции.

        Args:
            txid (str): Идентификатор транзакции.
            priority_delta (float): Изменение приоритета.
            fee_delta (float): Изменение комиссии.
        """
        return await self.coind_implementation.fetch('prioritisetransaction', [txid, priority_delta, fee_delta])

    async def set_block_version(self, block_version_number: int):
        """Устанавливает версию блока для майнинга.

        Args:
            block_version_number (int): Номер версии блока.
        """
        return await self.coind_implementation.fetch('setblockversion', [block_version_number])

    async def set_miner_comment(self, comment: str):
        """Устанавливает комментарий для майнера.

        Args:
            comment (str): Комментарий майнера.
        """
        return await self.coind_implementation.fetch('setminercomment', [comment])

    async def set_mining_max_block(self, block_size: int):
        """Устанавливает максимальный размер блока для майнинга.

        Args:
            block_size (int): Размер блока в байтах.
        """
        return await self.coind_implementation.fetch('setminingmaxblock', [block_size])

    async def submit_block(self, hex_data: str, json_parameters_object: Optional[str] = None):
        """Отправляет сгенерированный блок для добавления в блокчейн.

        Args:
            hex_data (str): Данные блока в шестнадцатеричном формате.
            json_parameters_object (Optional[str]): Объект JSON с параметрами запроса (опционально).
        """
        if json_parameters_object is not None:
            return await self.coind_implementation.fetch('submitblock', [hex_data, json_parameters_object])
        else:
            return await self.coind_implementation.fetch('submitblock', [hex_data])

    async def submit_mining_solution(self, mining_candidate_data: str, json_parameters_object: Optional[str] = None):
        """Отправляет решение майнинга для проверки и добавления в блокчейн.

        Args:
            mining_candidate_data (str): Данные кандидата для майнинга.
            json_parameters_object (Optional[str]): Объект JSON с параметрами запроса (опционально).
        """
        if json_parameters_object is not None:
            return await self.coind_implementation.fetch('submitminingsolution', [mining_candidate_data, json_parameters_object])
        else:
            return await self.coind_implementation.fetch('submitminingsolution', [mining_candidate_data])

    async def validate_block_template(self, hex_data: str):
        """Проверяет шаблон блока на его валидность.

        Args:
            hex_data (str): Данные блока в шестнадцатеричном формате.
        """
        return await self.coind_implementation.fetch('validateblocktemplate', [hex_data])

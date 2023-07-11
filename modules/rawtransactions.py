from typing import Optional, List, Union, Dict


class RawTransactions:

    def __init__(self, coind_implementation):
        self.coind_implementation = coind_implementation

    async def create_raw_transaction(
        self,
        inputs: List[Dict[str, Union[str, int]]],
        outputs: Dict[str, Union[str, int]],
        locktime: Optional[int] = None
    ) -> str:
        """Создает неподписанную транзакцию.

        Args:
            inputs (List[Dict[str, Union[str, int]]]): Список входов.
            outputs (Dict[str, Union[str, int]]): Выходы.
            locktime (Optional[int]): Время блокировки (опционально).

        Returns:
            str: Неподписанная транзакция в шестнадцатеричном формате.
        """
        if locktime is not None:
            return await self.coind_implementation.fetch('createrawtransaction', [inputs, outputs, locktime])
        else:
            return await self.coind_implementation.fetch('createrawtransaction', [inputs, outputs])

    async def decode_raw_transaction(self, hex_string: str) -> dict:
        """Декодирует неподписанную или подписанную транзакцию.

        Args:
            hex_string (str): Транзакция в шестнадцатеричном формате.

        Returns:
            dict: Информация о декодированной транзакции.
        """
        return await self.coind_implementation.fetch('decoderawtransaction', [hex_string])

    async def decode_script(self, hex_script: str) -> dict:
        """Декодирует шестнадцатеричный скрипт.

        Args:
            hex_script (str): Скрипт в шестнадцатеричном формате.

        Returns:
            dict: Информация о декодированном скрипте.
        """
        return await self.coind_implementation.fetch('decodescript', [hex_script])

    async def enqueue_raw_transaction(self, hex_string: str, options: Optional[str] = None) -> None:
        """Помещает транзакцию в очередь на отправку.

        Args:
            hex_string (str): Транзакция в шестнадцатеричном формате.
            options (Optional[str]): Дополнительные опции (опционально).
        """
        if options is not None:
            return await self.coind_implementation.fetch('enqueuerawtransaction', [hex_string, options])
        else:
            return await self.coind_implementation.fetch('enqueuerawtransaction', [hex_string])

    async def fund_raw_transaction(self, hex_string: str, include_watching: bool) -> dict:
        """Финансирует неподписанную транзакцию.

        Args:
            hex_string (str): Транзакция в шестнадцатеричном формате.
            include_watching (bool): Включить наблюдаемые адреса.

        Returns:
            dict: Информация о финансированной транзакции.
        """
        return await self.coind_implementation.fetch('fundrawtransaction', [hex_string, include_watching])

    async def get_raw_block_transactions(self) -> List[str]:
        """Возвращает список транзакций в сыром блоке.

        Returns:
            List[str]: Список транзакций в шестнадцатеричном формате.
        """
        return await self.coind_implementation.fetch('getrawblocktransactions')

    async def get_raw_transaction(
        self,
        tx_id: str,
        verbose: Optional[bool] = False,
        block_hash: Optional[str] = None
    ) -> Union[dict, str]:
        """Возвращает информацию о сырой транзакции.

        Args:
            tx_id (str): Идентификатор транзакции.
            verbose (Optional[bool]): Включить подробную информацию (опционально).
            block_hash (Optional[str]): Хэш блока (опционально).

        Returns:
            Union[dict, str]: Информация о транзакции в виде словаря или шестнадцатеричная транзакция.
        """
        if verbose and block_hash is not None:
            return await self.coind_implementation.fetch('getrawtransaction', [tx_id, True, block_hash])
        elif verbose:
            return await self.coind_implementation.fetch('getrawtransaction', [tx_id, True])
        else:
            return await self.coind_implementation.fetch('getrawtransaction', [tx_id])

    async def get_raw_transactions_since(self) -> dict:
        """Возвращает список сырых транзакций с указанного момента.

        Returns:
            dict: Список сырых транзакций.
        """
        return await self.coind_implementation.fetch('getrawtransactionssince')

    async def send_raw_transaction(
        self,
        hex_string: str,
        allow_high_fees: Optional[bool] = False,
        allow_non_standard: Optional[bool] = False,
        verbose: Optional[bool] = False
    ) -> Union[str, dict]:
        """Отправляет сырую транзакцию в сеть.

        Args:
            hex_string (str): Транзакция в шестнадцатеричном формате.
            allow_high_fees (Optional[bool]): Разрешить высокие комиссии (опционально).
            allow_non_standard (Optional[bool]): Разрешить нестандартные транзакции (опционально).
            verbose (Optional[bool]): Включить подробную информацию (опционально).

        Returns:
            Union[str, dict]: Шестнадцатеричная транзакция или информация о транзакции.
        """
        params = [hex_string]
        if allow_high_fees:
            params.append(True)
        if allow_non_standard:
            params.append(True)
        if verbose:
            return await self.coind_implementation.fetch('sendrawtransaction', params, verbose)
        else:
            return await self.coind_implementation.fetch('sendrawtransaction', params)

    async def sign_raw_transaction(
        self,
        hex_string: str,
        prev_outputs: List[Dict[str, Union[str, int]]],
        private_keys: List[str],
        sighash_type: Optional[str] = 'ALL',
        sig_type: Optional[str] = 'ALL'
    ) -> dict:
        """Подписывает сырую транзакцию.

        Args:
            hex_string (str): Транзакция в шестнадцатеричном формате.
            prev_outputs (List[Dict[str, Union[str, int]]]): Предыдущие выходы.
            private_keys (List[str]): Приватные ключи.
            sighash_type (Optional[str]): Тип хеша для подписи (опционально).
            sig_type (Optional[str]): Тип подписи (опционально).

        Returns:
            dict: Информация о подписанной транзакции.
        """
        return await self.coind_implementation.fetch(
            'signrawtransaction',
            [hex_string, prev_outputs, private_keys, sighash_type, sig_type]
        )

    async def validate_raw_transaction(
        self,
        hex_string: str,
        allow_high_fees: Optional[bool] = False,
        allow_non_standard: Optional[bool] = False
    ) -> dict:
        """Проверяет сырую транзакцию на валидность.

        Args:
            hex_string (str): Транзакция в шестнадцатеричном формате.
            allow_high_fees (Optional[bool]): Разрешить высокие комиссии (опционально).
            allow_non_standard (Optional[bool]): Разрешить нестандартные транзакции (опционально).

        Returns:
            dict: Информация о валидности транзакции.
        """
        params = [hex_string]
        if allow_high_fees:
            params.append(True)
        if allow_non_standard:
            params.append(True)
        return await self.coind_implementation.fetch('validaterawtransaction', params)

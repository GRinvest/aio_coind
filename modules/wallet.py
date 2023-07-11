from typing import Optional, List, Dict, Union


class Wallet:

    def __init__(self, coind_implementation):
        self.coind_implementation = coind_implementation

    async def abandon_transaction(self, txid: str) -> None:
        """Отменяет транзакцию.

        Args:
            txid (str): Идентификатор транзакции.
        """
        return await self.coind_implementation.fetch('abandontransaction', [txid])

    async def add_multisig_address(
            self,
            nrequired: int,
            keys: List[str],
            account: Optional[str] = ""
    ) -> str:
        """Добавляет мультиподписной адрес.

        Args:
            nrequired (int): Минимальное количество необходимых подписей.
            keys (List[str]): Список публичных ключей.
            account (Optional[str]): Имя аккаунта (опционально).

        Returns:
            str: Добавленный мультиподписной адрес.
        """
        return await self.coind_implementation.fetch('addmultisigaddress', [nrequired, keys, account])

    async def backup_wallet(self, destination: str) -> None:
        """Создает резервную копию кошелька.

        Args:
            destination (str): Путь для сохранения резервной копии.
        """
        return await self.coind_implementation.fetch('backupwallet', [destination])

    async def dump_private_key(self, nexa_address: str) -> str:
        """Возвращает приватный ключ для указанного адреса.

        Args:
            nexa_address (str): Адрес Nexa.

        Returns:
            str: Приватный ключ.
        """
        return await self.coind_implementation.fetch('dumpprivkey', [nexa_address])

    async def dump_wallet(self, filename: str) -> None:
        """Создает дамп кошелька в файл.

        Args:
            filename (str): Имя файла для дампа кошелька.
        """
        return await self.coind_implementation.fetch('dumpwallet', [filename])

    async def encrypt_wallet(self, passphrase: str) -> None:
        """Шифрует кошелек с помощью пароля.

        Args:
            passphrase (str): Пароль для шифрования.
        """
        return await self.coind_implementation.fetch('encryptwallet', [passphrase])

    async def get_account(self, address: str) -> str:
        """Возвращает имя аккаунта, связанного с указанным адресом.

        Args:
            address (str): Адрес.

        Returns:
            str: Имя аккаунта.
        """
        return await self.coind_implementation.fetch('getaccount', [address])

    async def get_account_address(self, account: str) -> str:
        """Возвращает адрес, связанный с указанным аккаунтом.

        Args:
            account (str): Имя аккаунта.

        Returns:
            str: Адрес.
        """
        return await self.coind_implementation.fetch('getaccountaddress', [account])

    async def get_addresses_by_account(self, account: str) -> List[str]:
        """Возвращает список адресов, связанных с указанным аккаунтом.

        Args:
            account (str): Имя аккаунта.

        Returns:
            List[str]: Список адресов.
        """
        return await self.coind_implementation.fetch('getaddressesbyaccount', [account])

    async def get_balance(
            self,
            account: Optional[str] = "*",
            min_conf: Optional[int] = 1,
            include_watch_only: Optional[bool] = False
    ) -> float:
        """Возвращает баланс кошелька.

        Args:
            account (Optional[str]): Имя аккаунта (опционально).
            min_conf (Optional[int]): Минимальное количество подтверждений (опционально).
            include_watch_only (Optional[bool]): Включить наблюдаемые адреса (опционально).

        Returns:
            float: Баланс кошелька.
        """
        params = []
        if account is not None:
            params.append(account)
        params.append(min_conf)
        params.append(include_watch_only)
        return await self.coind_implementation.fetch('getbalance', params)

    async def get_new_address(
            self,
            address_type: Optional[str] = "legacy",
            account: Optional[str] = ""
    ) -> str:
        """Генерирует новый адрес для указанного типа.

        Args:
            address_type (Optional[str]): Тип адреса ("legacy", "p2sh-segwit" или "bech32") (опционально).
            account (Optional[str]): Имя аккаунта (опционально).

        Returns:
            str: Новый адрес.
        """
        params = []
        if address_type is not None:
            params.append(address_type)
        params.append(account)
        return await self.coind_implementation.fetch('getnewaddress', params)

    async def get_raw_change_address(self) -> str:
        """Возвращает сырой адрес для сдачи.

        Returns:
            str: Сырой адрес для сдачи.
        """
        return await self.coind_implementation.fetch('getrawchangeaddress')

    async def get_received_by_account(self, account: str, min_conf: Optional[int] = 1) -> float:
        """Возвращает сумму, полученную на указанный аккаунт.

        Args:
            account (str): Имя аккаунта.
            min_conf (Optional[int]): Минимальное количество подтверждений (опционально).

        Returns:
            float: Сумма, полученная на аккаунт.
        """

        return await self.coind_implementation.fetch('getreceivedbyaccount', [account, min_conf])

    async def get_received_by_address(self, address: str, min_conf: Optional[int] = 1) -> float:
        """Возвращает сумму, полученную на указанный адрес.

        Args:
            address (str): Адрес.
            min_conf (Optional[int]): Минимальное количество подтверждений (опционально).

        Returns:
            float: Сумма, полученная на адрес.
        """
        return await self.coind_implementation.fetch('getreceivedbyaddress', [address, min_conf])

    async def get_transaction(
            self,
            txid: str,
            include_watch_only: Optional[bool] = False
    ) -> Optional[dict]:
        """Возвращает информацию о транзакции.

        Args:
            txid (str): Идентификатор транзакции.
            include_watch_only (Optional[bool]): Включить наблюдаемые адреса (опционально).

        Returns:
            Optional[dict]: Информация о транзакции.
        """
        return await self.coind_implementation.fetch('gettransaction', [txid, include_watch_only])

    async def get_unconfirmed_balance(self) -> float:
        """Возвращает неподтвержденный баланс кошелька.

        Returns:
            float: Неподтвержденный баланс кошелька.
        """
        return await self.coind_implementation.fetch('getunconfirmedbalance')

    async def get_wallet_info(self) -> dict:
        """Возвращает информацию о кошельке.

        Returns:
            dict: Информация о кошельке.
        """
        return await self.coind_implementation.fetch('getwalletinfo')

    async def import_address(
            self,
            address: str,
            label: Optional[str] = "",
            rescan: Optional[bool] = True,
            p2sh: Optional[bool] = False
    ) -> None:
        """Импортирует адрес в кошелек.

        Args:
            address (str): Адрес.
            label (Optional[str]): Метка (опционально).
            rescan (Optional[bool]): Пересканировать блокчейн (опционально).
            p2sh (Optional[bool]): Адрес в формате P2SH (опционально).
        """
        params = [address]
        if label is not None:
            params.append(label)
        params.append(rescan)
        params.append(p2sh)
        return await self.coind_implementation.fetch('importaddress', params)

    async def import_addresses(
            self,
            rescan: str,
            addresses: List[str]
    ) -> None:
        """Импортирует адреса в кошелек.

        Args:
            rescan (str): Опция для пересканирования блокчейна ("rescan" или "no-rescan").
            addresses (List[str]): Список адресов.
        """
        return await self.coind_implementation.fetch('importaddresses', [rescan] + addresses)

    async def import_private_keys(
            self,
            rescan: str,
            private_keys: List[str]
    ) -> None:
        """Импортирует приватные ключи в кошелек.

        Args:
            rescan (str): Опция для пересканирования блокчейна ("rescan" или "no-rescan").
            private_keys (List[str]): Список приватных ключей.
        """
        return await self.coind_implementation.fetch('importprivatekeys', [rescan] + private_keys)

    async def import_priv_key(
            self,
            nexa_priv_key: str,
            label: Optional[str] = "",
            rescan: Optional[bool] = True
    ) -> None:
        """Импортирует приватный ключ в кошелек.

        Args:
            nexa_priv_key (str): Приватный ключ Nexa.
            label (Optional[str]): Метка (опционально).
            rescan (Optional[bool]): Пересканировать блокчейн (опционально).
        """
        params = [nexa_priv_key]
        if label is not None:
            params.append(label)
        params.append(rescan)
        return await self.coind_implementation.fetch('importprivkey', params)

    async def import_pruned_funds(self) -> None:
        """Импортирует урезанные средства в кошелек."""
        return await self.coind_implementation.fetch('importprunedfunds')

    async def import_pubkey(
            self,
            pubkey: str,
            label: Optional[str] = "",
            rescan: Optional[bool] = True
    ) -> None:
        """Импортирует публичный ключ в кошелек.

        Args:
            pubkey (str): Публичный ключ.
            label (Optional[str]): Метка (опционально).
            rescan (Optional[bool]): Пересканировать блокчейн (опционально).
        """
        params = [pubkey]
        if label is not None:
            params.append(label)
        params.append(rescan)
        return await self.coind_implementation.fetch('importpubkey', params)

    async def import_wallet(self, filename: str) -> None:
        """Импортирует кошелек из файла.

        Args:
            filename (str): Имя файла с кошельком.
        """
        return await self.coind_implementation.fetch('importwallet', [filename])

    async def keypool_refill(self, newsize: Optional[int] = 100) -> None:
        """Пополняет пул ключей.

        Args:
            newsize (Optional[int]): Новый размер пула ключей (опционально).
        """
        return await self.coind_implementation.fetch('keypoolrefill', [newsize])

    async def list_accounts(
            self,
            min_conf: Optional[int] = 1,
            include_watch_only: Optional[bool] = False
    ) -> Dict[str, float]:
        """Возвращает список аккаунтов и их балансы.

        Args:
            min_conf (Optional[int]): Минимальное количество подтверждений (опционально).
            include_watch_only (Optional[bool]): Включить наблюдаемые адреса (опционально).

        Returns:
            Dict[str, float]: Словарь с аккаунтами и их балансами.
        """

        return await self.coind_implementation.fetch('listaccounts', [min_conf, include_watch_only])

    async def list_active_addresses(self) -> List[str]:
        """Возвращает список активных адресов кошелька.

        Returns:
            List[str]: Список активных адресов.
        """
        return await self.coind_implementation.fetch('listactiveaddresses')

    async def list_address_groupings(self) -> List[List[List[str]]]:
        """Возвращает группировку адресов кошелька.

        Returns:
            List[List[List[str]]]: Группировка адресов.
        """
        return await self.coind_implementation.fetch('listaddressgroupings')

    async def list_lock_unspent(self) -> List[Dict[str, Union[str, int]]]:
        """Возвращает список непотраченных выходов, помеченных как заблокированные.

        Returns:
            List[Dict[str, Union[str, int]]]: Список заблокированных непотраченных выходов.
        """
        return await self.coind_implementation.fetch('listlockunspent')

    async def list_received_by_account(
            self,
            min_conf: Optional[int] = 1,
            include_empty: Optional[bool] = False,
            include_watch_only: Optional[bool] = False
    ) -> List[Dict[str, Union[str, float]]]:
        """Возвращает список полученных средств по аккаунтам.

        Args:
            min_conf (Optional[int]): Минимальное количество подтверждений (опционально).
            include_empty (Optional[bool]): Включить пустые аккаунты (опционально).
            include_watch_only (Optional[bool]): Включить наблюдаемые адреса (опционально).

        Returns:
            List[Dict[str, Union[str, float]]]: Список полученных средств по аккаунтам.
        """
        params = [min_conf, include_empty, include_watch_only]
        return await self.coind_implementation.fetch('listreceivedbyaccount', params)

    async def list_received_by_address(
            self,
            min_conf: Optional[int] = 1,
            include_empty: Optional[bool] = False,
            include_watch_only: Optional[bool] = False
    ) -> List[Dict[str, Union[str, float]]]:
        """Возвращает список полученных средств по адресам.

        Args:
            min_conf (Optional[int]): Минимальное количество подтверждений (опционально).
            include_empty (Optional[bool]): Включить пустые адреса (опционально).
            include_watch_only (Optional[bool]): Включить наблюдаемые адреса (опционально).

        Returns:
            List[Dict[str, Union[str, float]]]: Список полученных средств по адресам.
        """
        params = [min_conf, include_empty, include_watch_only]
        return await self.coind_implementation.fetch('listreceivedbyaddress', params)

    async def list_since_block(
            self,
            blockhash: Optional[str] = "",
            target_confirmations: Optional[int] = 1,
            include_watch_only: Optional[bool] = False
    ) -> Dict[str, Union[str, List[Dict[str, Union[str, int, float]]]]]:
        """Возвращает список транзакций, произошедших с указанного блока.

        Args:
            blockhash (Optional[str]): Хэш блока (опционально).
            target_confirmations (Optional[int]): Целевое количество подтверждений (опционально).
            include_watch_only (Optional[bool]): Включить наблюдаемые адреса (опционально).

        Returns:
            Dict[str, Union[str, List[Dict[str, Union[str, int, float]]]]]: Информация о транзакциях.
        """
        params = [blockhash, target_confirmations, include_watch_only]
        return await self.coind_implementation.fetch('listsinceblock', params)

    async def list_transactions(
            self,
            account: Optional[str] = "*",
            count: Optional[int] = 10,
            from_: Optional[int] = 0,
            include_watch_only: Optional[bool] = False
    ) -> List[Dict[str, Union[str, float]]]:
        """Возвращает список транзакций для указанного аккаунта.

        Args:
            account (Optional[str]): Имя аккаунта (опционально).
            count (Optional[int]): Количество возвращаемых транзакций (опционально).
            from_ (Optional[int]): Индекс начала списка транзакций (опционально).
            include_watch_only (Optional[bool]): Включить наблюдаемые адреса (опционально).

        Returns:
            List[Dict[str, Union[str, float]]]: Список транзакций.
        """
        params = [account, count, from_, include_watch_only]
        return await self.coind_implementation.fetch('listtransactions', params)

    async def list_transactions_from(
            self,
            account: Optional[str] = "*",
            count: Optional[int] = 10,
            from_: Optional[int] = 0,
            include_watch_only: Optional[bool] = False
    ) -> List[Dict[str, Union[str, float]]]:
        """Возвращает список транзакций для указанного аккаунта, начиная с указанного индекса.

        Args:
            account (Optional[str]): Имя аккаунта (опционально).
            count (Optional[int]): Количество возвращаемых транзакций (опционально).
            from_ (Optional[int]): Индекс начала списка транзакций (опционально).
            include_watch_only (Optional[bool]): Включить наблюдаемые адреса (опционально).

        Returns:
            List[Dict[str, Union[str, float]]]: Список транзакций.
        """
        params = [account, count, from_, include_watch_only]
        return await self.coind_implementation.fetch('listtransactionsfrom', params)

    async def list_unspent(
            self,
            min_conf: Optional[int] = 1,
            max_conf: Optional[int] = 9999999,
            addresses: Optional[List[str]] = None
    ) -> List[Dict[str, Union[str, int, float]]]:
        """Возвращает список непотраченных выходов.

        Args:
            min_conf (Optional[int]): Минимальное количество подтверждений (опционально).
            max_conf (Optional[int]): Максимальное количество подтверждений (опционально).
            addresses (Optional[List[str]]): Список адресов (опционально).

        Returns:
            List[Dict[str, Union[str, int, float]]]: Список непотраченных выходов.
        """
        params = [min_conf, max_conf]
        if addresses is not None:
            params.append(addresses)
        return await self.coind_implementation.fetch('listunspent', params)

    async def lock_unspent(
            self,
            unlock: bool,
            outputs: List[Dict[str, Union[str, int]]]
    ) -> bool:
        """Блокирует или разблокирует указанные непотраченные выходы.

        Args:
            unlock (bool): Флаг разблокировки.
            outputs (List[Dict[str, Union[str, int]]]): Список выходов.

        Returns:
            bool: Результат операции (успех или ошибка).
        """
        params = [unlock, outputs]
        return await self.coind_implementation.fetch('lockunspent', params)

    async def move(
            self,
            from_account: str,
            to_account: str,
            amount: float,
            min_conf: Optional[int] = 1,
            comment: Optional[str] = ""
    ) -> bool:
        """Перемещает средства между аккаунтами.

        Args:
            from_account (str): Имя аккаунта отправителя.
            to_account (str): Имя аккаунта получателя.
            amount (float): Сумма для перемещения.
            min_conf (Optional[int]): Минимальное количество подтверждений (опционально).
            comment (Optional[str]): Комментарий (опционально).

        Returns:
            bool: Результат операции (успех или ошибка).
        """
        params = [from_account, to_account, amount, min_conf, comment]
        return await self.coind_implementation.fetch('move', params)

    async def remove_pruned_funds(self, txid: str) -> None:
        """Удаляет урезанные средства по указанному идентификатору транзакции.

        Args:
            txid (str): Идентификатор транзакции.
        """
        return await self.coind_implementation.fetch('removeprunedfunds', [txid])

    async def send_from(
            self,
            from_account: str,
            to_address: str,
            amount: float,
            min_conf: Optional[int] = 1,
            comment: Optional[str] = "",
            comment_to: Optional[str] = ""
    ) -> str:
        """Отправляет средства с указанного аккаунта на указанный адрес.

        Args:
            from_account (str): Имя аккаунта отправителя.
            to_address (str): Адрес получателя.
            amount (float): Сумма для отправки.
            min_conf (Optional[int]): Минимальное количество подтверждений (опционально).
            comment (Optional[str]): Комментарий (опционально).
            comment_to (Optional[str]): Комментарий для получателя (опционально).

        Returns:
            str: Идентификатор транзакции.
        """
        params = [from_account, to_address, amount, min_conf, comment, comment_to]
        return await self.coind_implementation.fetch('sendfrom', params)

    async def send_many(
            self,
            from_account: str,
            to_addresses: Dict[str, float],
            min_conf: Optional[int] = 1,
            comment: Optional[str] = "",
            subtract_fee_from_amount: Optional[List[str]] = None
    ) -> str:
        """Отправляет средства с указанного аккаунта на несколько адресов.

        Args:
            from_account (str): Имя аккаунта отправителя.
            to_addresses (Dict[str, float]): Словарь адресов и сумм для отправки.
            min_conf (Optional[int]): Минимальное количество подтверждений (опционально).
            comment (Optional[str]): Комментарий (опционально).
            subtract_fee_from_amount (Optional[List[str]]): Список адресов, с которых вычесть комиссию (опционально).

        Returns:
            str: Идентификатор транзакции.
        """
        params = [from_account, to_addresses, min_conf, comment, subtract_fee_from_amount]
        return await self.coind_implementation.fetch('sendmany', params)

    async def send_to_address(
            self,
            address: str,
            amount: float,
            comment: Optional[str] = "",
            comment_to: Optional[str] = "",
            subtract_fee_from_amount: Optional[bool] = False
    ) -> str:
        """Отправляет средства на указанный адрес.

        Args:
            address (str): Адрес получателя.
            amount (float): Сумма для отправки.
            comment (Optional[str]): Комментарий (опционально).
            comment_to (Optional[str]): Комментарий для получателя (опционально).
            subtract_fee_from_amount (Optional[bool]): Вычесть комиссию из суммы (опционально).

        Returns:
            str: Идентификатор транзакции.
        """
        params = [address, amount, comment, comment_to, subtract_fee_from_amount]
        return await self.coind_implementation.fetch('sendtoaddress', params)

    async def set_account(self, address: str, account: str) -> None:
        """Устанавливает имя аккаунта для указанного адреса.

        Args:
            address (str): Адрес.
            account (str): Имя аккаунта.
        """
        return await self.coind_implementation.fetch('setaccount', [address, account])

    async def sign_data(self, address: str, msg_format: str, message: str) -> str:
        """Подписывает данные с помощью указанных адреса.

        Args:
            address (str): Адрес.
            msg_format (str): Формат сообщения.
            message (str): Сообщение.

        Returns:
            str: Подпись.
        """
        return await self.coind_implementation.fetch('signdata', [address, msg_format, message])

    async def sign_message(self, address: str, message: str) -> str:
        """Подписывает сообщение с помощью указанного адреса.

        Args:
            address (str): Адрес.
            message (str): Сообщение.

        Returns:
            str: Подпись.
        """
        return await self.coind_implementation.fetch('signmessage', [address, message])

    async def token_info(self) -> None:
        """Выводит информацию о токене."""
        return await self.coind_implementation.fetch('token', ['info'])

    async def token_new(self) -> None:
        """Создает новый токен."""
        return await self.coind_implementation.fetch('token', ['new'])

    async def token_mint(self) -> None:
        """Минтит токены."""
        return await self.coind_implementation.fetch('token', ['mint'])

    async def token_melt(self) -> None:
        """Мельтит токены."""
        return await self.coind_implementation.fetch('token', ['melt'])

    async def token_send(self) -> None:
        """Отправляет токены."""
        return await self.coind_implementation.fetch('token', ['send'])

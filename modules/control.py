class Control:

    def __init__(self, coind_implementation):
        self.coind_implementation = coind_implementation

    async def get_info(self) -> dict:
        """Возвращает информацию о состоянии узла.

        Returns:
            dict: Информация о состоянии узла.
        """
        return await self.coind_implementation.fetch('getinfo')

    async def help(self, command: str = None) -> dict:
        """Возвращает справочную информацию о команде или список доступных команд.

        Args:
            command (str): Команда, для которой требуется справочная информация (опционально).

        Returns:
            dict: Справочная информация о команде или список доступных команд.
        """
        tmp_command = command.replace('_', '') if command else None
        if tmp_command:
            return await self.coind_implementation.fetch('help', [tmp_command])
        else:
            return await self.coind_implementation.fetch('help')

    async def stop(self) -> None:
        """Останавливает работу узла."""
        await self._fetch('stop')

    async def uptime(self) -> int:
        """Возвращает время работы узла в секундах.

        Returns:
            int: Время работы узла в секундах.
        """
        return await self.coind_implementation.fetch('uptime')

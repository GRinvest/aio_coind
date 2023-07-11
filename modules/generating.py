from typing import Optional


class Generating:

    def __init__(self, coind_implementation):
        self.coind_implementation = coind_implementation

    async def generate(self, numblocks: int, maxtries: Optional[int] = None):
        """Генерирует указанное количество блоков.

        Args:
            numblocks (int): Количество блоков для генерации.
            maxtries (Optional[int]): Максимальное количество попыток генерации блока (опционально).

        Returns:
            List[str]: Список хэшей сгенерированных блоков.
        """
        if maxtries is not None:
            return await self.coind_implementation.fetch('generate', [numblocks, maxtries])
        else:
            return await self.coind_implementation.fetch('generate', [numblocks])

    async def generate_to_address(self, numblocks: int, address: str, maxtries: Optional[int] = None):
        """Генерирует указанное количество блоков и отправляет вознаграждение на указанный адрес.

        Args:
            numblocks (int): Количество блоков для генерации.
            address (str): Адрес, на который будет отправлено вознаграждение.
            maxtries (Optional[int]): Максимальное количество попыток генерации блока (опционально).

        Returns:
            List[str]: Список хэшей сгенерированных блоков.
        """
        if maxtries is not None:
            return await self.coind_implementation.fetch('generatetoaddress', [numblocks, address, maxtries])
        else:
            return await self.coind_implementation.fetch('generatetoaddress', [numblocks, address])

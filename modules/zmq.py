
class Zmq:

    def __init__(self, coind_implementation):
        self.coind_implementation = coind_implementation

    async def get_zmq_notifications(self) -> dict:
        """Возвращает текущую конфигурацию ZMQ-уведомлений.

        Returns:
            dict: Конфигурация ZMQ-уведомлений.
        """
        return await self.coind_implementation.fetch('getzmqnotifications')

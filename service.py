from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def _needs_service(self):
        pass
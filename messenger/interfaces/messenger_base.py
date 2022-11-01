from abc import ABC, abstractmethod


class MessengerBase(ABC):
    @abstractmethod
    def send_everything(self) -> None:
        pass

    @abstractmethod
    def _attach_log_file(self) -> None:
        pass
    @abstractmethod
    def _attach_recording(self) -> None:
        pass

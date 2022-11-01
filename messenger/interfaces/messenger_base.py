from abc import ABC, abstractmethod


class MessengerBase(ABC):
    @abstractmethod
    def send_logs(self):
        pass

    @abstractmethod
    def send_recording(self):
        pass

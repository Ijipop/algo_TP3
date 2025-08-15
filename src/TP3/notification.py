from abc import ABC, abstractmethod

class INotification(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

class notificaton_email(INotification):
    def send_notification(self, message):
        print(f"EMAIL: {message}")

class notificaton_sms(INotification):
    def send_notification(self, message):
        print(f"SMS: {message}")

class notificaton_push(INotification):
    def send_notification(self, message):
        print(f"PUSH: {message}")
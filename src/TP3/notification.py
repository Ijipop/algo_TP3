from abc import ABC, abstractmethod

class INotification(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

class NotificationEmail(INotification):
    def send_notification(self, message):
        print(f"EMAIL: {message}")

class NotificationSms(INotification):
    def send_notification(self, message):
        print(f"SMS: {message}")

class NotificationPush(INotification):
    def send_notification(self, message):
        print(f"PUSH: {message}")

class NotificationBoat(INotification):  #For joke and testing
    def send_notification(self, message):
        print(f"BROOOOOOOOOOOOO: {message}")

# class Notification(INotification):
#     def __init__(self, nom: str):
#         self.nom = nom

#     def send_notification(self, message):
#         print(f"{self.nom.upper()}: {message}")
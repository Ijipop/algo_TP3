# from TP3.notification import Notification

# class NotificationManager:
#     def __init__(self):
#         self.notifications = []
    
#     def subscribe(self, notification: Notification):
#         self.notifications.append(notification)
    
#     def unsubscribe(self, notification: Notification):
#         self.notifications.remove(notification)
    
#     def notify(self, message: str):
#         for notification in self.notifications:
#             notification.send_notification(message)

from TP3.notification import INotification

class NotificationManager:
    def __init__(self):
        self.notifications = []
    
    def subscribe(self, notification: INotification):
        self.notifications.append(notification)
    
    def unsubscribe(self, notification: INotification):
        self.notifications.remove(notification)
    
    def notify(self, message: str):
        for notification in self.notifications:
            notification.send_notification(message)
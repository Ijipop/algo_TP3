from TP3.notification_manager import NotificationManager
from TP3.user import *

class UserManager:
    def __init__(self, notification_manager: NotificationManager):
        self.notification_manager = notification_manager
        self.users: list[User] = []
    
    def add_user(self, user: User):
        self.users.append(user)
        self.notification_manager.notify(f"Nouvel utilisateur ajouté - ID {user.getId()}: {user.getName()}")
        return user
    
    def remove_user(self, user_id: int):
        for i, user in enumerate(self.users):
            if user.getId() == user_id:
                
                del self.users[i]
                
                self.notification_manager.notify(f"Utilisateur supprimé - ID {user_id}: {user.getName()}")
                return True
        return False

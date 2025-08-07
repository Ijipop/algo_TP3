
# PATTERN OBSERVATEUR MANQUANT
# Cette classe devrait implémenter le pattern Observateur pour gérer les notifications
# mais utilise un système de notifications codé en dur
class Notification:
    
    # VIOLATION OCP: La méthode doit être modifiée pour ajouter de nouveaux types de notifications
    def send_notification(self, message: str):
            self.send_email(message)
            self.send_sms(message)
            self.send_push_notification(message)
    
    def send_email(self, message: str):
        print(f"EMAIL: {message}")
    
    def send_sms(self, message: str):
        print(f"SMS: {message}")
    
    def send_push_notification(self, message: str):
        print(f"PUSH: {message}")


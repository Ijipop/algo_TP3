from TP3.library import Library
from TP3.notification_manager import NotificationManager
from TP3.notification import *
from TP3.searcher import *

from TP3.user import *
from TP3.book import *


# DÉMONSTRATION DU CODE PROBLÉMATIQUE. Vous pouvez adapter cette fonction pour tester différentes parties du code.
def main():
    print("=== SYSTÈME DE GESTION DE BIBLIOTHÈQUE ===")
    print()
    
    # Création du gestionnaire de notifications (pas d'observateur)
    notification_manager = NotificationManager()
    notification_manager.subscribe(NotificationEmail())
    notification_manager.subscribe(NotificationSms())
    notification_manager.subscribe(NotificationPush())

    # Création du gestionnaire principal
    library = Library(notification_manager)
    
    print("\n--- Ajout de livres ---")
    library.book_manager.add_book(Book("1984", "George Orwell", "978-0123456789", "Fiction"))
    library.book_manager.add_book(Book("Clean Code", "Robert Martin", "978-9876543210", "Informatique"))
    library.book_manager.add_book(Book("Design Patterns", "Gang of Four", "978-1111111111", "Informatique"))
    
    print("\n--- Ajout d'utilisateurs ---")
    library.user_manager.add_user(UserStudent("Alice Martin", "alice@example.com"))
    library.user_manager.add_user(UserTeacher("Prof. Dupont", "dupont@example.com"))
    library.user_manager.add_user(UserAdmin("Admin", "admin@example.com"))

    print("\n--- Emprunts ---")
    library.loan_manager.borrow_book(1, 1)  # Alice emprunte 1984
    library.loan_manager.borrow_book(2, 2)  # Prof. Dupont emprunte Clean Code

    # library.loan_manager.return_book(2)
    
    print("\n--- Recherche ---")
    results = SearcherByTitle(library.book_manager).search("Clean")
    print(f"Résultats de recherche: {len(results)} livre(s) trouvé(s)")
    
    print("\n--- Rapport des retards ---")
    library.overdue_manager.generate_overdue_report()

if __name__ == "__main__":
    main()
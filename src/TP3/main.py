from TP3.library import Library
from TP3.notification import Notification


# DÉMONSTRATION DU CODE PROBLÉMATIQUE. Vous pouvez adapter cette fonction pour tester différentes parties du code.
def main():
    print("=== SYSTÈME DE GESTION DE BIBLIOTHÈQUE ===")
    print()
    
    # Création du gestionnaire de notifications (pas d'observateur)
    notification_manager = Notification()
    # Création du gestionnaire principal
    library = Library(notification_manager=notification_manager)
    
    
    print("\n--- Ajout de livres ---")
    library.add_book("1984", "George Orwell", "978-0123456789", "Fiction")
    library.add_book("Clean Code", "Robert Martin", "978-9876543210", "Informatique")
    library.add_book("Design Patterns", "Gang of Four", "978-1111111111", "Informatique")
    
    print("\n--- Ajout d'utilisateurs ---")
    library.add_user("Alice Martin", "alice@example.com", "student")
    library.add_user("Prof. Dupont", "dupont@example.com", "teacher")
    library.add_user("Admin", "admin@example.com", "admin")
    
    print("\n--- Emprunts ---")
    library.borrow_book(1, 1)  # Alice emprunte 1984
    library.borrow_book(2, 2)  # Prof. Dupont emprunte Clean Code
    
    print("\n--- Recherche ---")
    results = library.search_books("Clean", "title")
    print(f"Résultats de recherche: {len(results)} livre(s) trouvé(s)")
    
    print("\n--- Rapport des retards ---")
    library.generate_overdue_report()

if __name__ == "__main__":
    main()
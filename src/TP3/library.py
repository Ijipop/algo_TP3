
import datetime
from TP3.notification import Notification

# VIOLATION SRP: Cette classe a trop de responsabilités
# Elle gère les livres, les utilisateurs, les emprunts, la base de données, les notifications, etc.
class Library:

    # VIOLATION DIP: Dépendance directe sur Notification
    def __init__(self, notification_manager : Notification):
        self.books = []
        self.users = []
        self.loans = []
        self.notification_manager = notification_manager
        
    # VIOLATION SRP: Gestion des livres dans la même classe que tout le reste
    def add_book(self, title: str, author: str, isbn: str, category: str):
        book = {
            'id': len(self.books) + 1,
            'title': title,
            'author': author,
            'isbn': isbn,
            'category': category,
            'available': True,
            'added_date': datetime.datetime.now().isoformat()
        }
        self.books.append(book)
        
        self.notification_manager.send_notification(f"Nouveau livre ajouté - {title}")
        
        return book
    
    # VIOLATION SRP: Gestion des livres dans la même classe que tout le reste
    def remove_book(self, book_id: int):
        for i, book in enumerate(self.books):
            if book['id'] == book_id:
                if not book['available']:
                    print("Erreur: Le livre est actuellement emprunté")
                    return False
                
                del self.books[i]
                
                self.notification_manager.send_notification(f"Livre supprimé - ID {book_id}")
                return True
        return False
    
    # VIOLATION SRP: Gestion des utilisateurs mélangée avec le reste
    def add_user(self, name: str, email: str, user_type: str):
        # VIOLATION OCP: Code dur à étendre pour de nouveaux types d'utilisateurs
        if user_type not in ['student', 'teacher', 'admin']:
            raise ValueError("Type d'utilisateur invalide")
        
        user = {
            'id': len(self.users) + 1,
            'name': name,
            'email': email,
            'type': user_type,
            'registration_date': datetime.datetime.now().isoformat(),
            'active': True
        }
        
        # VIOLATION OCP: Code dur à étendre pour de nouveaux types d'utilisateurs
        if user_type == 'student':
            user['max_loans'] = 3
            user['loan_duration'] = 14  # jours
        elif user_type == 'teacher':
            user['max_loans'] = 10
            user['loan_duration'] = 30  # jours
        elif user_type == 'admin':
            user['max_loans'] = -1  # illimité
            user['loan_duration'] = -1  # illimité
        
        self.users.append(user)
        
        self.notification_manager.send_notification(f"Nouvel utilisateur ajouté - {name}")
        return user
    
    # VIOLATION SRP: Logique d'emprunt mélangée avec la gestion des livres et des utilisateurs
    def borrow_book(self, user_id: int, book_id: int):
        user = None
        book = None
        
        # Recherche de l'utilisateur
        for u in self.users:
            if u['id'] == user_id:
                user = u
                break
        
        # Recherche du livre
        for b in self.books:
            if b['id'] == book_id:
                book = b
                break
        
        # VIOLATION OCP: Difficile d'ajouter de nouvelles règles d'emprunt
        if not user or not book:
            print("Erreur: Utilisateur ou livre introuvable")
            return False
        
        if not user['active']:
            print("Erreur: Utilisateur inactif")
            return False
        
        if not book['available']:
            print("Erreur: Livre non disponible")
            return False
        
        current_loans = [loan for loan in self.loans if loan['user_id'] == user_id
                         and not loan['returned']]
        
        # VIOLATION OCP: Code dur à étendre pour de nouveaux types d'utilisateurs
        if user['type'] == 'student' and len(current_loans) >= 3:
            print("Erreur: Limite d'emprunts atteinte pour les étudiants")
            return False
        elif user['type'] == 'teacher' and len(current_loans) >= 10:
            print("Erreur: Limite d'emprunts atteinte pour les enseignants")
            return False
        
        # Création de l'emprunt
        loan = {
            'id': len(self.loans) + 1,
            'user_id': user_id,
            'book_id': book_id,
            'loan_date': datetime.datetime.now().isoformat(),
            'due_date': self.calculate_due_date(user['type']),
            'returned': False,
            'return_date': None
        }
        
        self.loans.append(loan)
        book['available'] = False
        
        self.notification_manager.send_notification(f"Emprunt effectué - Livre: {book['title']}, Utilisateur: {user['name']}")
        
        return True
    
    def calculate_due_date(self, user_type: str):
        days = 14  # défaut
        # VIOLATION OCP: Code dur à étendre pour de nouveaux types d'utilisateurs
        if user_type == 'teacher':
            days = 30
        elif user_type == 'admin':
            return None  # pas de limite
        
        due_date = datetime.datetime.now() + datetime.timedelta(days=days)
        return due_date.isoformat()
    
    # VIOLATION SRP: Logique de retour mélangée avec tout le reste
    def return_book(self, loan_id: int):
        for loan in self.loans:
            if loan['id'] == loan_id:
                if loan['returned']:
                    print("Erreur: Livre déjà retourné")
                    return False
                
                loan['returned'] = True
                loan['return_date'] = datetime.datetime.now().isoformat()
                
                # Marquer le livre comme disponible
                for book in self.books:
                    if book['id'] == loan['book_id']:
                        book['available'] = True
                        break
                
                self.notification_manager.send_notification(f"Retour effectué - ID Emprunt: {loan_id}")
                
                return True
        
        print("Erreur: Emprunt introuvable")
        return False
    
    # VIOLATION SRP: Recherche mélangée avec tout le reste
    # VIOLATION OCP: Difficile d'ajouter de nouveaux critères de recherche
    def search_books(self, search_term: str, search_type: str = 'title'):
        results = []
        
        if search_type == 'title':
            results = [book for book in self.books if search_term.lower() in book['title'].lower()]
        elif search_type == 'author':
            results = [book for book in self.books if search_term.lower() in book['author'].lower()]
        elif search_type == 'isbn':
            results = [book for book in self.books if search_term in book['isbn']]
        elif search_type == 'category':
            results = [book for book in self.books if search_term.lower() in book['category'].lower()]
        else:
            print("Type de recherche invalide")
            return []
        
        return results
    
    # VIOLATION SRP: Génération de rapports dans la classe principale
    def generate_overdue_report(self):
        overdue_loans = []
        current_date = datetime.datetime.now()
        
        for loan in self.loans:
            if not loan['returned'] and loan['due_date']:
                due_date = datetime.datetime.fromisoformat(loan['due_date'])
                if current_date > due_date:
                    # Recherche des détails
                    user = next((u for u in self.users if u['id'] == loan['user_id']), None)
                    book = next((b for b in self.books if b['id'] == loan['book_id']), None)
                    
                    overdue_loans.append({
                        'loan': loan,
                        'user': user,
                        'book': book,
                        'days_overdue': (current_date - due_date).days
                    })
        
        # PATTERN OBSERVATEUR MANQUANT: Notification automatique des retards
        if overdue_loans:
            print(f"RAPPORT: {len(overdue_loans)} emprunts en retard")
            for overdue in overdue_loans:
                print(f"- {overdue['book']['title']} par {overdue['user']['name']} "
                      f"({overdue['days_overdue']} jours de retard)")
                
                # Notification directe (violation du pattern Observateur)
                self.send_email_notification(
                    f"Retard: {overdue['book']['title']} - {overdue['days_overdue']} jours"
                )
        
        return overdue_loans

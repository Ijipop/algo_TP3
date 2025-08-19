
from TP3.notification_manager import NotificationManager
from TP3.user_manager import UserManager
from TP3.book_manager import BookManager
from TP3.loan_manager import LoanManager
from TP3.loan import *
from TP3.book import *
from TP3.user import *
from TP3.rules import *

class OverdueManager:
    def __init__(self, notification_manager: NotificationManager, user_manager: UserManager, book_manager: BookManager, loan_manager: LoanManager):
        self.notification_manager = notification_manager
        self.user_manager = user_manager
        self.book_manager = book_manager
        self.loan_manager = loan_manager
        self.overdues: list = []

    def generate_overdue_report(self):
        self.overdues = []
        current_date = datetime.datetime.now()
        # current_date = datetime.datetime.now() + datetime.timedelta(days=100) # For testing overdues

        for loan in self.loan_manager.loans:
            if not loan.getReturned() and loan.getReturnDate() is None:
                due_date = loan.getDueDate()
                if due_date is None:
                    continue
                if current_date > due_date:
                    # Recherche des détails
                    user: User = next((u for u in self.user_manager.users if u.getId() == loan.getUserId()), None)
                    book: Book = next((b for b in self.book_manager.books if b.getId() == loan.getBookId()), None)
                    
                    self.overdues.append({
                        'loan': loan,
                        'user': user,
                        'book': book,
                        'days_overdue': (current_date - due_date).days
                    })
        
        if self.overdues:
            self.send_report()

        return self.overdues
        
    def send_report(self):
        print(f"RAPPORT: {len(self.overdues)} emprunts en retard")
        for overdue in self.overdues:
            print(f"- {overdue['book'].getTitle()} par {overdue['user'].getName()} "
                f"({overdue['days_overdue']} jours de retard)")
            
            self.notification_manager.notify(f"Retard: {overdue['book'].getTitle()} - {overdue['days_overdue']} jours")
        
        return self.overdues
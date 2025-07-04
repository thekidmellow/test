from datetime import datetime
from typing import List, Dict, Any, Optional
from data_handler import DataHandler


class ExpenseManager:
    """Manages expense operations and business logic"""

    def __init__(self):
        self.data_handler = DataHandler()
        self.categories = [
            "Food", "Transportation", "Entertainment", "Shopping",
            "Bills", "Healthcare", "Education", "Other"
        ]

    def add_expense(self, amount: float, category: str, description: str) -> bool:
        """Add a new expense"""
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if category not in self.categories:
            raise ValueError(f"Invalid category. Choose from: {', '.join(self.categories)}")

        expense = {
            "id": self._generate_id(),
            "amount": round(amount, 2),
            "category": category,
            "description": description.strip(),
            "date": datetime.now().isoformat()
        }

        expenses = self.data_handler.load_expenses()
        expenses.append(expense)
        return self.data_handler.save_expenses(expenses)

    def get_all_expenses(self) -> List[Dict[str, Any]]:
        """Get all expenses"""
        return self.data_handler.load_expenses()

    def get_expenses_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get expenses filtered by category"""
        expenses = self.get_all_expenses()
        return [exp for exp in expenses if exp['category'].lower() == category.lower()]

    def calculate_total(self, expenses: Optional[List[Dict[str, Any]]] = None) -> float:
        """Calculate total amount of expenses"""
        if expenses is None:
            expenses = self.get_all_expenses()
        return round(sum(exp['amount'] for exp in expenses), 2)

    def get_category_summary(self) -> Dict[str, float]:
        """Get spending summary by category"""
        expenses = self.get_all_expenses()
        summary = {}

        for expense in expenses:
            category = expense['category']
            summary[category] = summary.get(category, 0) + expense['amount']

        return {k: round(v, 2) for k, v in summary.items()}

    def _generate_id(self) -> int:
        """Generate unique ID for new expense"""
        expenses = self.get_all_expenses()
        return max([exp.get('id', 0) for exp in expenses], default=0) + 1

    def get_categories(self) -> List[str]:
        """Get available categories"""
        return self.categories.copy()

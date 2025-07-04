import json
import os
from datetime import datetime
from typing import List, Dict, Any


class DataHandler:
    """Handles all file operations for expense data"""

    def __init__(self, filename: str = "expenses.json"):
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self) -> None:
        """Create the data file if it doesn't exist"""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump([], file)

    def load_expenses(self) -> List[Dict[str, Any]]:
        """Load all expenses from the JSON file"""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_expenses(self, expenses: List[Dict[str, Any]]) -> bool:
        """Save expenses to the JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(expenses, file, indent=2, default=str)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False

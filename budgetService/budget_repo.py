class IBudgetRepo:
    def __init__(self, ls) -> None:
        self.budgetLs = ls

    def getAll(self) -> list:
        return self.budgetLs

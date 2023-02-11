from budget_repo import IBudgetRepo


class BudgetService:
    def __init__(self, budgetRepo) -> None:
        self.budgetRepo = budgetRepo

    def query(self, start, end) -> float:
        budgetLs = self.budgetRepo.getAll()
        if len(budgetLs) > 0:
            startYM = start.strftime("%Y%m")
            amount = 0
            for b in budgetLs:
                if b.yearMonth == startYM:
                    amount = b.amount
                    break
            return amount / 31
        return 0.0

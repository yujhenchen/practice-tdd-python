from budget_repo import IBudgetRepo


class BudgetService:
    def __init__(self, budgetRepo) -> None:
        self.budgetRepo = budgetRepo

    def query(self, start, end) -> float:
        budgetLs = self.budgetRepo.getAll()
        if len(budgetLs) > 0:
            startYM = start.strftime("%Y%m")
            endYM = end.strftime("%Y%m")
            amount = budgetLs[0].amount
            diff_day = (end - start).days + 1

            if budgetLs[0].yearMonth == startYM and diff_day == 31:
                return amount
            if budgetLs[0].yearMonth == startYM:
                return amount / 31
            # amount = 0
            # for b in budgetLs:

            #     if b.yearMonth == startYM:
            #         amount = b.amount
            #         break
            # month_days =
            # return amount / 31
        return 0.0

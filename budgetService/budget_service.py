from budget_repo import IBudgetRepo
import datetime
import calendar

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
            budgetMonth = datetime.datetime.strptime(budgetLs[0].yearMonth, "%Y%m")
            days_in_month = calendar.monthrange(budgetMonth.year, budgetMonth.month)[1]

            if budgetLs[0].yearMonth == startYM:
                return amount / days_in_month * diff_day

        return 0.0

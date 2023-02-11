import unittest
from budget_repo import IBudgetRepo
from budget_service import BudgetService
from datetime import date
from budget import Budget


class BudgetTestCase(unittest.TestCase):
    
    
    def test_one_day_no_budget(self):
        budgetRepo = IBudgetRepo([])
        budgetService = BudgetService(budgetRepo)
        start = date.fromisoformat("2019-12-04")
        end = date.fromisoformat("2019-12-04")
        self.assertEqual(budgetService.query(start, end), 0.0)

    def test_one_day_has_budget_within(self):
        budgetRepo = IBudgetRepo([Budget("201912", 3100)])
        budgetService = BudgetService(budgetRepo)
        start = date.fromisoformat("2019-12-04")
        end = date.fromisoformat("2019-12-04")
        self.assertEqual(budgetService.query(start, end), 100)
        

    def test_two_day_has_budget_within(self):
        budgetRepo = IBudgetRepo([Budget("201912", 3100)])
        budgetService = BudgetService(budgetRepo)
        start = date.fromisoformat("2019-12-04")
        end = date.fromisoformat("2019-12-05")
        self.assertEqual(budgetService.query(start, end), 200)


    def test_one_month_has_budget_within(self):  
        budgetRepo = IBudgetRepo([Budget("201912", 3100)])
        budgetService = BudgetService(budgetRepo)
        start = date.fromisoformat("2019-12-01")
        end = date.fromisoformat("2019-12-31")
        self.assertEqual(budgetService.query(start, end), 3100)
        

    # def test_cross_month_has_budget_within(self):  
    #     budgetRepo = IBudgetRepo([Budget("201911", 30000),Budget("201912", 3100)])
    #     budgetService = BudgetService(budgetRepo)
    #     start = date.fromisoformat("2019-11-29")
    #     end = date.fromisoformat("2019-12-03")
    #     self.assertEqual(budgetService.query(start, end), 2300)


if __name__ == "__main__":
    unittest.main()

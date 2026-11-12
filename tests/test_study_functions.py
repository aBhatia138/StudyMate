import unittest
from datetime import date, timedelta

from src.study_functions import (
    compound_interest_calculator,
    percentage_calculator,
    generate_study_plan,
    days_until_exam
)

class TestStudyFunctions(unittest.TestCase):

    def test_compound_interest(self):

        result = compound_interest_calculator(5000, 6, 3)

        self.assertAlmostEqual(
            result["final_amount"],
            5955.08,
            places=2
        )

    def test_percentage(self):

        result = percentage_calculator(850, 15)

        self.assertEqual(result["result"], 127.5)

    def test_days_until_exam(self):

        exam_date = (
            date.today() + timedelta(days=10)
        ).isoformat()

        result = days_until_exam(exam_date)

        self.assertEqual(
            result["days_remaining"],
            10
        )

    def test_study_plan(self):

        result = generate_study_plan(
            ["Maths", "Statistics", "Economics"],
            5,
            3
        )

        self.assertEqual(
            len(result["study_plan"]),
            5
        )

        self.assertEqual(
            result["study_plan"][4]["subject"],
            "Statistics"
        )

    def test_invalid_percentage(self):

        with self.assertRaises(ValueError):
            percentage_calculator(float("inf"), 15)

    def test_invalid_exam_date(self):

        with self.assertRaises(ValueError):
            days_until_exam("15-12-2026")

    def test_invalid_study_plan(self):

        with self.assertRaises(ValueError):
            generate_study_plan([], 7, 3)

if __name__ == "__main__":
    unittest.main()
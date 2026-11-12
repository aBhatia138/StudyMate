
import unittest

from src.tool_registry import TOOL_REGISTRY, execute_tool


class TestToolRegistry(unittest.TestCase):

    # --------------------------------------------------
    # 1. Registry structure
    # --------------------------------------------------

    def test_all_tools_are_registered(self):

        expected_tools = {
            "percentage_calculator",
            "compound_interest_calculator",
            "days_until_exam",
            "generate_study_plan"
        }

        self.assertEqual(set(TOOL_REGISTRY.keys()), expected_tools)

    # --------------------------------------------------
    # 2. Successful tool execution
    # --------------------------------------------------

    def test_percentage_calculator_execution(self):

        arguments = {
            "value": 850,
            "percentage": 15
        }

        result = execute_tool("percentage_calculator", arguments)

        self.assertEqual(result["result"], 127.5)
        self.assertEqual(result["value"], 850)
        self.assertEqual(result["percentage"], 15)

    def test_compound_interest_execution(self):

        arguments = {
            "principal": 5000,
            "annual_rate": 6,
            "years": 3
        }

        result = execute_tool("compound_interest_calculator", arguments)

        self.assertAlmostEqual(result["final_amount"], 5955.08)
        self.assertAlmostEqual(result["interest_earned"], 955.08)

    def test_days_until_exam_execution(self):

        arguments = {
            "exam_date": "2026-12-15"
        }

        result = execute_tool("days_until_exam", arguments)

        self.assertEqual(result["exam_date"], "2026-12-15")
        self.assertIsInstance(result["days_remaining"], int)
        self.assertIsInstance(result["exam_has_passed"], bool)

    def test_study_plan_execution(self):

        arguments = {
            "subjects": ["Mathematics", "Statistics", "Finance"],
            "available_days": 5,
            "hours_per_day": 4
        }

        result = execute_tool("generate_study_plan", arguments)

        self.assertEqual(result["total_days"], 5)
        self.assertEqual(len(result["study_plan"]), 5)

        self.assertEqual(
            result["study_plan"][0]["subject"],
            "Mathematics"
        )

        self.assertEqual(
            result["study_plan"][1]["subject"],
            "Statistics"
        )

        self.assertEqual(
            result["study_plan"][2]["subject"],
            "Finance"
        )

    # --------------------------------------------------
    # 3. Error handling
    # --------------------------------------------------

    def test_unknown_tool(self):

        with self.assertRaises(ValueError):
            execute_tool("stock_price_predictor", {})

    def test_missing_required_argument(self):

        arguments = {
            "value": 850
        }

        with self.assertRaises(TypeError):
            execute_tool("percentage_calculator", arguments)

    def test_invalid_function_arguments(self):

        arguments = {
            "subjects": [],
            "available_days": 5,
            "hours_per_day": 4
        }

        with self.assertRaises(ValueError):
            execute_tool("generate_study_plan", arguments)


if __name__ == "__main__":
    unittest.main()

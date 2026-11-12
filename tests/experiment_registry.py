
from src.tool_registry import TOOL_REGISTRY, execute_tool

print("Available tools:")

for tool_name in TOOL_REGISTRY:
    print(tool_name)

print("\nTesting percentage calculator:")

function_to_execute = TOOL_REGISTRY["percentage_calculator"]

result = function_to_execute(
    value=850,
    percentage=15
)

print(result)

print("\nTesting unknown tool:")

try:
    execute_tool(
        tool_name="stock_price_predictor",
        arguments={}
    )
except ValueError as error:
    print(f"Error caught: {error}")

print("\nTesting invalid argument types:")

try:
    execute_tool(
        tool_name="percentage_calculator",
        arguments={
            "value": "850",
            "percentage": 15
        }
    )
except ValueError as error:
    print(f"Validation error caught: {error}")


print("\nTesting missing arguments:")

try:
    execute_tool(
        tool_name="percentage_calculator",
        arguments={
            "value": 850
        }
    )
except ValueError as error:
    print(f"Validation error caught: {error}")

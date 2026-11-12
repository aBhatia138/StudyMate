from src.groq_client import get_response
from src.tool_definitions import TOOLS
from src.tool_registry import execute_tool
import json

messages = [
    {
        "role": "system",
        "content": (
            "You are StudyMate, a helpful AI assistant. "
            "Use the available tools whenever they are relevant. "
        )
    },

    {
        "role": "user",
        "content": (
            "Calculate 15% of 850 and 20% of 1200. "
            "Calculate both separately. "
        )
    }
]

response = get_response(messages, tools=TOOLS)

tool_call = response.tool_calls[0]

tool_call_function = tool_call.function

tool_name = tool_call_function.name

# print(f"\n\n{response}")

# print(f"\n\n{tool_call}")

# print(f"\n\n{tool_call_function}")

# print(f"\n\nTool name requested: {tool_name}")

arguments_str = tool_call.function.arguments

arguments = json.loads(arguments_str)

# result = execute_tool(
#     tool_name,
#     arguments
# )

# print(f"\nExecuted Tool Result: {result}")

# print(f"Arguments: {arguments_str}")

# print(f"\n\nArguments in json format: {arguments}")

messages.append(
    response.model_dump(exclude_none=True)
)

for tool_call in response.tool_calls:

    tool_name = tool_call.function.name

    arguments = json.loads(
        tool_call.function.arguments
    )

    result = execute_tool(tool_name, arguments)

    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(result)
    })

    print(f"\nExecuted: {tool_name}")
    print(f"Result: {result}")

    final_response = get_response(messages, tools=TOOLS)

    print("\nStudyMate's final response:")
    print(final_response.content)
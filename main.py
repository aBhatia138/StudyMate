from src.groq_client import get_response

#Initial conversation instructions
messages = [
    {
        "role": "system",
        "content": (
            "You are StudyMate, a helpful and concise "
            "AI study assistant. Help students understand "
            "academic concepts clearly. "
        )
    }
]

print("=" * 45)
print("          WELCOME TO STUDYMATE")
print("=" * 45)
print("Ask me anything about your studies!")
print("Type 'exit' to quit.")
print("=" * 45)

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("StudyMate: Goodbye!")
        break

    if not user_input:
        continue

    #Add user message to the conversation
    messages.append({
        "role": "user",
        "content": user_input
    })

    try:

        #Obtain reponse from groq
        assistant_response = get_response(messages)

        #Add assistant reponse to conversation
        messages.append({
            "role": "assistant",
            "content": assistant_response
        })

        print(f"\nStudyMate: {assistant_response}")

    except Exception as e:
        print("\nAn error occured:", e)
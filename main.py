from nemoguardrails import Rails

# Load configuration
rails = Rails("guardrails_config/")

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    response = rails.generate(user_input)
    print("Guarded:", response)

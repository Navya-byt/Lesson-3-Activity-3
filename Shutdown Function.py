# Define the shutdown function
def shutdown(command):
    if command == "yes":
        return "Shutting down..."
    elif command == "no":
        return "Shutdown aborted!"
    else:
        return "Sorry, I don't understand."

# Ask the user
user_input = input("Do you want to shut down? (yes/no): ").lower()

# Call the function and print the result
print(shutdown(user_input))


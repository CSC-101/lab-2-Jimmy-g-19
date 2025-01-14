# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "Jimmy.."
   return message


message = welcome_message("jmart792@calpoly.edu")
print(message)

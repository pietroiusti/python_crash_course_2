responses = {}

polling_active = True

while polling_active:

    name = input("\nName? ")
    response = input("What's your dream vacation? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name}'s deam vaction: {response}.")

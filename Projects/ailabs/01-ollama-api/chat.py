from utils import generate

print("Type 'exit' to quit.\n")

while True:

    prompt = input("You > ")

    if prompt.lower() == "exit":
        break

    print()
    print("AI >")
    print(generate(prompt))
    print()
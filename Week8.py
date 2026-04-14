try:
    open("message.txt", "x")
    print("File created!")
except:
    print("File already exists!")


while True:
    print("\n1. Send Message")
    print("2. View Messages")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        message = input("Enter message: ")
        file = open("message.txt", "a")
        file.write(message + "\n")
        file.close()
        print("Message saved!")

    elif choice == "2":
        try:
            file = open("message.txt", "r")
            print("\nMessages:")
            print(file.read())
            file.close()
        except:
            print("Error reading file!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

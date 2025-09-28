name = input("Enter name: ")
choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>> ").lower()
while choice != 'q':
    if choice == 'h':
        print(f"Hello {name}")
    elif choice == 'g':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>> ").lower()
print("Finished.")
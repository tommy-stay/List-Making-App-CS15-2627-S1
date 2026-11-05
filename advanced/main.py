import time

todo_list = []
completed_list = []
saved_todo_list = []
saved_completed_list = []

print("I'm not going to make a story for this one...")
time.sleep(5)
print("Just kidding.")
time.sleep(1)

story = """
Welcome back. Long time no see I guess.
Now, from the last one, you built your list and it was quite nice I guess.
Whether or not, you actually put anything in it.

....
Guess what you're going to do here?
Take a wild guess! It's really different, unique, and fun!

It's not.. different.
We're making a list.
Again.
Fun, right?
"""
print(story)
time.sleep(8)

story2 = """
But you know... this time, I've updated the system!
Yeah! Now you can actually check off your items!
Because that's normally what you do with a grocery list.
...
But at least give me credit, I tried, didn't I?

...

Anyways! You can also replace items! 
So get right to it!
"""
print(story2)
time.sleep(8)

while True:
    print()
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display a List")
    print("4. Undo the Previous Change")
    print("5. Replace an Item")
    print("6. Check Off an Item")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        saved_todo_list = todo_list.copy()
        saved_completed_list = completed_list.copy()

        item = input("Enter the item to add: ")
        todo_list.append(item)
        print(item, "was added to the to-do list.")

    elif choice == "2":
        item_count = 0
        for item in todo_list:
            item_count = item_count + 1

        if item_count == 0:
            print("The to-do list is empty.")
        else:
            saved_todo_list = todo_list.copy()
            saved_completed_list = completed_list.copy()

            print("Current to-do items:")
            index = 0
            for item in todo_list:
                print(index, "-", item)
                index = index + 1

            remove_index = int(input("Enter the index of the item to remove: "))

            if remove_index >= 0 and remove_index < item_count:
                removed_item = todo_list.pop(remove_index)
                print(removed_item, "was removed from the to-do list.")
            else:
                print("That index does not exist.")

    elif choice == "3":
        list_choice = input("Which list do you want to view? Enter 1 for to-do or 2 for bought: ")

        if list_choice == "1":
            item_count = 0
            for item in todo_list:
                item_count = item_count + 1

            if item_count == 0:
                print("The to-do list is empty.")
            else:
                print("Current to-do list:")
                index = 0
                for item in todo_list:
                    print(index, "-", item)
                    index = index + 1

        elif list_choice == "2":
            item_count = 0
            for item in completed_list:
                item_count = item_count + 1

            if item_count == 0:
                print("The completed list is empty.")
            else:
                print("Completed items:")
                index = 0
                for item in completed_list:
                    print(index, "-", item)
                    index = index + 1

        else:
            print("That is not a valid list choice.")

    elif choice == "4":
        if saved_todo_list == [] and saved_completed_list == []:
            print("There is no previous change to undo.")
        else:
            todo_list = saved_todo_list.copy()
            completed_list = saved_completed_list.copy()
            saved_todo_list = []
            saved_completed_list = []
            print("The previous change was undone.")

    elif choice == "5":
        item_count = 0
        for item in todo_list:
            item_count = item_count + 1

        if item_count == 0:
            print("The to-do list is empty.")
        else:
            saved_todo_list = todo_list.copy()
            saved_completed_list = completed_list.copy()

            print("Current to-do items:")
            index = 0
            for item in todo_list:
                print(index, "-", item)
                index = index + 1

            replace_index = int(input("Enter the index of the item to replace: "))

            if replace_index >= 0 and replace_index < item_count:
                new_item = input("Enter the new item: ")
                todo_list[replace_index] = new_item
                print("The item was replaced with", new_item)
            else:
                print("That index does not exist.")

    elif choice == "6":
        item_count = 0
        for item in todo_list:
            item_count = item_count + 1

        if item_count == 0:
            print("The to-do list is empty.")
        else:
            saved_todo_list = todo_list.copy()
            saved_completed_list = completed_list.copy()

            print("Current to-do items:")
            index = 0
            for item in todo_list:
                print(index, "-", item)
                index = index + 1

            complete_index = int(input("Enter the index of the item to check off: "))

            if complete_index >= 0 and complete_index < item_count:
                completed_item = todo_list.pop(complete_index)
                completed_list.append(completed_item)
                print(completed_item, "was checked off.")
            else:
                print("That index does not exist.")


    elif choice == "7":
        if completed_list == []:
            time.sleep(3)
            print("Oh come on!")
            time.sleep(1)
            print("We've been through this!")
            time.sleep(1)
            print("Mr. Forsyth is hungry! He's hungry and waiting!")
            time.sleep(1)
            print("How could you leave without filling out the list?!")
            time.sleep(2)
            print("Ugh!")
            print("Goodbye!")
            break
        else:
            print("Hope you tried out the new functions...")
            time.sleep(2)
            print("I worked really hard on those...")
            time.sleep(2)
            print("🥺")
            time.sleep(1)
            print("Anyways, go and uh.. do whatever you want to with the list.")
            time.sleep(2)
            print("...")
            time.sleep(1)
            print("Bye.")
            break
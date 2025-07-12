def main():
    repeat = ''
    while repeat != "no":
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")
        fruit_list.reverse()
        print(f"reversed: {fruit_list}")
        fruit_list.append("orange")
        print(f"append orange: {fruit_list}")
        fruit_list.insert(1, "cherry")
        print(f"insert cherry: {fruit_list}")
        fruit_list.remove("banana")
        # fruit_list.pop(3)
        print(f"remove banana: {fruit_list}")
        popped_fruit = fruit_list.pop()
        print(f"pop {popped_fruit}: {fruit_list}")
        fruit_list.sort()
        print(f"sorted: {fruit_list}")
        fruit_list.clear()
        print(f"cleared: {fruit_list}")

        repeat = input("Would you like to repeat the code (yes/no)? ")

if __name__ == "__main__":
    main()
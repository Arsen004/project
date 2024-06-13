'''fdg'''

def greet_all(name1, name2, *names):
    print(f"Здравствуйте, {name1}!")
    print(f"Здравствуйте, {name2}!")
    for name in names:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    greet_all("Вася", "Петя", "Коля", "Оля")

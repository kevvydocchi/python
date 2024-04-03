
for i in range(1,11):
    if i % 3 == 0:
        break
    print(i)





rows = int(input("enter any number = "))

for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print("\n")

print("\n")


for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print("\n")

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
    


rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end="")

    print("\n")
number = int(input())
answer = ""
while True:
    if answer == "":
        answer = str(number)
    else:
        answer += " " + str(number)
    
    if number == 1:
        break
    if number % 2 == 0:
        number = int(number / 2)
    else:
        number = (3 * number) + 1

print(answer)
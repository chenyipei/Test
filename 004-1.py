import random
answer = random.randint(0,100)
temp = input("猜猜数字，范围0-100，你有5次猜测机会：")
guess = int(temp)
time=5
while time > 1:
    if guess == answer:
        print("回答正确")
        break
    else:
        if guess > answer:
            print("大了")
        else:
            print("小了")
    time = time-1
    temp = input("请重新输入，你还有%s次机会:"%time)
print("game over,the answer is %s" %answer)

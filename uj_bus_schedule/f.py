
    
start = int(input())
end = int(input())
second = 1

# print(start, second)

end -= 2

while end > 0:

    next = start + second
    print(next)

    temp = second
    second = start + second
    start = temp
    end -= 1
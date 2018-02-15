words = "It's thanksgiving day. It's my birthday, too!"

print words.find("day")

words2 = words.replace("day", "month")

print words2

x = [2,54,-2,7,12,98]

print min(x)
print max(x)

x = ["hello", 2, 54, -2, 7, 12, 98, "world"]

print x[0]
print x[len(x)-1]

newx = [x[0], x[len(x)-1]]
print newx

x = [19,2,52,-2,7,12,98,32,10,-3,6]

x.sort()

y = x[:len(x)/2]
z = x[len(x)/2:]

z.insert(0,y)

print z
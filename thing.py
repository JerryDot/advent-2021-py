print("hi")
with open('thing.txt', 'rb') as f:
    input = f.readlines()

ticker = 0
ans = 0
last_thing = [0, 0, 0]
last_value = 0
for thing in input:
    try:
        last_thing.append(int(thing))
        del last_thing[0]
        if ticker < 3:
            pass
        else:
            if sum(last_thing) > last_value:
                ans += 1
        last_value = sum(last_thing)
    except:
        pass
    ticker += 1
print(ans)
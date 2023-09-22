data = input().split()
try:
    a, b = map(int, data)
except ValueError:
    try:
        a, b = map(float, data)
    except ValueError:
        a, b = data
finally:
    ttl = a + b
    print(ttl)











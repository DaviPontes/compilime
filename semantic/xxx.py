import scopeAnalyzer as scope

for i in range(0, 10):
    print(f"for - {i}")
    j = 0
    while j != 3:
        j += 1
        print(f"while - {j}")
        if j == 2:
            break
    if i == 2:
        break

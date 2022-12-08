def D(xi, yi):
    if min(xi, yi) >= 0:
        return 1 - ((1 + min(xi, yi)) / (1 + max(xi, yi)))
    else:
        return 1 - ((1 + max(xi, yi) + abs(min(xi, yi))) / (1 + max(xi, yi) + abs(min(xi, yi))))

def H(x, y):
    return sum([D(x[i], y[i]) for i in range(len(x))])
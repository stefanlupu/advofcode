def main():
    with open("input.txt", "r") as f:
        lines = f.read().strip().split("\n")

    count = len(lines)
    left, right = [], []
    for line in lines:
        l = line.strip().split(" ")
        left.append(int(l[0]))
        right.append(int(l[-1]))

    left.sort()
    right.sort()

    totaldiff = 0
    for i in range(count):
        totaldiff = totaldiff + abs(left[i] - right[i])

    print(totaldiff)


if __name__ == "__main__":
    main()

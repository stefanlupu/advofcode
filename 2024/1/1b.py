def main():
    with open("input.txt", "r") as f:
        lines = f.read().strip().split("\n")

    count = len(lines)
    left, right = [], []
    for line in lines:
        l = line.strip().split(" ")
        left.append(int(l[0]))
        right.append(int(l[-1]))

    watch = {}
    totaldiff = 0
    for i in range(count):
        if left[i] not in watch.keys():
            watch[left[i]] = [1, 0]
        else:
            watch[left[i]][0] += 1

        if left[i] in right:
            watch[left[i]][1] = right.count(left[i])

    for key, val in watch.items():
        totaldiff = totaldiff + (key * val[0] * val[1])
    print(totaldiff)


if __name__ == "__main__":
    main()

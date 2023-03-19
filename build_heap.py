# python3
def heap(data, n, i, swaps):
    s = i 
    right = 2*i+2
    left=2*i+1

    if left<n and data[i] > data[left]:
        s = left

    if right<n and data[s] > data[right]:
        s = right

    if s != i :
        data[i], data[s] = data[s], data[i]
        swaps.append((i, s))
        heap(data, n , s, swaps)


def build_heap(data, n):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    for i in range (n//2,-1,-1):
        heap(data, n,i,swaps) 


    return swaps


def main():
    try:
        teksts = input("Enter I or F")
        if teksts.startswith('I'):
            n = int(input("Enter num"))
            data = list(map(int, input().split()))
        elif teksts.startswith('F'):
            filename = "tests/" + input("Enter file")
            with open(filename, "r") as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))

        assert len(data) == n
        swaps = build_heap(data, n)

        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    except Exception as e:
        print("Error")
        return



if __name__ == "__main__":
    main()

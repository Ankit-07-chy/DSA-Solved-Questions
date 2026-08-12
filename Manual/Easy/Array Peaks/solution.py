import sys


def arrayPeaks(n, target):
    # Write your code here
    result = []
    if n < 3:
        if n == 1:
            return target
        if n == 2:
            result = []
            if target[0]>target[1]:
                result.append(target[0])
            elif target[1]>target[0]:
                result.append(target[1])
            
            return result
    else:
        if target[0] > target[1]:
            result.append(target[0])
        # n = len(target)
        for i in range(1,n-1):
            if target[i] > target[i-1] and target[i] > target[i+1]:
                result.append(target[i])

        if target[n-1]>target[n-2]:
            result.append(target[-1])
    return result 


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    target = [int(x) for x in data[1:1 + n]]
    res = arrayPeaks(n, target)
    out = [str(len(res))]
    if res:
        out.append(" ".join(map(str, res)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

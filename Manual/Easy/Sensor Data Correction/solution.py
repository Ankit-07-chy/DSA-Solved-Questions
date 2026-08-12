import sys


def sensorDataCorrection(sensorReadings):
    # Write your code here
    '''
    Suspected Reading : atleast one pair of equal digits stanidn next to each other

    O(n) -> solution wants
    '''

    def check_corrupted(read):
        n = len(read)
        for i in range(n-1):
            if read[i] == read[i+1]:
                return True 
        return False

    def find_sum(read):
        ans = 0
        for s in read:
            ans += int(s)
        return str(ans)
    # print(type(sensorReadings)) -> this is string
    sensorReadings = sensorReadings.split(' ')
    
    ans = []
    for reading in sensorReadings:
        # reading is also string
        temp = check_corrupted(reading) # True if corrupted else False
        if temp == False:
            ans.append(reading)
        else:
            ans.append(find_sum(reading))
    return ' '.join(ans)



def main():
    sensorReadings = sys.stdin.buffer.read().decode().strip()
    sys.stdout.write(sensorDataCorrection(sensorReadings) + "\n")


if __name__ == "__main__":
    main()

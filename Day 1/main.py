def convert(): 
    #This function will basiclly convert the raw data to list so that it can be used. IN <-- raw_data.txt || OUT --> usable_data.txt
    file = "Day 1/raw_data.txt"
    data = open(file, "r").read().split()
    #print(data)
    return data

def solution(data):
    final = 1
    for i in range(1, len(data)):
        if i == 0:
            print(f"{data[i]} (No previous increment)")
            pass
        
        else:
            previouslist = data[i-1]
            currentlist = data[i]

            if previouslist < currentlist:
                print(f"{currentlist} (Increasing)")
                final += 1

            elif previouslist > currentlist:
                pass
                print(f"{currentlist} (Decreasing)")
    
    print(f"Total final answer is: {final}")

if __name__ == "__main__":
    #solution([5,3,7,1,4])
    solution(convert())
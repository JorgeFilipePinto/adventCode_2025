#We need verify what ID is invalid
#At the end we need to add up all

test = [
    "11-22",
    "95-115",
    "998-1012",
    "1188511880-1188511890",
    "222220-222224",
    "1698522-1698528",
    "446443-446449",
    "38593856-38593862"
]


def getInputs(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    lines = lines[0].split(",")
    return lines



def getInvalidIDs(idList):
    print("Let's find out how many invalid IDs we have.")
    invalidIDs = 0
    for ids in idList:
        idRange = ids.split("-")
        min = idRange[0]
        max = idRange[1]
        counter = int(min)
        
        while counter <= int(max):
            strCounter = str(counter)
            halfSize = len(strCounter) / 2
            isInvalid = False
            
            if len(strCounter) % 2 == 0:
                if strCounter[:int(len(strCounter) / 2)] == strCounter[int(len(strCounter) / 2):]:
                    isInvalid = True

                if isInvalid:
                    invalidIDs += counter

            counter += 1
    return invalidIDs


inputs = getInputs("inputs.txt")
print(f"It has {getInvalidIDs(inputs)} invalid IDs")
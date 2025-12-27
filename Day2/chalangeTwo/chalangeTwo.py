#Equal to chalangeOne but now we have new rugles


test = [
"11-22",
"95-115",
"998-1012",
"1188511880-1188511890",
"222220-222224",
"1698522-1698528",
"446443-446449",
"38593856-38593862",
"565653-565659",
"824824821-824824827",
"2121212118-2121212124"
]


def getInputs(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    lines = lines[0].split(",")
    return lines

def getInvalidIDs(inputData):
    invalidIDs = 0
    print("Let's find out how many invalid IDs we have.")

    for ids in inputData:
        idRange = ids.split("-")
        min = idRange[0]
        max = idRange[1]
        print(f"min: {min} - max: {max}")
        counter = int(min)
        invalidIDsList = []
        
        while counter <= int(max):
            strCounter = str(counter)
            halfSize = len(strCounter) / 2
            isInvalid = everyNumberAreEqual(strCounter)

            if len(strCounter) % 2 == 0 and not isInvalid:
                if strCounter[:int(len(strCounter) / 2)] == strCounter[int(len(strCounter) / 2):]:
                    isInvalid = True
                elif strCounter[:2] == strCounter[len(strCounter) - 2:len(strCounter)] and int(len(strCounter) / 2) > 1:
                    numberOfParts = int(len(strCounter) / 2)
                    parts = []
                    for i in range(0, numberOfParts + 2, 2):
                        part = strCounter[i:i + 2]
                        parts.append(part)

                    for i in range(0, len(parts) - 1, 1):
                        if parts[i] != parts[i + 1]:
                            isInvalid = False
                            break
                        else:
                            isInvalid = True
            elif len(strCounter) % 3 == 0 and len(strCounter) > 1 and not isInvalid:
                if len(strCounter) > 5:
                    numberOfParts = int(len(strCounter) / 3)
                    parts = []
                    for i in range(0, numberOfParts + 6, 3):
                        part = strCounter[i:i + 3]
                        parts.append(part)

                    isInvalid = True
                    for i in range(len(parts)-1):
                        if parts[i] != parts[i + 1]:
                            isInvalid = False

            if isInvalid:
                invalidIDs += counter
                invalidIDsList.append(str(counter))
                #print(f"Invalid ID: {counter}")

            counter += 1
    return invalidIDs


def everyNumberAreEqual(strNumber):
    if len(strNumber) > 1:
        for i in range(len(strNumber)-1):
            if strNumber[i] != strNumber[i +1]:
                return False
        return True
    return False


inputs = getInputs("inputs.txt")
print(f"We have {getInvalidIDs(inputs)} invalid IDs")
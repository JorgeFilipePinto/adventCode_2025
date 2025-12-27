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
        counter = int(min)
        
        while counter <= int(max):
            strCounter = str(counter)
            halfSize = len(strCounter) / 2
            isInvalid = False
            
            if len(strCounter) % 2 == 0:
                if strCounter[:int(len(strCounter) / 2)] == strCounter[int(len(strCounter) / 2):]:
                    isInvalid = True
                elif strCounter[:2] == strCounter[len(strCounter) - 2:len(strCounter)] and int(len(strCounter) / 2) > 1:
                    print(f"{strCounter}: {strCounter[:2]} ---->{strCounter[len(strCounter) - 2:len(strCounter)]}")
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
            else:
                for i in range(len(strCounter)-1):
                    if strCounter[i] == strCounter[i + 1]:
                        isInvalid = True
                    else:
                        isInvalid = False
                        break


            if isInvalid:
                invalidIDs += counter
                print(f"Invalid ID: {counter}")
            counter += 1

    return invalidIDs



inputs = getInputs("inputs.txt")
print(f"We have {getInvalidIDs(test)} invalid IDs")

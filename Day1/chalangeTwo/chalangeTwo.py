
#Same chalange but at this time we need count when dial pass in 0

test = [
"L68",
"L30",
"R48",
"L5",
"R60",
"L55",
"L1",
"L99",
"R14",
"L82"
]



def getInputValues(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    return lines

def getCode(instructions):
    dial = 50
    code = 0
    print("Let's find out the door's code")
    
    for instruction in instructions:
        instructionConvertion = int(instruction[1: len(instruction)])
        while instructionConvertion > 0:
            match instruction[0]:
                case 'L':
                    dial -= 1
                    if dial == 0:
                        code += 1
                    elif dial == -1:
                        dial = 99
                case 'R':
                    dial += 1
                    if dial == 100:
                        dial = 0
                        code += 1
            instructionConvertion -= 1
    return code



inputs = getInputValues("instructions.txt")
print(f"The door's code is: {getCode(inputs)}")
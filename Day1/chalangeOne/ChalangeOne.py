#One arrow
#Range of numbers 0..99
#How many 0 have it?

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

def getCodes(intructionsInput):
    vaultIndicator = 50
    _vaultCodes = []
    print("Let's go find the code of vault")
    for instruction in intructionsInput:
        instructionConvertion = int(instruction[1:len(instruction) + 1])
        #print(f"Input convertion: {instructionConvertion}")
        match instruction[0]:
            case 'R':
                #print("Rotate to RIGTH")
                newVaultIndicator = (vaultIndicator + instructionConvertion) % 100
                #print(f"{instruction} -> {newVaultIndicator}")
                vaultIndicator = newVaultIndicator
            case 'L':
                #print("Rotate to LEFT")
                newVaultIndicator = (vaultIndicator - instructionConvertion) % 100
                #print(f"{instruction} -> {newVaultIndicator}")
                vaultIndicator = newVaultIndicator
        _vaultCodes.append(newVaultIndicator)
    return _vaultCodes


def getVaultCode(inputs):
    codes = []
    for i in range(len(inputs)):
        if inputs in codes:
            continue
        code = filter(lambda x: inputs[i] == x, inputs)
        codes.append(list(code))

    for code in codes:
        if 0 in code:
            return len(code)

file = open("instructions.txt")
lines = file.readlines()
file.close()

vaultCodes = getCodes(lines)
print(f"The vault code is: {getVaultCode(vaultCodes)}")

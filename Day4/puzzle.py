import os
import sys
import re

def validateBirthYear(year):
    return 1920 <= int(year) <= 2002

def validateIssueYear(year):
    return 2010 <= int(year) <= 2020

def validateExpYear(year):
    return 2020 <= int(year) <= 2030

def validateHeight(height):
    min = 0
    max = 0
    if (height.endswith("cm")):
        min = 150
        max = 193
    elif (height.endswith("in")):
        min = 59
        max = 76
    else:
        return False

    return (min <= int(height[:-2]) <= max)

def validateHairColor(color):
    return re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color)
    
def validateEyeColor(color):
    validColors = ['amb','blu','brn','gry','grn','hzl','oth']
    return color in validColors

def validatePassportId(id):
    return re.search(r'^\d{9}$', id)

passports = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    inputData = f.read()
    inputData = inputData.split("\n\n")
    inputData = [x.strip() for x in inputData]
    inputData = [x.replace('\n', ' ') for x in inputData]

    for line in inputData:
        passports.append(dict(item.split(":") for item in line.split(" ")))

mandatoryPassportFields = dict([('byr', validateBirthYear), ('iyr', validateIssueYear), ('eyr', validateExpYear), ('hgt', validateHeight), ('hcl', validateHairColor), ('ecl', validateEyeColor),  ('pid', validatePassportId)])
optionalPasswordField = ['cid', ]

validPassportsA = 0
validPassportsB = 0

for passport in passports:
    passportFieldsValid = True
    passportFieldAvailable = True

    for mandatoryField in mandatoryPassportFields.keys():
        if (not mandatoryField in passport):
            passportFieldAvailable = False
        elif(not mandatoryPassportFields[mandatoryField](passport[mandatoryField])):
            passportFieldsValid = False
    
    if (passportFieldAvailable):
        validPassportsA += 1
    
    if (passportFieldAvailable and passportFieldsValid):
        validPassportsB += 1

print("Valid passports A: ", validPassportsA)
print("Valid passports B: ", validPassportsB)
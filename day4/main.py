import time
import re
def puzzel1():
    data=[]
    dataline=""
    validPassports = 0

    fileHandler = open("input.txt")

    listOfLines = fileHandler.readlines()
    for line in listOfLines:
        if line != '\n':
            line = line.replace('\n', " ")
            dataline = dataline + line
        else:
            data.append(dataline)
            dataline=""

    for pasport in data:
        if pasport.__contains__("byr") and pasport.__contains__("iyr") and pasport.__contains__("eyr") and pasport.__contains__("hgt")\
                and pasport.__contains__("hcl") and pasport.__contains__("ecl") and pasport.__contains__("pid"):
            validPassports = validPassports+1

    print("Puzzle 1: The number of correct passports in the dataset are: "f"{validPassports}")


def puzzel2():
    data=[]
    validpplist=[]
    dataline=""
    validPassports = 0
    ecllist= ['amb','blu','brn','gry','grn','hzl','oth']
    fileHandler = open("input.txt")

    listOfLines = fileHandler.readlines()
    for line in listOfLines:
        if line != '\n':
            line = line.replace('\n', " ")
            dataline = dataline + line
        else:
            data.append(dataline)
            dataline=""

    for pasport in data:
        if pasport.__contains__("byr") and pasport.__contains__("iyr") and pasport.__contains__("eyr") and pasport.__contains__("hgt")\
                and pasport.__contains__("hcl") and pasport.__contains__("ecl") and pasport.__contains__("pid"):
            validpplist.append(pasport)


    for passport in validpplist:
        passport=passport[:-1]
        passport = passport.replace(' ', ',')
        mydict = dict((k.strip(), v.strip()) for k, v in
                      (item.split(':') for item in passport.split(',')))
        if 1919 < int(mydict['byr']) < 2003 and len(mydict['byr']) > 3:
            if 2009 < int(mydict['iyr']) < 2021 and len(mydict['iyr']) > 3:
                if 2019 < int(mydict['eyr']) < 2031 and len(mydict['eyr']) > 3:
                    if len(mydict['pid']) == 9:
                        if any(x in mydict['ecl'] for x in ecllist):
                            if re.match('(^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f])', mydict['hcl']):
                                huugte = mydict['hgt']
                                if huugte[-2:] == "in":
                                    huugte = huugte[:-2]
                                    if 58 < int(huugte) < 77:
                                        validPassports = validPassports + 1
                                if huugte[-2:] == "cm":
                                    huugte = huugte[:-2]
                                    if 149 < int(huugte) < 194:
                                        validPassports = validPassports + 1


    print("Puzzle 2: The number of correct passports in the dataset are: "f"{validPassports}")

    return True



if __name__ == '__main__':
    t = time.process_time()
    puzzel1()
    elapsed_time = time.process_time() - t
    print("benchpress69: ",elapsed_time*1000, "milisex")

    t = time.process_time()
    puzzel2()
    elapsed_time = time.process_time() - t
    print("benchpress69: ",elapsed_time*1000, "milisex")


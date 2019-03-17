def addInterestFromMajor(x):
    majors = open('majorintext.txt')
    majorsR = majors.readlines()
    print(majorsR[x-1].split(';')[1])
    return ';' + majorsR[x-1].split(';')[1]

def getMajorName(x):
    majors = open('majorintext.txt')
    majorsR = majors.readlines()
    return majorsR[x-1].split(';')[0]

def findBasedOnInterest():
    print("finding you a club")
    for line in clubtags:
        clubInfo = line.split(',')
        clubName = clubInfo[0]
        clubInterests = clubInfo[1].split(";")
        for c in chosenInterest:
            if c in clubInterests:
                print("JOIN " + clubName)
        if chosenInterest is clubInterests:
            print("Really consider" + clubName)

print("These are the schools at Penn State: \n1 College of Agricultural Sciences\n2 College of Arts and Architecture\n3 Smeal College of Business\n4 Donald P. Bellisario College of Communications\n5 College of Earth and Mineral Sciences\n6 College of Education\n7 College of Engineering\n8 College of Health and Human Development\n9 College of Information Sciences and Technology\n10 College of the Liberal Arts\n11 College of Nursing\n12 Eberly College of Science \n13 Other")
major = input("What is your college? (enter the number only please)")


print("These are the possible interests \n Political \n Greek  \n Medical \n Physical Activity \n Music \n Health \n Math \n Educational \n Business \n Religious \n Cultural \n Agricultural \n LGBT \n Engineering \n Hobby \n Chemistry \n Biology \n Biological \n THON \n Military \n Arts \n Sport \n Tech \n Geoscience \n Community \n Meteorology \n Religion \n Educational \n Education \n Physical Acvitvity \n Musical \n Cultural  \n Cultu \n Politics")

interst = input("What is your field of interest? If you would like to enter in multiple, please seperate them by ';'")
interst += addInterestFromMajor(int(major))
chosenInterest = interst.split(";")
clubtagsIN = open('clubtags.txt')
clubtags = clubtagsIN.readlines()
findBasedOnInterest()

# First the bot will scan for a club that contains both of these values, and if not it will then offer one based off of interst first. Growing over time with the AI


finalSelection = input("What clubs offered have you chosen? (seperated by ; for multiple selections)")
update = open('output.txt',"a")
update.write('\n')
StringOfInterests = ''
update.write(getMajorName(int(major)) + ',' +interst + ',' + finalSelection)




#Week 2 Activity 9: display data
#Name: Tan Jun Wei
#Student ID: S10266704C

#file contents:
# Alan Ang, 81110000
# Bobby Boey, 91231234
# Catherine Chan, 88776655
# Danny Don, 99223344
# Elson Eng, 99101112

path = 'C:\\Users\Admin\Downloads\\'
file = open(path+'StudentData.txt', 'r')
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
line4 = file.readline()
line5 = file.readline()
print(line1, line3, line5, sep="")
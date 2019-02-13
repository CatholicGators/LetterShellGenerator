import csv, sys

if len(sys.argv) != 3:
    print('Usage: python3 %s <team member list> <your name>' % sys.argv[0])
    sys.exit(1)

TO_LIST_FILE_NAME = sys.argv[1]
FROM_NAME = sys.argv[2]

toListFile = open(TO_LIST_FILE_NAME, 'r')
letterShellsFile = open('letterShells.txt', 'w')

reader = csv.reader(toListFile)
for row in reader:
    toName = row[0].split()[0]
    letterShellsFile.write('''mm/dd/yy
Dear %s,



Best regards,
%s

''' % (toName, FROM_NAME))

import csv, sys

if len(sys.argv) != 3:
    print('Usage: python3 %s <team member list> <your name>' % sys.argv[0])
    sys.exit(1)

TEAM_MEMBER_LIST_FILE_NAME = sys.argv[1]
fromName = sys.argv[2]

teamFile = open(TEAM_MEMBER_LIST_FILE_NAME, 'r')
palancaShellsFile = open('palancaShells.txt', 'w')

reader = csv.reader(teamFile)
for row in reader:
    toName = row[0].split()[0]
    palancaShellsFile.write('''mm/dd/yy
Dear %s,



Best regards,
%s

''' % (toName, fromName))

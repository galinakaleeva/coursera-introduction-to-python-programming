inputFile = open('input.txt', 'r', encoding='utf8')


class Participant:
    lastName = ''
    firstName = ''
    someNumber = 0
    mark = 0


def participantkey(participant):
    return(participant.lastName)


participantList = []
tempData = inputFile.readlines()
i = 0
for tempMan in tempData:
    tmp = tempMan.strip().split()
    participant = Participant()
    participant.lastName = tmp[0]
    participant.firstName = tmp[1]
    participant.someNumber = int(tmp[2])
    participant.mark = int(tmp[3])
    participantList.append(participant)
participantList.sort(key=participantkey)
for participant in participantList:
    print(participant.lastName, participant.firstName, participant.mark)

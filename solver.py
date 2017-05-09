fsm = {"St": ["R B","S C"],
       "A": ["B","C"],
       "B": ["E","D"],
       "C": ["F",""],
       "D": ["",""],
       "E": ["G","G"],
       "F": ["",""],
       "G": ["","A"],
       "R": ["R","S"],
       "S": ["S","T"],
       "T": ["T","R"] };

todo = ["St"]
final = {}

while (len(todo) > 0):
    current = todo.pop();
    statesz = set()
    stateso = set()
    for state in current.split(" "):
        for i in fsm[state][0].split(" "):
            if i != '':
                statesz.add(i)
        for i in fsm[state][1].split(" "):
            if i != '':
                stateso.add(i)

    statesz = sorted(statesz);
    statesz = ' '.join(statesz);
    stateso = sorted(stateso);
    stateso = ' '.join(stateso);

    if current not in final:
        final[current] = [[],[]];

    final[current][0] = (statesz);
    if statesz not in final:
        todo.append(statesz);

    final[current][1] = (stateso);
    if stateso not in final:
        todo.append(stateso);

for line in final:
    string = ''
    for blob in final[line][0]:
        string += blob.replace(' ','');
    string += ' ';
    for blob in final[line][1]:
        string += blob.replace(' ','');

    line = line.replace(' ','')
    print(line, '&', string.split(" ")[0], '&', string.split(" ")[1])

import re
from itertools import product
from collections import OrderedDict

def generateTestCases(length):
    for i in range(length):
        for seq in product("01", repeat=i):
            if seq != ():
                yield "".join(seq)

cases = ['1100', '1011','1000']
def checkValid(line):
    regex = re.match(r'^(0001|0011)*(00|01|10)$', line);
    count = line.count('1');

    return count % 3 == 1 and bool(regex);

    #line = ([line[i:i+4] for i in range(0, len(line), 4)])
    #count = 0;
    #for block in line[:-1]:
    #    count += block.count("0")
    #    if block not in cases:
    #        return False
    #if (line == ['0']):
    #    return True
    #if (line == ['1']):
    #    return False
    #if (len(line[-1]) > 1):
    #    return False
    #if (count % 2 == 0):
    #    if (line[-1] == '0'):
    #        return True
    #    return False
    #else:
    #    if (line[-1] == '1'):
    #        return True
    #    return False
    #return False

def iterateState(testCase):
    state = (start, states[start])
    for char in testCase:
        #print(char, state)
        if char == '0':
            state = (state[1][0], states[state[1][0]])
        else:
            state = (state[1][1], states[state[1][1]])
    return state[0]

def printWebForm():
    i = 1;
    seen = OrderedDict()
    seen[list(states.keys())[0]] = 0
    for state in states.values():
        if (state[0] not in seen):
            seen[state[0]] = i
            i+=1
        if (state[1] not in seen):
            seen[state[1]] = i
            i+=1
    print(seen)

    final = []
    for state in states:
        value = states[state]
        #print(seen[state[0]], seen[state[1]])
        final.append((seen[state], seen[value[0]], seen[value[1]]))

    for state in final:
        print(state)
    print()

    for state in sorted(final, key=lambda x: x[0]):
        print(state)
        #print(state[0], '&', state[1], '&', state[2], '& \\\\')
        #print(state[0], '->', state[2], '[label ="1"]')

def reduction():
    equivalent = OrderedDict()
    for state in states:
        equivalent[state] = 0;
        if state in accepting:
            equivalent[state] = 1;

    before = [];
    while (before != list(equivalent.values())):
        before = list(equivalent.values());

        idk = {}
        for state in states:
            value = states[state];
            idk[state] = (equivalent[value[0]], equivalent[value[1]])

        i = 0
        seen = {}
        for state in equivalent:
            blob = (equivalent[state], idk[state][0], idk[state][1])
            if not blob in seen:
                seen[blob] = i
                equivalent[state] = i
                i += 1
            else:
                equivalent[state] = seen[blob]

    print("Equiv")
    for value in equivalent.values():
        print(value)
    print()

f = open("states9.txt")
states = OrderedDict();

start = '0'
accepting = ['3', '14', 'FS', 'DS', 'ES']

for line in f:
    line = line.strip()
    split = re.split(r" +", line)
    states[split[0]] = (split[1], split[2])

import time
for testcase in generateTestCases(16):
    #print(testcase)
    valid = checkValid(testcase)
    state = iterateState(testcase);
    check = state in accepting;

    #print("Check", check);
    #print("State", state);
    #time.sleep(0.5)
    if (valid):
        print("Valid test case:", testcase);

    if (check != valid):
        if (valid):
            print("Didnt pass a valid test case")
        else:
            print("Didnt pass a invalid test case")
        print("State:",state)
        print("Valid:",valid)
        print("Check:",check)
        break

reduction();
printWebForm();

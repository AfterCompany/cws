import sys
from collections import deque
sys.stdin = open('28073.txt','r')


def bfs():
    global edgeInfo, nodeInfo, endCount

    while Q:
        curDistance, curNodeAlphabet, curNodeIndex = Q.popleft()

        if curNodeAlphabet == endAlphabet:
            endCount = curDistance
        
        for edge in edgeInfo[curNodeIndex]:
            nxtNodeIndex, edgeIndex = edge
            
            nxtNodeInfo = nodeInfo[nxtNodeIndex]
            nxtNodeAlphabet, nxtNodeDistance, nxtNodePreAlphabet, nxtNodePreNodeIndex = nxtNodeInfo
            asciiCurNodeAlphabet = ord(curNodeAlphabet)
            

            if nxtNodePreAlphabet == '':
                asciiNxtNodeAlphabet = ord(curNodeAlphabet)
            else:
                asciiNxtNodeAlphabet = ord(nxtNodePreAlphabet)

            if curDistance + 1 > nxtNodeDistance:
                nodeInfo[nxtNodeIndex][1] = curDistance + 1
                nodeInfo[nxtNodeIndex][2] = curNodeAlphabet
                nodeInfo[nxtNodeIndex][3] = curNodeIndex
                if endCount >= curDistance + 1:
                    Q.append([curDistance + 1, nxtNodeAlphabet, nxtNodeIndex])
            elif curDistance + 1 == nxtNodeDistance and asciiCurNodeAlphabet <= asciiNxtNodeAlphabet:
                nodeInfo[nxtNodeIndex][1] = curDistance + 1
                nodeInfo[nxtNodeIndex][2] = curNodeAlphabet
                nodeInfo[nxtNodeIndex][3] = curNodeIndex
                if endCount >= curDistance + 1:
                    Q.append([curDistance + 1, nxtNodeAlphabet, nxtNodeIndex])
            elif nxtNodeDistance == float('inf'):
                nodeInfo[nxtNodeIndex][1] = curDistance + 1
                nodeInfo[nxtNodeIndex][2] = curNodeAlphabet
                nodeInfo[nxtNodeIndex][3] = curNodeIndex
                if endCount >= curDistance + 1:
                    Q.append([curDistance + 1, nxtNodeAlphabet, nxtNodeIndex])

    return

nodeCount, edgeCount = map(int, input().split())
startAlphabet, endAlphabet = map(str, input().split())
nodeAlphabetList = list(input())
edgeInfo = {nodeIndex : [] for nodeIndex in range(nodeCount)}
nodeInfo = {nodeIndex : [nodeAlphabetList[nodeIndex], float('inf'), '', ''] for nodeIndex in range(nodeCount )}
endCount = float('inf')
endCandidateIndex = []

for index in range(len(nodeAlphabetList)):
    alphabet = nodeAlphabetList[index]

    if alphabet == endAlphabet:
        endCandidateIndex.append(index)


# edgeInfo nodeIndex : [nodeIndex와 연결된 node]
# nodeInfo nodeIndex : [자기 알파벳, 거리, 이전 알파벳, 이전 노드]

for edgeIndex in range(edgeCount):
    nodeOne, nodeTwo = map(int, input().split())
    nodeOne -= 1
    nodeTwo -= 1
    edgeInfo[nodeOne].append([nodeTwo, edgeIndex])
    edgeInfo[nodeTwo].append([nodeOne, edgeIndex])

Q = deque()

for nodeIndex in range(nodeCount):
    nodeAlphabet = nodeAlphabetList[nodeIndex]
    if nodeAlphabet == startAlphabet:
        Q.append([0, nodeAlphabet, nodeIndex])

bfs()

answerEndPosition = float('inf')
answerEndAlphabet = float('inf')

for index in endCandidateIndex:
    distance = nodeInfo[index][1]
    alphabet = nodeInfo[index][2]

    if answerEndAlphabet == float('inf'):
        answerEndAlphabet = 

    if answerEndPosition > distance:
        answerEndPosition = distance
        
    if answerEndPosition == distance and answerEndAlphabet > ord(alphabet):


if endCount != float('inf'):
    answer = ''
else:
    print('Aaak!')


# SPDDDD CCK
# SPCCCC CCK

# 예외케이스가 존재함
# 길이도 동일하고, 알파벳 순서가 중간에 다른경우에 대한 체크 로직 추가가 필요함

# 끝 후보 리스트 전부 찾고, 거기서 부터 뒤로돌리는 모든거 체크 => 이 중에 답을 표현
# 귀찮아서 아직 안하는 중 => 시간나면 수정하여 채점하기
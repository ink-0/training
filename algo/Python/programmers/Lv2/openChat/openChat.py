def solution(record):
    enterLeaveLst = []
    idNickLst={}
    enterLeaveLst=[]
    answer=[]
    for r in record:
        
        k=list(map(str,r.split()))

        if k[0] == 'Enter':
            idNickLst[k[1]]=k[2]
            enterLeaveLst.append([k[0],k[1]])
            
        elif k[0] == 'Change':
            idNickLst[k[1]]=k[2]
        else :
            enterLeaveLst.append([k[0],k[1]])
    
    for a in enterLeaveLst:
        if a[0] == 'Enter':
            answer.append(idNickLst[a[1]]+'님이 들어왔습니다.')
            
        else:
            answer.append(idNickLst[a[1]]+'님이 나갔습니다.')

    return answer

            




    
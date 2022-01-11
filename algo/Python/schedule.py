def solution(schedule):
    ansArr=[]
    # 두개 스케줄인지 확인
    def isTwoSchedule(sche):
        if(len(sche)>8):
             return True
        else:
             return False

    def divideTwoSche(sche):
        arr = sche.split(' ')
        return [[arr[0],arr[1]],[arr[2],arr[3]]]


    # 스케줄 두개를 1:1로 비교해 겹치는지 확인
    def isOverlap(s1,s2):
        daytime1 = s1.split(' ')
        daytime2= s2.split(' ')
        if(daytime1[0]!= daytime2[0]):
            return 0
        else:
            return 1
    
    def checkOverlapinLoop(subjectIdx,sche):
        for idx,daySchedule in enumerate(schedule):
            if(idx!= subjectIdx):
                for sclass in daySchedule:
                    print(sche,sclass)
                    print(isOverlap(sche,sclass))
                    return isOverlap(sche,sclass)





    for idx,daySchedule in enumerate(schedule):
        print(idx)
        # print(daySchedule)
        cnt=0
        for sclass in daySchedule:
            print(checkOverlapinLoop(idx,sclass))
            cnt+=checkOverlapinLoop(idx,sclass)
        ansArr.append(cnt)
    print(ansArr)
          



import pandas as pd
from datetime import datetime, timedelta, time

import dijkstra as di
import loader as ld


temp = ld.DfLine1_upper.loc[0]


ListLine1 = []
ListLine2 = []
ListLine3 = [] 
ListTrans = []

for x in ld.DfLine1_lower["역명"] :
    ListLine1.append(x)

for x in ld.DfLine2_lower["역명"] :
    ListLine2.append(x)

for x in ld.DfLine3_lower["역명"] :
    ListLine3.append(x)

for station in ListLine1 :
    if station in ListLine2 :
        ListTrans.append(station)
    elif station in ListLine3 :
        ListTrans.append(station)
for station in ListLine2 :
    if station in ListLine3 :
        ListTrans.append(station)

ListLines = [ListLine1,ListLine2,ListLine3]

def checkupdown(start, end, listline) :
    
    if start in listline and end in listline :
        return listline.index(start) - listline.index(end)
    #리턴 값이 음수면 하행 양수면 상행
    return 0


def getdeparttime(depart, destin):
    departtime = None
    currenttime = datetime.now().time().strftime("%H:%M")

    fmt = "%H:%M"
    fmts = "%H:%M:%S"

    if destin == "없음":
        destin = StrDestin

    for i, listline in enumerate(ListLines):
        if checkupdown(depart, destin, listline) < 0:
            for index, t in enumerate(ld.DFLines_lower[i].iloc[listline.index(depart)]):
                if index > 3 and pd.notna(t):
                    t1 = datetime.strptime(currenttime, fmt)
                    t2 = datetime.strptime(str(t), fmts)
                    if t1 < t2:
                        departtime = t2
                        break
        elif checkupdown(depart, destin, listline) > 0:
            for index, t in enumerate(ld.DfLines_upper[i].iloc[-(listline.index(depart)+1)]):
                if index > 3 and pd.notna(t):
                    t1 = datetime.strptime(currenttime, fmt)
                    t2 = datetime.strptime(str(t), fmts)
                    if t1 < t2:
                        departtime = t2
                        break

    # ✅ 보정: 아무 것도 못 찾았을 경우 현재 시각을 기본값으로 사용
    if departtime is None:
        print("[WARN] 출발 시간을 찾을 수 없어 현재 시각 사용")
        departtime = datetime.now()

    return departtime.time()




def transfer(routes) :
    first = "없음"
    last = "없음"
    count = 0

    listindexs = [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]

    for index, station in enumerate(routes) :
        if station in ListTrans and index > 0 and index < len(routes)-1:
            for listindex in listindexs:
                if routes[index-1] in ListLines[listindex[0]] and routes[index+1] in ListLines[listindex[1]] and not routes[index+1] in ListTrans:
                    if count == 0 :
                        first = station
                        last = station
                    last = station
                    count += 1
    return first, last

StrDepart = "다사" # input으로 입력받아서 할 예정
StrDestin = "교대" # input으로 입력받아서 할 예정

firsttransfer = ""
lasttransfer = ""


#arrivaltime = currenttime + timedelta(minutes=DictDistance[StrDestin])


from datetime import datetime, timedelta, time

def compute_route_info(depart, destin):
    dist, prev = di.dijkstra(ld.DictInterval_data, depart)
    route = di.routes(prev, destin)
    first_tr, last_tr = transfer(route)

    # 출발 시간 가져오기
    depart_time = getdeparttime(depart, first_tr or depart)

    # ✅ 타입이 int라면 time 객체로 변환
    if isinstance(depart_time, int):
        # 정수라면 시(hour)만 입력되었다고 가정
        depart_time = time(hour=depart_time, minute=0)
    elif isinstance(depart_time, str):
        # 혹시 문자열로 반환되었다면 예: '08:10' → time으로 파싱
        h, m = map(int, depart_time.split(":"))
        depart_time = time(hour=h, minute=m)

    # 도착 시간 계산
    arrive_time = (datetime.combine(datetime.now(), depart_time) + timedelta(minutes=dist[destin])).time()

    return {
        'route': route,
        'distance': dist[destin],
        'first_transfer': first_tr,
        'last_transfer': last_tr,
        'depart_time': depart_time,
        'arrival_time': arrive_time
    }

import tkinter as tk
from tkinter import ttk
from collections import deque
from test_style2 import *

def show_coords(event):
    print(f"Mouse at ({event.x}, {event.y})")

selected_start = None
selected_end = None

def on_station_click(event):
    global selected_start, selected_end
    clicked = c.find_withtag("current") #마우스 클릭 -> 해당 리스트를 변수에 저장
    if not clicked:
        return
    tags = c.gettags(clicked[0])
    if len(tags) < 2: #역 이름이 2개 이상
        return
    station_name = tags[1]

    if selected_start is None:
        selected_start = station_name
        print(f"Start selected: {selected_start}")
    elif selected_end is None:
        if station_name == selected_start:
            print("출발지와 도착지가 같을 수 없습니다.")
            return
        selected_end = station_name
        print(f"End selected: {selected_end}")

        draw_highlight_path(selected_start, selected_end)

        #상태 초기화
        selected_start = None 
        selected_end = None

def find_path(start,end):
    visited = set() #이미 방문한 역들 저장. 중복 탐색 막아줌
    queue = deque([[start]])

    while queue:
        path = queue.popleft() #큐에서 하나의 경로 꺼내기
        node = path[-1] #현재 마지막 위치한 역 가져오기

        if node == end:
            return path #도착역이면 지금까지 온 경로 반환
        
        if node not in visited:
            visited.add(node)  #방문 안 했을시 현재역을 방문 목록에 추가

            for a,b in edges:
                #b가 방문을 안 했다면 path+[b]로 현재 경로 뒤에 추가
                if a==node and b not in visited:
                    queue.append(path+[b])
                elif b==node and a not in visited:
                    queue.append(path+[a])


#선택한 역에 빨간원, 금색 경로
def draw_highlight_path(start,end):
    print(f"Highlight path from {start} to {end}")

    # 기존 경로 제거
    c.delete("highlight")


    path = find_path(start, end)
    if not path:
        print("경로 없음")
        return

    # 경로 선 그리기
    for i in range(len(path)-1):
        a, b = path[i], path[i+1]
        x1, y1 = stations[a]
        x2, y2 = stations[b]
        c.create_line(x1, y1, x2, y2, fill="gold", width=6, tags="highlight")

   
    for station in [start, end]:
        x,y = stations[station]
        c.create_oval(x-6,y-6,x+6,y+6, fill="red",outline="black", tags="highlight")

def on_find_route():
    start = start_var.get()
    end = end_var.get()
    if start not in stations or end not in stations or start == end:
        result_var.set("올바른 출발지/도착지를 선택하세요.")
        return
    
    path = find_path(start,end)
    if not path:
        result_var.set("경로를 찾을 수 없습니다.")
        c.delete("highlight")
        return
    draw_highlight_path(start,end)
    result_var.set(" → ".join(path))

# 역 좌표
stations_1 = {
    "설화명곡": (157, 127),
    "화원": (157, 157),
    "대곡": (157, 187),
    "진천": (157, 217),
    "월배": (158, 247),
    "상인": (168, 277),
    "월촌": (190, 285),
    "송현": (220, 292),

    "서부정류장": (255, 298),
    "대명": (297, 298),
    "안자랑": (337, 298),
    "현충로": (384, 298),
    "영대병원": (430, 298),
    "교대": (477, 298),
    "명덕": (520, 260),

    "반월당": (563, 299),
    "중앙로": (563, 376),
    "대구역": (563, 406),
    "칠성시장": (563, 436),
    "신천": (569, 466),
    "동대구역": (587, 490),

    "동구청": (605, 513),
    "아양교": (640, 513),
    "동촌": (680, 513),
    "해안": (720, 513),
    "방촌": (753, 513),
    "용계": (787, 513),

    "율하": (823, 523),
    "신기": (847, 533),
    "반야월": (865, 565),
    "각산": (872, 595),
    "안심": (872, 625),
    "대구한의대병원": (872, 655),
    "부호": (872, 685),
    "하양": (872, 715),
}

stations_2 = {
    "문양": (13, 209),
    "다사": (13, 239),
    "대실": (13, 269),
    "강창": (13, 299),

    "계명대": (53, 299),
    "성서산업단지": (113, 299),
    "이곡": (163, 299),
    "용산": (213, 299),
    "죽전": (263, 299),
    "감삼": (313, 299),
    "두류": (363, 299),
    "내당": (413, 299),
    "반고개": (463, 299),
    "청라언덕": (513, 299),
    "반월당": (563, 299),
    "경대병원": (613, 299),
    "대구은행": (663, 299),
    "범어": (713, 299),
    "수성구청": (763, 299),
    "만촌": (813, 299),
    "담티": (863, 299),
    "연호": (913, 299),

    "수성알파시티": (953, 329),
    "고산": (953, 359),
    "신매": (953, 389),
    "사월": (953, 419),
    "정평": (953, 449),
    "임당": (953, 479),
    "영남대": (953, 509),
}
stations_3 = {
   "용지": (870, 90),
    "범물": (870, 120),
    "지산": (870, 150),
    "수성못": (870, 180),
    "황금": (850, 210),
    "어린이세상": (800, 235),
    "수성구민운동장": (750, 253),
    "수성시장": (700, 253),

    "대봉교": (650, 253),
    "건들바위": (585, 255),
    "명덕": (520, 260),          # 고정

    "남산": (516, 285),
    "청라언덕": (513, 299),       # 고정
    "서문시장": (513, 360),
    "달성공원": (513, 390),
    "북구청": (510, 420),
    "원대": (490, 450),
    "팔달시장": (460, 470),
    "만평": (420, 470),
    "공단": (380, 470),
    "팔달": (340, 470),
    "매천시장": (300, 470),
    "매천": (260, 470),
    "태전": (220, 470),
    "구암": (180, 490),
    "칠곡운암": (165, 530),
    "동천": (155, 570),
    "팔거": (155, 600),
    "학정": (155, 630),
    "칠곡경대병원": (155, 660),
}



# 연결리스트
edges_1 = [
    (a, b) for a, b in zip(list(stations_1), list(stations_1)[1:])
]

edges_2 = [
    (a, b) for a, b in zip(list(stations_2), list(stations_2)[1:])
]

edges_3 = [
    (a, b) for a, b in zip(list(stations_3), list(stations_3)[1:])
]

stations_1_shifted = {
    name: (x, y - 40) for name, (x, y) in stations_1.items()
}


# 모든 역 좌표 병합
stations = {}
stations.update(stations_1_shifted)
stations.update(stations_2)
stations.update(stations_3)

# 모든 연결 병합
edges = edges_1 + edges_2 + edges_3
edges += [(b, a) for a, b in edges] 

root = tk.Tk()
root.geometry("1200x850")

apply_styles()

c = tk.Canvas(root, width=1100, height=700, bg="white")
c.pack()

# 기본 노선
for a,b in edges_1:
    x1,y1 = stations[a]; x2,y2 = stations[b]
    c.create_line(x1,y1,x2,y2, fill="#F8064A",width=3)

for a, b in edges_2:
    x1, y1 = stations[a]
    x2, y2 = stations[b]
    c.create_line(x1, y1, x2, y2, fill="#2ED5AE", width=3)

for a, b in edges_3:
    x1, y1 = stations[a]
    x2, y2 = stations[b]
    c.create_line(x1, y1, x2, y2, fill="#FFD700", width=3)

for name, (x,y) in stations.items():
    color = "white"  # 기본 흰색
    c.create_oval(x-6,y-6,x+6,y+6, fill=color,outline="black", tags=("station",name))
    c.create_text(x,y-12, text=name, font=("Arial",8))

c.tag_bind("station","<Button-1>", on_station_click)

#입력 박스
frame = tk.Frame(root)
frame.pack(pady=10)

start_var = tk.StringVar()
end_var = tk.StringVar()
result_var = tk.StringVar()

ttk.Label(frame, text="출발지:").grid(row=0, column=0)
ttk.Combobox(frame, textvariable=start_var, values=list(stations.keys()), width=15, font=("Arial", 12)).grid(row=0, column=1, padx=10)

ttk.Label(frame, text="도착지:").grid(row=0, column=2)
ttk.Combobox(frame, textvariable=end_var, values=list(stations.keys()), width=15,font=("Arial", 12)).grid(row=0, column=3, padx=10)

ttk.Button(frame, text="경로 찾기", command=on_find_route).grid(row=0, column=4, padx=10)

tk.Label(root, textvariable=result_var, font=("Arial", 14), fg="black").pack(pady=10)


root.mainloop()


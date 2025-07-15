import ttkbootstrap as tb
import tkinter as tk
from tkinter import ttk
from collections import deque #최단 경로 찾기용
from main import compute_route_info, checkupdown, ListLine1, ListLine2, ListLine3


def show_coords(event):
    print(f"Mouse at ({event.x}, {event.y})")

StrStart_sty = None
StrEnd_sty = None
start_circle = None
end_circle = None
detail_expanded = False

root = tb.Window(themename="flatly")
root.geometry("1200x1080")
select_mode = tk.StringVar(value="none")

c = tk.Canvas(root, width=1100, height=700, bg="white")
c.pack()

def on_station_click(event): #클릭 이벤트
    global StrStart_sty, StrEnd_sty, start_circle, end_circle
    clicked = c.find_withtag("current") #마우스 클릭 -> 해당 리스트를 변수에 저장

    if not clicked:
        return
    
    tags = c.gettags(clicked[0])

    if len(tags) < 2: #역 이름이 2개 이상
        return
    
    station_name = tags[1]

    if StrStart_sty is None:
    # 이전 경로, 원 등 초기화
        c.delete("highlight")
        if start_circle:
            c.delete(start_circle)
            start_circle = None
        if end_circle:
            c.delete(end_circle)
            end_circle = None

        StrStart_sty = station_name
        x, y = stations[station_name]

        start_circle = c.create_oval(x - 6, y - 6, x + 6, y + 6, fill="red", outline="black")
        start_var.set(station_name)
        print(f"Start selected: {StrStart_sty}")


    elif StrEnd_sty is None:
        if station_name == StrStart_sty:
            print("출발지와 도착지가 같을 수 없습니다.")
            return
        StrEnd_sty = station_name
        print(f"End selected: {StrEnd_sty}")  # 여기 추가
        x,y = stations[station_name]

        if end_circle:
            c.delete(end_circle) 

        end_circle = c.create_oval(x-6, y-6, x+6, y+6, fill="red", outline="black")
        end_var.set(station_name)
    
        show_route_and_info(StrStart_sty,StrEnd_sty)

        select_mode.set("none")

def draw_highlight_path(start, end):
    c.delete("highlight")

    try:
        path = compute_route_info(start, end)["route"]
    except:
        print("경로 없음")
        return

    # 하이라이트 라인 그리기
    for i in range(len(path) - 1):
        a, b = path[i], path[i + 1]
        x1, y1 = stations[a]
        x2, y2 = stations[b]
        c.create_line(x1, y1, x2, y2, fill="blue", width=6, tags="highlight")

    for station in path:
        x, y = stations[station]
        c.create_oval(x-6, y-6, x+6, y+6, fill="red", outline="black", tags="highlight")

#def find_path(start,end):
    #visited = set() #이미 방문한 역들 저장.
    #queue = deque([[start]]) #지금까지의 경로들을 저장

    #while queue:
        #path = queue.popleft() #큐에서 하나의 경로 꺼내기
        #node = path[-1] #현재 마지막 위치한 역 가져오기

        #if node == end:
            #return path #도착역이면 지금까지 온 경로 반환
        
        #if node not in visited:
            #visited.add(node)  #방문 안 했을시 현재역을 방문 목록에 추가

        #for a,b in edges:
                #b가 방문을 안 했다면 path+[b]로 현재 경로 뒤에 추가
                #if a==node and b not in visited:
                    #queue.append(path+[b])
                #elif b==node and a not in visited:
                    #queue.append(path+[a])

def show_station_list(mode):
    select_mode.set(mode)
    if mode == "start":
        start_btn.config(state="normal", bootstyle="secondary-outline")
        end_btn.config(state="normal", bootstyle="info-outline")
    else:
        end_btn.config(state="normal", bootstyle="secondary-outline")
        start_btn.config(state="normal", bootstyle="info-outline")

    station_listbox_frame.pack(pady=5)

    # 결과창 숨기기
    result_text.pack_forget()
    detail_btn.pack_forget()


def on_station_select(event):
    try:
        widget = event.widget
        selection = widget.curselection()
        if not selection:
            return
        selected = widget.get(selection[0])
    except:
        return

    if select_mode.get() == "start":
        start_var.set(selected)
        start_btn.config(text=selected)
        clear_path_result()  # ← 추가!
    elif select_mode.get() == "end":
        end_var.set(selected)
        end_btn.config(text=selected)
        clear_path_result()  # ← 추가!


    station_listbox_frame.pack_forget()
    select_mode.set("none")


#선택한 역에 빨간원, 금색 경로
def draw_highlight_path(start, end):
    print(f"Highlight path from {start} to {end}")
    c.delete("highlight")  # 기존 하이라이트 제거

    try:
        path = compute_route_info(start, end)["route"]
    except Exception as e:
        print("경로 없음:", e)
        return

    # 경로 선 그리기
    for i in range(len(path) - 1):
        a, b = path[i], path[i + 1]
        if a not in stations or b not in stations:
            continue
        x1, y1 = stations[a]
        x2, y2 = stations[b]
        c.create_line(x1, y1, x2, y2, fill="blue", width=6, tags="highlight")

    # 경로상 역에 빨간 원 그리기
    for station in path:
        if station not in stations:
            continue
        x, y = stations[station]
        c.create_oval(x - 6, y - 6, x + 6, y + 6, fill="red", outline="black", tags="highlight")



#입력 방식으로 경로찾기
def on_find_route():
    global StrStart_sty, StrEnd_sty, start_circle, end_circle
    start = start_var.get()
    end = end_var.get()

    print(f"[DEBUG] on_find_route 호출: start={start}, end={end}")

    if start not in stations:
        print(f"[ERROR] 출발역 '{start}'가 좌표 목록에 없음")
        result_var.set("출발역이 잘못되었습니다.")
        return
    if end not in stations:
        print(f"[ERROR] 도착역 '{end}'가 좌표 목록에 없음")
        result_var.set("도착역이 잘못되었습니다.")
        return
    if start == end:
        print("[ERROR] 출발역과 도착역이 같음")
        result_var.set("출발역과 도착역이 같을 수 없습니다.")
        return

    # 상태 초기화
    StrStart_sty = None
    StrEnd_sty = None
    if start_circle:
        c.delete(start_circle)
        start_circle = None
    if end_circle:
        c.delete(end_circle)
        end_circle = None
    c.delete("highlight")

    # 경로 정보 및 지도 표시
    try:
        show_route_and_info(start, end)
    except Exception as e:
        print(f"[ERROR] show_route_and_info 호출 중 예외 발생: {e}")


def format_time(t):
    if isinstance(t, int):
        h = t // 100
        m = t % 100
        return f"{h:02d}:{m:02d}"
    return str(t)

def show_route_and_info(start, end):
    global StrStart_sty, StrEnd_sty, start_circle, end_circle, detail_expanded
    
    print(f"[DEBUG] show_route_and_info 호출: {start} -> {end}")
    
    if start_circle:
        c.delete(start_circle)
        start_circle = None
    if end_circle:
        c.delete(end_circle)
        end_circle = None
    c.delete("highlight")

    StrStart_sty = start
    StrEnd_sty = end
    detail_expanded = False

    try:
        info = compute_route_info(start, end)
        print(f"[DEBUG] compute_route_info 결과: {info}")

        route_str = f"{start} → {end}"
        distance_str = f"⏱ 소요 시간: {info['distance']}분"
        time_str = f"🕒 출발: {info['depart_time'].strftime('%H:%M:%S')}    도착: {info['arrival_time'].strftime('%H:%M:%S')}"

        first_tr = info['first_transfer']
        transfer_info = "🔁 환승 역: 없음"
        if first_tr != "없음":
            direction = ""
            for line in ListLine1 + ListLine2 + ListLine3:
                dir_value = checkupdown(first_tr, end, line)
                if dir_value != 0:
                    direction = "하행" if dir_value < 0 else "상행"
                    break
            transfer_info = f"🔁 환승 역: {first_tr}역에서 {direction} 열차로 환승"

        result = f"🚉 {route_str}\n\n{distance_str}\n{time_str}\n{transfer_info}"

        result_text.configure(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result,"center")
        result_text.configure(state="disabled")

        result_text.pack(pady=10, fill="x", padx=20)
        detail_btn.pack()
        detail_btn.config(text="경로 보기 ▼")

        draw_highlight_path(start, end)

    except Exception as e:
        print(f"[ERROR] show_route_and_info 예외 발생: {e}")
        result_text.configure(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "❌ 경로를 찾을 수 없습니다.", "center")
        result_text.configure(state="disabled")
        result_text.pack(pady=10, fill="x", padx=20)
        c.delete("highlight")


def toggle_detail():
    global detail_expanded
    if not StrStart_sty or not StrEnd_sty:
        return

    info = compute_route_info(StrStart_sty, StrEnd_sty)
    route = info["route"]

    if not detail_expanded:
        route_str = " → ".join(route)
        result_text.configure(state="normal")
        result_text.insert(tk.END, f"\n\n📍 전체 경로:\n{route_str}", "center")
        result_text.configure(state="disabled")
        detail_btn.config(text="간단히 보기 ▲")
        detail_expanded = True
    else:
        show_route_and_info(StrStart_sty, StrEnd_sty)


# 역 좌표
Dict_stations_1 = {
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
    "안지랑": (337, 298),
    "현충로": (384, 298),
    "영대병원": (430, 298),
    "교대": (477, 298),
    "명덕": (540, 260),

    "반월당": (563, 299),
    "중앙로": (563, 400),
    "대구역": (563, 436),
    "칠성시장": (563, 466),
    "신천": (569, 496),
    "동대구역": (577, 525),

    "동구청": (615, 540),
    "아양교": (655, 540),
    "동촌": (695, 540),
    "해안": (735, 540),
    "방촌": (775, 540),
    "용계": (815, 540),

    "율하": (850, 545),
    "신기": (870, 570),
    "반야월": (875, 600),
    "각산": (875, 630),
    "안심": (875, 660),
    "대구한의대병원": (875, 690),
    "부호": (875, 720),
    "하양": (875, 750),
}

Dict_stations_2 = {
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
    "청라언덕": (513, 309),
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
Dict_stations_3 = {
   "용지": (870, 90),
    "범물": (870, 120),
    "지산": (870, 150),
    "수성못": (870, 180),
    "황금": (850, 210),
    "어린이세상": (820, 235),
    "수성구민운동장": (765, 253),
    "수성시장": (700, 253),

    "대봉교": (650, 253),
    "건들바위": (585, 255),
    "명덕": (540, 260),          # 고정

    "남산": (516, 275),
    "청라언덕": (513, 309),       # 고정
    "서문시장": (513, 350),
    "달성공원": (513, 385),
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
    "팔거": (155, 610),
    "학정": (155, 650),
    "칠곡경대병원": (155, 690),
}


# 연결리스트
edges_1 = [
    (a, b) for a, b in zip(list(Dict_stations_1), list(Dict_stations_1)[1:])
]

edges_2 = [
    (a, b) for a, b in zip(list(Dict_stations_2), list(Dict_stations_2)[1:])
]

edges_3 = [
    (a, b) for a, b in zip(list(Dict_stations_3), list(Dict_stations_3)[1:]) 
]

Dict_stations_1_shifted = {
    name: (x, y - 60) for name, (x, y) in Dict_stations_1.items()
}
Dict_stations_2_shifted = {
    name: (x, y + 10) for name, (x, y) in Dict_stations_2.items()
}
# stations_3_shifted = {
#     name: (x, y + 10) for name, (x, y) in stations_3.items()
# }


# 모든 역 좌표 병합
stations = {}
stations.update(Dict_stations_1_shifted)
stations.update(Dict_stations_2_shifted)
stations.update(Dict_stations_3)

#좌표 이동
shift_x = 80
shift_y = -15
stations = {
    name: (x + shift_x, y + shift_y)
    for name, (x, y) in stations.items()
}

# 모든 연결 병합
edges = edges_1 + edges_2 + edges_3
edges += [(b, a) for a, b in edges] #역순 연결 추가(양방향)

edges += [
    ("반월당", "청라언덕"), ("청라언덕", "반월당"),   #환승 역들만 경로 추가로 지정
    ("청라언덕", "남산"), ("남산", "청라언덕"),  
    ("남산","명덕"), ("명덕","남산"),      
    ("명덕", "반월당"), ("반월당", "명덕")          
]

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
    c.create_oval(x-6,y-6,x+6,y+6, fill="white", outline="black", tags=("station", name))
    c.create_text(x,y-12, text=name, font=("Arial",8))

c.tag_bind("station","<Button-1>", on_station_click)


#입력 박스
frame = tb.Frame(root)
frame.pack(pady=35)

start_var = tk.StringVar()
end_var = tk.StringVar()
result_var = tk.StringVar()

start_btn = tb.Button(frame, textvariable=start_var, bootstyle="info-outline", command=lambda: show_station_list("start"), width=15)
start_var.set("출발역 선택")
start_btn.grid(row=0, column=0, padx=10)

end_btn = tb.Button(frame, textvariable=end_var, bootstyle="info-outline", command=lambda: show_station_list("end"), width=15)
end_var.set("도착역 선택")
end_btn.grid(row=0, column=1, padx=10)

tb.Button(frame, text="경로 찾기", command=on_find_route, bootstyle="primary").grid(row=0, column=2, padx=10)

# 기존 result_label 제거

# 기존 pack 제거
# result_text.pack(pady=10, fill="x", padx=20)
# detail_btn.pack()

# 대신 .pack_forget() 상태로 시작
result_text = tk.Text(root, height=8, width=60, font=("Arial", 12), wrap="word", background="#f0f8ff", borderwidth=0, highlightthickness=0)
result_text.tag_configure("center", justify="center")  # 중앙 정렬 태그 정의
result_text.configure(state="disabled")
result_text.pack_forget()  # 처음에는 숨김

detail_btn = tb.Button(root, text="상세 보기 ▼", bootstyle="secondary-outline", command=lambda: toggle_detail())
detail_btn.pack_forget()  # 처음에는 숨김

station_listbox_frame = ttk.Frame(root)
station_listbox_frame.pack_forget()

def clear_path_result():
    result_var.set("")     # 결과 라벨 초기화
    c.delete("highlight")  # 지도 위 경로선 제거

def create_station_tabs(parent):
    notebook = ttk.Notebook(parent)
    notebook.pack(fill="both", expand=True)
    lines = [
        ("1호선", Dict_stations_1),
        ("2호선", Dict_stations_2),
        ("3호선", Dict_stations_3),
    ]
    for line_name, station_dict in lines:
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=line_name)
        listbox = tk.Listbox(frame, width=30, height=10, font=("마란고딕", 13))
        listbox.pack(fill="both", expand=True)
        for station_name in station_dict.keys():
            listbox.insert(tk.END, station_name)
        listbox.bind("<<ListboxSelect>>", on_station_select)
    return notebook

notebook = create_station_tabs(station_listbox_frame)
#print(list(Dict_stations_1))

root.mainloop()

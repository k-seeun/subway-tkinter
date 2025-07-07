import tkinter as tk
from tkinter import ttk

# 0. 역 좌표 정의 (최상단에 있어야 함)
stations = {
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
    "명덕": (522, 298),

    "반월당": (563, 330),
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

# 1호선 연결 정보 (stations 순서대로 선을 연결)
edges_1 = [(a, b) for a, b in zip(list(stations), list(stations)[1:])]

def update_route():
    start = start_var.get()
    end = end_var.get()
    if start not in stations or end not in stations:
        print("역을 올바르게 선택하세요.")
        return
    highlight_route(start, end)

def highlight_route(start, end):
    x1, y1 = stations[start]
    x2, y2 = stations[end]
    canvas.create_line(x1, y1, x2, y2, fill="gold", width=6)
    canvas.create_oval(x1-8, y1-8, x1+8, y1+8, fill="gold", outline="black")
    canvas.create_oval(x2-8, y2-8, x2+8, y2+8, fill="gold", outline="black")

# 1. 기본 UI 구성
root = tk.Tk()
root.geometry("1000x700")

frame = tk.Frame(root)
frame.pack(pady=10)

start_var = tk.StringVar()
end_var = tk.StringVar()

tk.Label(frame, text="출발지:").grid(row=0, column=0)
ttk.Combobox(frame, textvariable=start_var, values=list(stations.keys())).grid(row=0, column=1, padx=10)

tk.Label(frame, text="도착지:").grid(row=0, column=2)
ttk.Combobox(frame, textvariable=end_var, values=list(stations.keys())).grid(row=0, column=3, padx=10)

tk.Button(frame, text="경로 찾기", command=update_route).grid(row=0, column=4, padx=10)

# 2. 지하철 캔버스
canvas = tk.Canvas(root, width=1000, height=800, bg="white")
canvas.pack()

# 캔버스에 빨간 선 그리기
for a, b in edges_1:
    x1, y1 = stations[a]
    x2, y2 = stations[b]
    canvas.create_line(x1, y1, x2, y2, fill="#F8064A", width=3)


for name, (x, y) in stations.items():
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="white", outline="black")
    canvas.create_text(x, y - 10, text=name, font=("Arial", 9))

root.mainloop()

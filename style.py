import tkinter as tk
from PIL import Image, ImageTk

def show_coords(event):
    print(f"Mouse at ({event.x}, {event.y})")

#image = Image.open("D:\자료\Desktop\노선도.webp")

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
    "명덕": (522, 298),

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
# stations_3 = {
#    "용지": (887, 127),
#     "범물": (887, 157),
#     "지산": (887, 187),
#     "수성못": (887, 217),
#     "황금": (880, 247),
#     "어린이세상": (870, 277),
#     "수성구민운동장": (855, 295),
#     "수성시장": (835, 310),

#     "대봉교": (785, 298),
#     "건들바위": (740, 298),
#     "명덕": (522, 310),          # 고정

#     "남산": (485, 330),
#     "청라언덕": (663, 299),       # 고정
#     "서문시장": (650, 350),
#     "달성공원": (640, 390),
#     "북구청": (620, 430),
#     "원대": (590, 460),
#     "팔달시장": (570, 480),
#     "만평": (540, 500),
#     "공단": (520, 520),
#     "팔달": (490, 530),
#     "매천시장": (460, 530),
#     "매천": (430, 530),
#     "태전": (400, 530),
#     "구암": (370, 535),
#     "칠곡운암": (340, 540),
#     "동천": (310, 550),
#     "팔거": (280, 580),
#     "학정": (270, 600),
#     "칠곡경대병원": (260, 630),
# }



# 연결리스트
edges_1 = [
    (a, b) for a, b in zip(list(stations_1), list(stations_1)[1:])
]

edges_2 = [
    (a, b) for a, b in zip(list(stations_2), list(stations_2)[1:])
]

# edges_3 = [
#     (a, b) for a, b in zip(list(stations_3), list(stations_3)[1:])
# ]

stations_1_shifted = {
    name: (x, y - 40) for name, (x, y) in stations_1.items()
}


# 모든 역 좌표 병합
stations = {}
stations.update(stations_1_shifted)
stations.update(stations_2)
#stations.update(stations_3)

# 모든 연결 병합
edges = edges_1 + edges_2 #+ edges_3

# 사용자 선택
highlight = ["문양","경대병원",]

root = tk.Tk()
root.geometry("1200x700")


c = tk.Canvas(root, width=1200, height=700, bg="white")
c.pack()
# new_width = 800
# new_height = 500
# image = image.resize((new_width, new_height))

# # 2. 리사이즈된 이미지로 PhotoImage 생성
# photo = ImageTk.PhotoImage(image)

# canvas_width = 1000
# canvas_height = 600
# canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
# canvas.pack()

# # 3. 캔버스 하단 중앙에 이미지 배치
# c.create_image(canvas_width // 2, canvas_height, anchor=tk.S, image=photo)

# # 4. 이미지 참조 유지
# c.image = photo

# 기본 노선
for a,b in edges_1:
    x1,y1 = stations[a]; x2,y2 = stations[b]
    c.create_line(x1,y1,x2,y2, fill="#F8064A",width=3)

for a, b in edges_2:
    x1, y1 = stations[a]
    x2, y2 = stations[b]
    c.create_line(x1, y1, x2, y2, fill="#2ED5AE", width=3)

# for a, b in edges_3:
#     x1, y1 = stations[a]
#     x2, y2 = stations[b]
#     c.create_line(x1, y1, x2, y2, fill="#FFD700", width=3)

# 선택된 노선 - 굵은 금색
for i in range(len(highlight)-1):
    a,b = highlight[i], highlight[i+1]
    x1,y1 = stations[a]; x2,y2 = stations[b]
    c.create_line(x1,y1,x2,y2, fill="gold",width=6)

# 선택된 역은 빨간 원 아니면 흰 원
for name, (x,y) in stations.items():
    color = "gold" if name in highlight else "white"
    c.create_oval(x-6,y-6,x+6,y+6, fill=color,outline="black")
    c.create_text(x,y-12, text=name, font=("Arial",8))

c.bind("<Button-1>", show_coords)

root.mainloop()


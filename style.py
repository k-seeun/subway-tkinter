import tkinter as tk
from PIL import Image, ImageTk

def show_coords(event):
    print(f"Mouse at ({event.x}, {event.y})")

image = Image.open("C:\\Users\\3CLASS_012\\Desktop\\노선도2.webp")

# 역 좌표
stations = {
    "설화명곡": (50, 100),
    "화원": (50, 140),
    "대곡": (50, 180),
    "진천": (50, 220),
    "월배": (50, 260),
    "상인": (80, 300),

    "월촌": (120, 340),
    "송현": (160, 380),
    "서부정류장": (200, 420),
    "대명": (240, 420),
    "안자랑": (290, 420),
    "현충로": (330, 420),
    "영대병원": (370, 420),
    "교대": (410, 420),
    "명덕": (450, 430),

    "반월당": (450, 470),
    "중앙로": (450, 510),
    "대구역": (450, 550),
    "칠성시장": (450, 590),
    "신천": (460, 620),
    "동대구역": (470, 650),

    "동구청": (500, 660),
    "아양교": (530, 670),
    "동촌": (570, 670),
    "해안": (610, 670),
    "방촌": (650, 670),
    "용계": (690, 670),

    "율하": (720, 680),
    "신기": (750, 690),
    "반야월": (770, 700),
    "각산": (780, 710),
    "안심": (780, 750),
    "대구한의대병원": (780, 790),
    "부호": (780, 830),
    "하양": (780, 870),
}


# 연결리스트
edges = [
    ("설화명곡", "화원"),
    ("화원", "대곡"),
    ("대곡", "진천"),
    ("진천", "월배"),
    ("월배", "상인"),
    ("상인", "월촌"),
    ("월촌", "송현"),
    ("송현", "서부정류장"),
    ("서부정류장", "대명"),
    ("대명", "안자랑"),
    ("안자랑", "현충로"),
    ("현충로", "영대병원"),
    ("영대병원", "교대"),
    ("교대", "명덕"),
    ("명덕", "반월당"),
    ("반월당", "중앙로"),
    ("중앙로", "대구역"),
    ("대구역", "칠성시장"),
    ("칠성시장", "신천"),
    ("신천", "동대구역"),
    ("동대구역", "동구청"),
    ("동구청", "아양교"),
    ("아양교", "동촌"),
    ("동촌", "해안"),
    ("해안", "방촌"),
    ("방촌", "용계"),
    ("용계", "율하"),
    ("율하", "신기"),
    ("신기", "반야월"),
    ("반야월", "각산"),
    ("각산", "안심"),
    ("안심", "대구한의대병원"),
    ("대구한의대병원", "부호"),
    ("부호", "하양"),
]

# 사용자 선택
highlight = ["월배","화원",]

root = tk.Tk()
root.geometry("1200x700")

c = tk.Canvas(root, width=1200, height=700, bg="white")
c.pack()
new_width = 800
new_height = 800
image = image.resize((new_width, new_height))

# 2. 리사이즈된 이미지로 PhotoImage 생성
photo = ImageTk.PhotoImage(image)

canvas_width = 1000
canvas_height = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# 3. 캔버스 하단 중앙에 이미지 배치
c.create_image(canvas_width // 2, canvas_height, anchor=tk.S, image=photo)

# 4. 이미지 참조 유지
c.image = photo

# 기본 노선 - 얇은 회색
for a,b in edges:
    x1,y1 = stations[a]; x2,y2 = stations[b]
    c.create_line(x1,y1,x2,y2, fill="#ccc",width=3)

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


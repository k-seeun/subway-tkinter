import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("대구 지하철 노선도")

image = Image.open("C:\\Users\\3CLASS_012\\Desktop\\노선도2-removebg-preview.png")

# 1. 이미지 크기 조절
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
canvas.create_image(canvas_width // 2, canvas_height, anchor=tk.S, image=photo)

# 4. 이미지 참조 유지
canvas.image = photo

root.mainloop()

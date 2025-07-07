import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# 1. 노선 정보
stations = {
    "문양": 0,
    "반월당": 1,
    "경대병원": 2,
}

# 단순한 경로 정보 (임시 경로 설정)
simple_routes = {
    ("문양", "경대병원"): ["문양", "반월당", "경대병원"],
    ("문양", "반월당"): ["문양", "반월당"],
    ("반월당", "경대병원"): ["반월당", "경대병원"],
}

# 2. 함수 정의
def update_route():
    start = start_var.get()
    end = end_var.get()
    if start not in stations or end not in stations or start == end:
        result_var.set("올바른 출발지/도착지를 선택하세요.")
        return
    
    route = simple_routes.get((start, end)) or simple_routes.get((end, start))[::-1]
    if route:
        result_var.set(" → ".join(route))
    else:
        result_var.set("경로를 찾을 수 없습니다.")

# 3. UI 구성
root = tk.Tk()
root.title("대구 지하철 경로 찾기")
root.geometry("1000x700")

# 3-1. 이미지 배경 (노선도)
canvas = tk.Canvas(root, width=1000, height=600)
canvas.pack()

# 실제 이미지 경로 사용
image = Image.open("D:\\자료\\Desktop\\노선도.webp")  # 이미지 파일 경로 수정 필요
image = image.resize((1000, 600), Image.Resampling.LANCZOS)


photo = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)
canvas.image = photo  # 이미지 참조 유지

# 3-2. 입력 박스
frame = tk.Frame(root)
frame.pack(pady=10)

start_var = tk.StringVar()
end_var = tk.StringVar()
result_var = tk.StringVar()

tk.Label(frame, text="출발지:").grid(row=0, column=0)
ttk.Combobox(frame, textvariable=start_var, values=list(stations.keys()), width=15).grid(row=0, column=1, padx=10)

tk.Label(frame, text="도착지:").grid(row=0, column=2)
ttk.Combobox(frame, textvariable=end_var, values=list(stations.keys()), width=15).grid(row=0, column=3, padx=10)

tk.Button(frame, text="경로 찾기", command=update_route).grid(row=0, column=4, padx=10)

tk.Label(root, textvariable=result_var, font=("Arial", 14), fg="blue").pack(pady=10)

root.mainloop()

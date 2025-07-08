from tkinter import ttk

def apply_styles():
    style = ttk.Style()
    #style.theme_use("default")
    style.theme_use("clam")


    style.configure("TCombobox",
    fieldbackground="#FFFFFF",        # 더 밝은 흰색
    background="#E3F0FF",             # 드롭다운 배경
    foreground="#333333",             # 부드러운 글씨색
    padding=3                        # 여백 확대
)

    
    style.map("TCombobox",
    fieldbackground=[("readonly", "#F0F8FF")],
    foreground=[("active", "#000000")],
    background=[("active", "#DDEEFF")]
)

    style.configure("TButton",
    font=("Arial", 12, "bold"),
    background="#A7C8FF",             # 부드러운 블루
    foreground="#202020",
    padding=8
)

    style.map("TButton",
    background=[("active", "#96C9FF"), ("pressed", "#5EA6EF")],
    foreground=[("active", "#101010")]
)

    style.configure("TLabel",
    font=("Arial", 14, "bold"),
    foreground="#3366CC",             # 선명한 블루
    background="SystemButtonFace",    # 부모 배경 따라감
    padding=4
)

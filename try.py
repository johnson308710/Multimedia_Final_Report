import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

def open_image():
    global img, pixels, converted_image

    # 選擇圖片文件
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if not file_path:
        return

    # 加載圖片並顯示
    try:
        with Image.open(file_path) as image:
            img = image.convert("RGB")  # 確保轉為 RGB 模式
            pixels = np.array(img)
            tk_img = ImageTk.PhotoImage(img)

            # 更新顯示
            img_label.config(image=tk_img)
            img_label.image = tk_img
            img_label.pack()
    except Exception as e:
        messagebox.showerror("Error", f"無法加載圖片: {e}")

def convert_and_save_image():
    global pixels

    if pixels is None:
        messagebox.showwarning("Warning", "請先加載圖片！")
        return

    # 轉換像素數據（簡單反轉顏色作為示例）
    new_pixels = 255 - pixels  # 將顏色取反
    converted_image = Image.fromarray(new_pixels)

    # 保存圖片
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
    )
    if not save_path:
        return

    try:
        converted_image.save(save_path)
        messagebox.showinfo("Success", f"圖片已保存至: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"無法保存圖片: {e}")

# 創建主視窗
root = tk.Tk()
root.title("圖片轉換工具")

# 初始化變數
img = None
pixels = None
converted_image = None

# 按鈕和標籤
open_btn = tk.Button(root, text="選擇圖片", command=open_image)
open_btn.pack(pady=10)

convert_btn = tk.Button(root, text="執行轉換並保存", command=convert_and_save_image)
convert_btn.pack(pady=10)

img_label = tk.Label(root)
img_label.pack()

# 啟動主迴圈
root.mainloop()

from PIL import Image
import numpy as np

# 假設你已經有所有像素值，這裡我們用隨機值模擬
# 圖片尺寸為 512x512，3 個通道（RGB）
# height, width = 512, 512
# pixels = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
# 假設這是你的像素數據 (3x3 小圖片示例)
pixels = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],  # 紅、綠、藍
    [[255, 255, 0], [0, 255, 255], [255, 0, 255]],  # 黃、青、紫
    [[0, 0, 0], [128, 128, 128], [255, 255, 255]]  # 黑、灰、白
], dtype=np.uint8)

# 將像素矩陣轉換為圖片
image = Image.fromarray(pixels)

# 保存圖片
image.save("generated_image.png")

# 顯示圖片
image.show()


# # 創造圖片
# image = Image.fromarray(pixels)

# # 顯示圖片
# image.show()

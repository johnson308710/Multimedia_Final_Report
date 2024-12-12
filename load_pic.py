from PIL import Image
import numpy as np

# 讀取圖片
image_path = "original.jpg"  # 替換為你的圖片路徑
image = Image.open(image_path)

# 獲取圖片尺寸
width, height = image.size
print(f"圖片尺寸：{width}x{height}")

# 將圖片轉換為像素矩陣（使用 NumPy）
pixels = np.array(image)
print("像素矩陣形狀：", pixels.shape)

# 打印前幾個像素的數據
print("前幾個像素數據：")
print(pixels[:5, :5])  # 顯示前5x5個像素的數據

# 單個像素值的訪問（例如訪問第 (0, 0) 個像素）
pixel_value = pixels[0, 0]  # 取得左上角像素的數據
print(f"第 (0, 0) 個像素值：{pixel_value}")
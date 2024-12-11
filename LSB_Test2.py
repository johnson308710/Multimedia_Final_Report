from PIL import Image

def extract_lsb(image_path):
    # 開啟圖片
    image = Image.open(image_path)
    pixels = list(image.getdata())  # 獲取圖片像素
    width, height = image.size

    # 檢查圖片模式
    if image.mode == 'RGB':  # 彩色圖片
        binary_data = ""
        for pixel in pixels:
            # 提取藍色通道的最低有效位
            binary_data += str(pixel[2] & 1)
    elif image.mode in ['L', '1']:  # 灰階圖片或二值圖片
        binary_data = ""
        for pixel in pixels:
            # 提取單一灰階值的最低有效位
            binary_data += str(pixel & 1)
    else:
        raise ValueError(f"不支援的圖片模式：{image.mode}")

    # 將二進制資料轉換為字元
    byte_size = 8  # 每個字元 8 位元
    extracted_text = ""
    for i in range(0, len(binary_data), byte_size):
        byte = binary_data[i:i+byte_size]
        extracted_text += chr(int(byte, 2))

    # 檢查結束符號
    if "###END###" in extracted_text:
        return extracted_text.split("###END###")[0]
    return "無法找到隱藏的機密資訊。"

# 測試提取機密資訊
image_with_secret = "secret_image.png"
try:
    extracted_message = extract_lsb(image_with_secret)
    print(f"提取的機密資訊：{extracted_message}")
except Exception as e:
    print(f"提取過程中發生錯誤：{e}")

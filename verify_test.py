import cv2

def verify_watermark(image_path, original_watermark):
    # 讀取影像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 將影像展開為一維陣列
    flat_image = image.flatten()
    
    # 提取嵌入的浮水印
    extracted_bits = [str(flat_image[i] & 1) for i in range(len(original_watermark) * 8)]
    extracted_watermark = ''.join(chr(int(''.join(extracted_bits[i:i+8]), 2)) for i in range(0, len(extracted_bits), 8))
    
    # 驗證浮水印
    if extracted_watermark == original_watermark:
        print("驗證通過，影像未被篡改。")
    else:
        print("驗證失敗，影像可能已被篡改！")
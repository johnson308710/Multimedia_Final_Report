import cv2
import numpy as np
import hashlib

def embed_watermark(image_path, output_path, watermark):
    # 讀取影像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 將影像展開為一維陣列
    flat_image = image.flatten()
    
    # 將浮水印轉為二進制
    binary_watermark = ''.join(format(ord(char), '08b') for char in watermark)
    
    # 嵌入浮水印到影像的LSB位
    for i in range(len(binary_watermark)):
        flat_image[i] = (flat_image[i] & 0xFE) | int(binary_watermark[i])
    
    # 重組影像
    watermarked_image = flat_image.reshape(image.shape)
    
    # 保存嵌入結果
    cv2.imwrite(output_path, watermarked_image)
    print(f"浮水印已嵌入並保存到: {output_path}")



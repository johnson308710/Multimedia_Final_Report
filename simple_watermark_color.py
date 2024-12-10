import cv2
import numpy as np
import hashlib

def embed_watermark_color(image_path, output_path, watermark):
    # 讀取彩色影像
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    # 分離通道 (B, G, R)
    b_channel, g_channel, r_channel = cv2.split(image)
    
    # 將浮水印轉為二進制
    binary_watermark = ''.join(format(ord(char), '08b') for char in watermark)
    
    # 確保浮水印大小不超過單個通道的總像素數
    flat_r_channel = r_channel.flatten()
    if len(binary_watermark) > len(flat_r_channel):
        raise ValueError("浮水印太大，無法嵌入影像")
    
    # 嵌入浮水印到紅色通道 (R 通道) 的 LSB 位
    for i in range(len(binary_watermark)):
        flat_r_channel[i] = (flat_r_channel[i] & 0xFE) | int(binary_watermark[i])
    
    # 重組通道
    r_channel = flat_r_channel.reshape(r_channel.shape)
    watermarked_image = cv2.merge((b_channel, g_channel, r_channel))
    
    # 保存嵌入結果
    #cv2.imwrite(output_path, watermarked_image)
    cv2.imwrite(output_path, watermarked_image, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    print(f"彩色浮水印已嵌入並保存到: {output_path}")


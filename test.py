import cv2
import numpy as np
import hashlib

def embed_watermark(image_path, output_path):
    # 讀取影像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 計算影像的哈希值
    image_hash = hashlib.md5(image.tobytes()).hexdigest()
    binary_hash = ''.join(format(int(char, 16), '04b') for char in image_hash)  # 轉為二進制

    # 將哈希值嵌入影像的 LSB
    flat_image = image.flatten()
    for i in range(len(binary_hash)):
        flat_image[i] = (flat_image[i] & 0xFE) | int(binary_hash[i])
    watermarked_image = flat_image.reshape(image.shape)

    # 保存結果
    cv2.imwrite(output_path, watermarked_image)
    print(f"浮水印嵌入完成，保存至：{output_path}")
    return image_hash
def verify_watermark(image_path, original_hash):
    # 讀取影像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 提取影像中的哈希值
    flat_image = image.flatten()
    extracted_bits = [str(flat_image[i] & 1) for i in range(len(original_hash) * 4)]
    extracted_hash = ''.join(chr(int(''.join(extracted_bits[i:i+4]), 2) + ord('0')) for i in range(0, len(extracted_bits), 4))

    # 比對哈希值
    if extracted_hash == original_hash:
        print("驗證成功：影像未被篡改")
    else:
        print("驗證失敗：影像可能已被篡改")
        return False
    return True

# 範例
original_image_path = "original.jpg"
watermarked_image_path = "watermarked.jpg"
original_hash = embed_watermark(original_image_path, watermarked_image_path)

# 範例
verify_watermark(watermarked_image_path, original_hash)
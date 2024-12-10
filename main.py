import verify_test
import simple_watermark_gray
import simple_watermark_color
import hashlib
print("執行嵌入浮水印的動作")
# 使用範例
original_image_path = "original.jpg"
watermarked_image_path = "watermarked.png"
watermark = hashlib.md5(b"My Image").hexdigest()[:32]  # 取前32位哈希值
ans=print("選擇模式(1 or 2)",input())
if ans==1:
    simple_watermark_gray.embed_watermark(original_image_path, watermarked_image_path, watermark)
else:
    simple_watermark_color.embed_watermark_color(original_image_path, watermarked_image_path, watermark)
print("finish!!!")
print("進行浮水印的驗證")
verify_test.verify_watermark(watermarked_image_path, watermark)
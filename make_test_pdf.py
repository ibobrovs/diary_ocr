from PIL import Image
import os

# Папка с изображениями
INPUT_DIR = "pages"
# Имена нужных файлов
pages = [f"page_{i}.png" for i in range(5, 10)]

# Загружаем изображения
images = [Image.open(os.path.join(INPUT_DIR, p)).convert("RGB") for p in pages]

# Сохраняем как один PDF
output_path = "test_pages_5_to_9.pdf"
images[0].save(output_path, save_all=True, append_images=images[1:])

print(f"[✓] PDF сохранён: {output_path}")

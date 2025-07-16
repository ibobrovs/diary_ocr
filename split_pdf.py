import os
from pdf2image import convert_from_path

# Пути
PDF_PATH = "test_diary.pdf"  # замените на имя вашего файла
OUTPUT_DIR = "pages"

# Создание выходной папки
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Конвертация PDF в изображения
images = convert_from_path(PDF_PATH, dpi=300)

for i, img in enumerate(images):
    output_path = os.path.join(OUTPUT_DIR, f"page_{i+1:03d}.png")
    img.save(output_path, "PNG")
    print(f"[✓] Сохранена: {output_path}")

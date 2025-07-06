from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import os

IMAGES_DIR = "dataset/images"
OUTPUT_FILE = "recognized_text.txt"

# Загружаем модель и препроцессор
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")

recognized_lines = []

# Сортировка по имени файла
for filename in sorted(os.listdir(IMAGES_DIR)):
    if not filename.endswith(".png"):
        continue

    path = os.path.join(IMAGES_DIR, filename)
    image = Image.open(path).convert("RGB")

    # Преобразование и генерация текста
    inputs = processor(images=image, return_tensors="pt")
    generated_ids = model.generate(**inputs)
    text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    print(f"{filename}: {text}")
    recognized_lines.append(text)

# Сохраняем результат
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for line in recognized_lines:
        f.write(line.strip() + "\n")

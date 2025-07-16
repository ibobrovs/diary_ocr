import os
import cv2

INPUT_DIR = "pages"
OUTPUT_DIR = "dataset/images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

line_counter = 1

for filename in sorted(os.listdir(INPUT_DIR)):
    if not filename.lower().endswith(".png"):
        continue

    print(f"[INFO] Обработка: {filename}")
    image_path = os.path.join(INPUT_DIR, filename)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Бинаризация
    _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Морфология (шире по X, как ты хотел)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (60, 5))  # было 40x5
    dilated = cv2.dilate(binary, kernel, iterations=1)

    # Контуры
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[1])  # сортировка по Y

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if h > 20 and w > 150:
            line_img = image[y:y+h, x:x+w]
            output_path = os.path.join(OUTPUT_DIR, f"line_{line_counter:04d}.png")
            cv2.imwrite(output_path, line_img)
            print(f"  → Сохранено: {output_path}")
            line_counter += 1

print(f"[DONE] Вырезано строк: {line_counter - 1}")

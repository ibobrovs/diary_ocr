import os
from pdf2image import convert_from_path
from PIL import Image
import cv2
import pytesseract

# make new directory for images
IMAGES_DIR = "output_images"
os.makedirs(IMAGES_DIR, exist_ok=True)

# PDF to Image Conversion and OCR Processing
def pdf_to_images(pdf_path):
    print(f"[INFO] PDF convertation: {pdf_path}")
    images = convert_from_path(pdf_path)
    image_paths = []
    for i, img in enumerate(images):
        img_path = os.path.join(IMAGES_DIR, f"page_{i+1}.png")
        img.save(img_path, "PNG")
        image_paths.append(img_path)
        print(f" → Saved: {img_path}")
    return image_paths

# Image preprocessing
def preprocess_image(image_path):
    print(f"[INFO] Preprocessing: {image_path}")
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) #to gray
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] #to bw
    preprocessed_path = image_path.replace(".png", "_processed.png")
    cv2.imwrite(preprocessed_path, img)
    return preprocessed_path

# OCR processing
def run_ocr(image_path):
    print(f"[INFO] text recognition: {image_path}")
    text = pytesseract.image_to_string(Image.open(image_path), lang='lat')
    print("▼  Recognized text:")
    print(text)
    return text

if __name__ == "__main__":
    pdf_file = "/home/ibobrovs/handwritten_pdf_ocr/LKM_5_24377_1485-DK_compressed.pdf"
    pages = pdf_to_images(pdf_file)
    for page in pages:
        processed = preprocess_image(page)
        run_ocr(processed)


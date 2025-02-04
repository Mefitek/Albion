from PIL import Image
import pytesseract

# Cesta k Tesseract executable, pokud není ve výchozí cestě
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_text_from_image(image: Image.Image) -> str:
    # Přečte text z obrázku pomocí pytesseract
    text = pytesseract.image_to_string(image)
    return text

# Příklad použití:
# Načte obrázek (nahraďte 'path_to_image' skutečnou cestou k vašemu obrázku)
image_path = 'c1.jpg'
image = Image.open(image_path)
    
# Přečte text z obrázku
text = read_text_from_image(image)
    
# Vytiskne text do konzole
print(text)
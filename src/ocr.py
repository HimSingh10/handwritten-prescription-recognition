import easyocr
import cv2

# Load reader once
reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(image):

    if image is None:
        return ""

    # If grayscale, convert to RGB
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    results = reader.readtext(
        image,
        detail=0,
        paragraph=True,
        contrast_ths=0.1,
        adjust_contrast=0.5
    )

    extracted_text = "\n".join(results)

    return extracted_text.strip()
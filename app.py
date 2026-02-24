import os
from src.preprocess import preprocess_image
from src.ocr import extract_text_from_image
from src.parser import parse_medicines


def main():
    image_path = "data/sample.png"

    # 🔹 Check if file exists
    if not os.path.exists(image_path):
        print("❌ Error: Image file not found.")
        return

    # 🔹 Preprocess image
    processed_image = preprocess_image(image_path)

    if processed_image is None:
        print("❌ Error: Failed to load image.")
        return

    # 🔹 OCR extraction
    text = extract_text_from_image(processed_image)

    if not text.strip():
        print("⚠ No text detected.")
        return

    print("\n" + "=" * 60)
    print("📄 RAW EXTRACTED TEXT")
    print("=" * 60)
    print(text)

    # 🔹 Parse structured medicines
    structured_output = parse_medicines(text)

    print("\n" + "=" * 60)
    print("💊 STRUCTURED OUTPUT")
    print("=" * 60)

    if not structured_output:
        print("No structured medicines detected.")
        return

    for i, med in enumerate(structured_output, 1):
        print(f"\nMedicine #{i}")
        print("-" * 30)

        name_data = med.get("name", "N/A")

        # If parser returns dict with confidence
        if isinstance(name_data, dict):
            print(f"Name       : {name_data.get('name', 'N/A')}")
            print(f"Confidence : {round(name_data.get('confidence', 0), 2)}%")
        else:
            print(f"Name       : {name_data}")

        print(f"Dosage     : {med.get('dosage', 'N/A')}")
        print(f"Frequency  : {med.get('frequency', 'N/A')}")
        print(f"Duration   : {med.get('duration', 'N/A')}")

    print("\n✅ Processing Completed.\n")


if __name__ == "__main__":
    main()
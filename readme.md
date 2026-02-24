🔹 Handwritten Prescription Recognition
📌 Overview

This project extracts medicine names and dosage information from handwritten prescription images using OCR and intelligent post-processing.

🛠 Tech Stack

Python

OpenCV

EasyOCR

RapidFuzz (Fuzzy Matching)

🧠 Approach

Image preprocessing (resize, denoise, contrast enhancement)

OCR extraction using EasyOCR

Text cleaning and candidate filtering

Fuzzy matching against a medicine database

Threshold filtering (75%)

Structured output generation

📊 Features

Confidence score for each detected medicine

Duplicate removal

Basic dosage extraction

Clean structured terminal output

🚧 Challenges

Noisy OCR due to doctor handwriting

Spelling distortions

False positives control

🚀 Future Improvements

Transformer-based OCR (TrOCR)

Better segmentation

Deep learning fine-tuning
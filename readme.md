Handwritten Prescription Recognition System
Overview:

This project presents a modular pipeline for extracting medicine names and dosage information from handwritten prescription images using Optical Character Recognition (OCR) combined with intelligent post-processing techniques.

The system is designed as a confidence-aware assistive tool, helping identify medicines from handwritten prescriptions while incorporating safety through threshold-based validation and structured output generation.

Tech Stack:

Python

OpenCV – Image preprocessing

EasyOCR – Handwritten text extraction

RapidFuzz – Fuzzy string matching

Regex-based Parsing – Dosage extraction

System Architecture:
Input Prescription Image
        ↓
Image Preprocessing
        ↓
OCR Extraction (EasyOCR)
        ↓
Text Cleaning & Filtering
        ↓
Fuzzy Matching with Medicine Database
        ↓
Confidence Scoring & Threshold Logic
        ↓
Structured Output Generation
Approach:

Image Preprocessing

Resizing

Noise reduction

Contrast enhancement

OCR Extraction

Text detection using EasyOCR

Raw text generation

Post-Processing

Text normalization

Candidate filtering

Duplicate removal

Medicine Matching

Fuzzy matching against predefined medicine database

Threshold filtering (≥ 75%)

Confidence-Based Decision Layer

≥ 85% → Auto-Verified

70–85% → Review Recommended

< 70% → Manual Verification Required

Features:

Structured terminal output

Confidence score for detected medicines

Duplicate removal

Basic dosage extraction

CLI-based execution

Modular code design for future extensions

Limitations:

Performance depends on OCR quality.

Highly cursive or extremely complex doctor handwriting may reduce accuracy.

Designed as an assistive system; human verification is recommended for low-confidence outputs.

Key Challenges:

Noisy OCR results due to doctor handwriting

Spelling distortions and abbreviations

Controlling false positives during fuzzy matching

Handling overlapping or unclear text regions

Future Improvements:

Integration of Transformer-based OCR models (e.g., TrOCR)

Improved word-level segmentation

Context-aware correction using language models

Evaluation on larger annotated datasets

Web-based deployment (Streamlit/Flask interface)

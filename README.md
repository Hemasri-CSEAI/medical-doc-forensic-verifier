# Medical Document Forgery & Tampering Detector

An AI and Computer Vision tool designed to analyze medical certificates, lab reports, and official health documentation for digital manipulation. The system combines **Error Level Analysis (ELA)** and **EXIF Metadata Forensics** inside an interactive Streamlit interface to flag forged or edited regions.

## Key Features
- **Error Level Analysis (ELA):** Identifies digital alterations by resaving images at specific compression levels and highlighting variations in JPEG compression artifacts.
- **EXIF Metadata Parsing:** Extracts hidden metadata tags to inspect software history, modification timestamps, and camera/device profiles.
- **Visual Heatmap Generation:** Generates high-contrast visual difference maps pinpointing tampered text, modified dates, or altered doctor signatures.
- **Interactive Web App:** Built with Streamlit for seamless document uploads and real-time visual inspection.

## Tech Stack
- **Language:** Python
- **Web Framework:** Streamlit
- **Computer Vision & Image Processing:** OpenCV, Pillow (PIL), NumPy
- **Image Forensics:** Error Level Analysis (ELA), `piexif` / `ExifRead`

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Hemasri-CSEAI/medical-doc-forensic-verifier.git
   cd medical-doc-forensic-verifier
```
2. Install dependencies
```bash
   pip install streamlit opencv-python pillow numpy piexif
```
3. Run the application:
```bash
   streamlit run app.py
```

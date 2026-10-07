import streamlit as st
from PIL import Image, ImageChops, ImageEnhance
from PIL.ExifTags import TAGS
import os

# --- 1. THE DETECTION BRAINS ---

# Brain A: Metadata Check
def check_metadata(image_file):
    img = Image.open(image_file)
    info = img.getexif()
    if not info:
        return "No metadata found. (Common in WhatsApp/Scanned files)."
    for tag_id in info:
        tag = TAGS.get(tag_id, tag_id)
        data = info.get(tag_id)
        if tag == "Software":
            return f"⚠️ ALERT: Modified via *{data}*!"
    return "✅ No editing software signatures found."

# Brain B: ELA Heatmap (Visual Tampering)
def conduct_ela(image_file, quality=90):
    original = Image.open(image_file).convert('RGB')
    
    # Save temporary version at lower quality
    temp_filename = "temp_ela.jpg"
    original.save(temp_filename, 'JPEG', quality=quality)
    temporary = Image.open(temp_filename)
    
    # Calculate the difference between original and temporary
    diff = ImageChops.difference(original, temporary)
    
    # Boost the brightness of the difference so we can see it
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    
    diff = ImageEnhance.Brightness(diff).enhance(scale)
    
    # Cleanup temporary file
    if os.path.exists(temp_filename):
        os.remove(temp_filename)
        
    return diff

# --- 2. THE USER INTERFACE ---
st.set_page_config(page_title="Forensic Doc Verifier", layout="wide")
st.title("🛡️ Medical Document Forgery Detector")

uploaded_file = st.file_uploader("Upload Medical Scan (JPG/PNG)", type=["jpg", "png"])

if uploaded_file:
    # Create two columns for a professional look
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Document")
        st.image(uploaded_file, use_container_width=True)
        
        # Run Metadata Check
        meta_result = check_metadata(uploaded_file)
        st.info(f"*Metadata Analysis:* {meta_result}")

    with col2:
        st.subheader("Tampering Heatmap (ELA)")
        with st.spinner("Analyzing pixels..."):
            ela_image = conduct_ela(uploaded_file)
            st.image(ela_image, use_container_width=True)
            st.caption("Bright/noisy spots indicate potential digital alterations.")

    st.warning("Note: This is an assistive tool. Always cross-verify with hospital records.")
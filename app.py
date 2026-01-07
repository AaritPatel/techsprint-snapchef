import streamlit as st
from PIL import Image
import image_handler  # <--- NEW LINE

# 1. Page Configuration (The Title Bar)
st.set_page_config(page_title="SnapChef", page_icon="🍳", layout="centered")

# 2. Main Title and CSS Styling
st.title("🍳 SnapChef")
st.write("Snap a photo of your fridge ingredients, and I'll tell you what to cook!")

# 3. Two Input Options: Camera OR File Upload
# We use columns to make it look neat
col1, col2 = st.columns(2)

with col1:
    camera_file = st.camera_input("📸 Take a photo")

with col2:
    uploaded_file = st.file_uploader("📂 Or upload an image", type=["jpg", "png", "jpeg"])

# 4. Logic to handle the image (Prioritize camera if both exist)
image_source = camera_file if camera_file else uploaded_file

# 5. Display the image so the user knows it worked
if image_source:
    # Open the image using PIL (Python Imaging Library)
    image = Image.open(image_source)
    
    st.success("Image captured! 🚀")
    st.image(image, caption="Your Ingredients", use_container_width=True)
    
    # This button will eventually trigger the AI (Member 3's job)
    if st.button("👨‍🍳 Generate Recipe", type="primary"):
        # 1. Process the image (Member 2's Job)
        try:
            processed_image = image_handler.process_image(image_source)
            st.success("✅ Image processed successfully!")
            
            # 2. AI Logic (Member 3's Job - Coming Soon)
            st.info("Sending to AI Chef...")
            
        except Exception as e:
            st.error(f"Error processing image: {e}")
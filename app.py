import streamlit as st
from PIL import Image
import image_handler  # <--- NEW LINE
import image_handler
import chef_brain  # <--- NEW LINE

# 1.. Minimal Welcome Interface
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🍳 Welcome to SnapChef</h1>", unsafe_allow_html=True)
st.write("### Your kitchen, reimagined. Snap a photo and let's get cooking!")

# 1. Page Configuration (The Title Bar)
st.set_page_config(page_title="SnapChef", page_icon="🍳", layout="centered")

# 2. Main Title and CSS Styling
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
        try:
            with st.spinner("👨‍🍳 Chef is analyzing your ingredients...Stay calm as it might take a few seconds to suggest you a delicious meal..."):
                # 1. Process Image
                processed_image = image_handler.process_image(image_source)
                
                # 2. Ask the AI (Member 3's Job)
                response_text = chef_brain.get_recipe(processed_image)
                
                # 3. Display Result
                st.markdown(response_text)
                st.balloons()
                
        except Exception as e:
            st.error(f"Error: {e}")

            


import streamlit as st

def process_image(uploaded_file):
    """
    Converts a Streamlit file upload object into the format
    expected by Google Gemini API.
    """
    # Check if a file was actually uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        # Create the dictionary format Gemini expects
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # e.g., "image/jpeg" or "image/png"
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No image uploaded")
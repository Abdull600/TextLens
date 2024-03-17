import replicate
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="TextLens")

st.title("Image text extraction(OCR model)")
st.header("Model UI")


image_upload = st.file_uploader(
        "Please upload an image(with text)", type=["png", "jpg", "jpeg"]
    )


def extract_text():
    text_extract = replicate.run(
        "abiruyt/text-extract-ocr:a524caeaa23495bc9edc805ab08ab5fe943afd3febed884a4f3747aa32e9cd61",
        input={
            "image": image_upload,
        },
    )
    return text_extract



if image_upload:
    if st.button("Extract text"):
        image_extract = extract_text()
        
        with st.chat_message('user'):
            st.write("This is the extracted text")
            st.markdown(
                f"""
                    <div style="background-color: black; color: white; font-weight: bold; padding: 1rem; margin-bottom: 0.5rem; border-radius: 10px;">
                    {image_extract}
                """,
                unsafe_allow_html=True,
            )
            
    st.success("Successful")




st.write("")
st.write("")
st.write("")


st.markdown(
    """
    <div style="text-align: center; padding: 1rem;">
        Project by <a href="https://github.com/ChibuzoKelechi" target="_blank" style="color: white; font-weight: bold; text-decoration: none;">
         kelechi_tensor</a>
    </div>
    
    <div style="text-align: center; padding: 1rem;">
        Powered by <a href="https://replicate.com" target="_blank" style="color: lightblue; font-weight: bold; text-decoration: none;">
         ReplicateAI models</a>
    </div>
""",
    unsafe_allow_html=True,
)

# Arigato :)
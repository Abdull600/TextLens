import replicate
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="TextLens")

st.title("Image text extraction(OCR model)")
st.header("Model UI")

# file_tab, camera_tab = st.tabs(["Files", "Camera"])

# with file_tab:
image_upload = st.file_uploader(
        "Please upload an image(with text)", type=["png", "jpg", "jpeg"]
    )

# with camera_tab:
#     camera_upload = st.camera_input("Take pic with phone")


def extract_text():
    text_extract = replicate.run(
        "abiruyt/text-extract-ocr:a524caeaa23495bc9edc805ab08ab5fe943afd3febed884a4f3747aa32e9cd61",
        input={
            "image": image_upload,
        },
    )
    # text_extract = st.write_stream(text_extract)
    return text_extract

# def extract_input():
#     if camera_tab:
#         extract_text(camera_upload)
#     else:
#         extract_text(image_upload)
        

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


# print(text_extract)


# Footer
st.write("")
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

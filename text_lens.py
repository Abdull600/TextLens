import replicate
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="TextLens")

st.title("Image classification (Crops)")
st.header("Model UI")


image_upload = st.file_uploader(
    "Please upload an image(Face)", type=["png", "jpg", "jpeg"]
)

text_extract = replicate.run(
    "abiruyt/text-extract-ocr:a524caeaa23495bc9edc805ab08ab5fe943afd3febed884a4f3747aa32e9cd61",
    input={
        "image": image_upload,
    },
)


if image_upload:
    if st.button("Extract text"):
        with st.spinner("Extracting..."):
            st.markdown(
                f"""
                    <div style="background-color: black; color: white; font-weight: bold; padding: 1rem; border-radius: 10px;">
                    <h4>Image text</h4>
                    {text_extract}
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
        Data from <a href="https://kaggle.com" target="_blank" style="color: lightblue; font-weight: bold; text-decoration: none;">
         Kaggle</a>
    </div>
""",
    unsafe_allow_html=True,
)

# Arigato :)

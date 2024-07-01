import streamlit as st
from PIL import Image
from ultralytics import YOLOv10
import cv2


MODEL_PATH = "./models/best.pt"
IMG_SIZE = 640
CONF_THRESHOLD = 0.3

if "model" not in st.session_state:
    st.session_state.model = YOLOv10(MODEL_PATH)

st.title("Helmet Safety Detection Demo")


file = st.file_uploader("Select image", ['jpg', 'png', 'jpeg'])

if file is not None:
    col1, col2 = st.columns(2)
    with col1:
        st.image(file, caption="Uploaded image")
    with col2:
        image = Image.open(file)
        results = st.session_state.model.predict(
            source=image, imgsz=IMG_SIZE, conf=CONF_THRESHOLD)
        annotated_img = cv2.cvtColor(results[0].plot(), cv2.COLOR_BGR2RGB)

        st.image(annotated_img, "YOLOv10 result")

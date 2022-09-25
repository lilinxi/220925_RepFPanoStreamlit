import time

import streamlit as st
import numpy as np

from util import *

Title = "RepF Pano Context"

st.set_page_config(
    page_title=Title,
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title(Title)

uploaded_file = st.file_uploader("Drag and drop a pano image, only jpg or png are allowed", type=["jpg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    cv2.imwrite('test.png', opencv_image)

    with st.sidebar:
        st.header("Load Pano Image")
        with st.spinner("Loading Pano Image..."):
            st_image_file(st, './test.png')
        st.success("Load Pano Image Success!")

        st.header("Process Pano Image")
        PROGRESS = get_progress()
        PROGRESS(10)

    col1, col2, col3, col4 = st.columns([1, 1, 2, 2])

    with col1:
        st.subheader("Proj Image")
        total_progress = 20
        image_list = [f'./network/proj_image_{i}.png' for i in range(19)]
        sub_progress = total_progress / len(image_list)
        for img in image_list:
            PROGRESS(sub_progress)
            st_image_file(st, img, width=150)
    with col2:
        st.subheader("Proj Result")
        total_progress = 20
        image_list = [f'./network/proj_image_{i}.png' for i in range(19)]
        sub_progress = total_progress / len(image_list)
        for img in image_list:
            PROGRESS(sub_progress)
            st_image_file(st, img, width=150)

    with col3:
        st.subheader("Re-Proj Image")
        total_progress = 20
        image_list = [f'./network/proj_resp_{i}.png' for i in range(19)]
        sub_progress = total_progress / len(image_list)
        for img in image_list:
            PROGRESS(sub_progress)
            st_image_file(st, img, width=300)

    with col4:
        st.subheader("Re-Proj Result")
        total_progress = 20
        image_list = [f'./network/proj_resp_{i}.png' for i in range(19)]
        sub_progress = total_progress / len(image_list)
        for img in image_list:
            PROGRESS(sub_progress)
            st_image_file(st, img, width=300)

    with st.sidebar:
        PROGRESS(10)
        st_image_file(st, './network/resp.png')
        st.success("Process Pano Image Success!")

    st.markdown('<iframe src="https://gltf-viewer.donmccurdy.com/" '
                'style="'
                'width: 100%; '
                'height: 500px; '
                '">'
                '</iframe>',
                unsafe_allow_html=True)

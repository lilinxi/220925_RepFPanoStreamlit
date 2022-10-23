import time
import subprocess
import threading

import streamlit as st
import numpy as np

from util import *
from client import *

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

    time_stamp = int(time.time())
    sys = platform.system()
    if sys == 'Darwin':
        work_dir = f'/Users/limengfan/Desktop/tmp/repf_pano_client/{time_stamp}'
    elif sys == 'Linux':
        work_dir = f'/home/lmf/tmp/repf_pano_client/{time_stamp}'
    else:
        print(f"uploaded_file do not support {sys} system")
        exit(255)
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    image_path = f"{work_dir}/input.png"
    print("image_path:", image_path)
    cv2.imwrite(image_path, opencv_image)

    with st.sidebar:
        st.header("Load Pano Image")
        with st.spinner("Loading Pano Image..."):
            st_image_file(st, image_path)
        st.success("Load Pano Image Success!")

        st.header("Process Pano Image")

        log_path = f"{image_path}.log"
        if os.path.exists(log_path):
            os.remove(log_path)
        open(log_path, 'w').close()

        # 1. 先打开日志流监控
        p = subprocess.Popen(f'tail -f {log_path}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 2. 再请求算法模块，image_path 使用绝对路径
        threading.Thread(target=detect_client(image_path)).start()

        line = p.stdout.readline().decode("utf-8")[:-1]
        PROGRESS = get_progress()
        PROGRESS(5)

        project_num = int(p.stdout.readline().decode("utf-8")[:-1])

    col1, col2, col3, col4 = st.columns([1, 1, 2, 2])

    # with col1:
    #     st.subheader("Proj Image")
    # with col2:
    #     st.subheader("Proj Result")
    # total_progress = 20
    # sub_progress = total_progress / project_num
    #
    # for _ in range(project_num):
    #     img = p.stdout.readline().decode("utf-8")[:-1]
    #     st_image_file(col1, img, width=150)
    #     PROGRESS(sub_progress)
    #
    #     img = p.stdout.readline().decode("utf-8")[:-1]
    #     st_image_file(col2, img, width=150)
    #     PROGRESS(sub_progress)

    with col1:
        st.subheader("Proj Image")
        total_progress = 20
        sub_progress = total_progress / project_num

        for i in range(project_num):
            img = p.stdout.readline().decode("utf-8")[:-1]
            st_image_file(st, img, width=150)
            PROGRESS(sub_progress)

    with col2:
        st.subheader("Proj Result")
        total_progress = 20
        sub_progress = total_progress / project_num

        for i in range(project_num):
            img = p.stdout.readline().decode("utf-8")[:-1]
            st_image_file(st, img, width=150)
            PROGRESS(sub_progress)

    with col3:
        st.subheader("Re-Proj Image")
        total_progress = 20
        sub_progress = total_progress / project_num

        for i in range(project_num):
            img = p.stdout.readline().decode("utf-8")[:-1]
            st_image_file(st, img, width=300)
            PROGRESS(sub_progress)

    with col4:
        st.subheader("Re-Proj Result")
        total_progress = 20
        sub_progress = total_progress / project_num

        for i in range(project_num):
            img = p.stdout.readline().decode("utf-8")[:-1]
            st_image_file(st, img, width=300)
            PROGRESS(sub_progress)

    with st.sidebar:
        resp_img = p.stdout.readline().decode("utf-8")[:-1]
        PROGRESS(5)
        st_image_file(st, resp_img)

    resp_glb = p.stdout.readline().decode("utf-8")[:-1]
    st.markdown('<a href="http://219.224.167.226/scene.glb" download="scene.glb">scene.glb</a>', unsafe_allow_html=True)
    st.markdown('<iframe src="https://gltf-viewer.donmccurdy.com/" '
                'style="'
                'width: 100%; '
                'height: 500px; '
                '">'
                '</iframe>',
                unsafe_allow_html=True)
    PROGRESS(10)
    with st.sidebar:
        st.success("Process Pano Image Success!")



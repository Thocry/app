import streamlit as st
import tensorflow as tf
import cv2
import numpy as np

from PIL import Image


def main():
    st.title("Đọc và hiển thị ảnh")

    # Cho phép người dùng chọn tệp tin ảnh
    uploaded_file = st.file_uploader("Chọn tệp tin ảnh", type=["jpg", "jpeg", "png"])

    # Kiểm tra xem người dùng đã chọn tệp tin hay chưa
    if uploaded_file is not None:
        # Đọc ảnh từ tệp tin
        image = Image.open(uploaded_file)

        # Chuyển đổi ảnh thành mảng numpy
        image_array = np.array(image)

        # Hiển thị ảnh
        st.image(image, caption="Ảnh đã chọn")

        # Hiển thị thông tin về ảnh
        st.write("Kích thước ảnh:", image.size)
        st.write("Định dạng ảnh:", image.format)
        st.write("Loại dữ liệu:", type(image))
        st.write("Mảng numpy:", image_array)

if __name__ == "__main__":
    main()
 
'''import streamlit as st
from PIL import Image
from NN18 import predict18
from NN34 import predict34
from NN50 import predict50
from NN101 import predict101
from NN152 import predict152

st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("Simple Image Classification App")
st.write("")

file_up = st.file_uploader("Upload an image", type="jpg")

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Just a second...")
    labels18 = predict18(file_up)
    labels34 = predict34(file_up)
    labels50 = predict50(file_up)
    labels101 = predict101(file_up)
    labels152 = predict152(file_up)

    # print out the top prediction label with score
    for i in labels18:
        st.write("Prediction from ResNet18(index, name)", i[0], ",   Score: ", i[1])
    for i in labels34:
        st.write("Prediction from ResNet34(index, name)", i[0], ",   Score: ", i[1])
    for i in labels50:
        st.write("Prediction from ResNet50(index, name)", i[0], ",   Score: ", i[1])
    for i in labels101:
        st.write("Prediction from ResNet101 (index, name)", i[0], ",   Score: ", i[1])
    for i in labels152:
        st.write("Prediction from ResNet152(index, name)", i[0], ",   Score: ", i[1])
'''
'''
import streamlit as st
from PIL import Image
from NN18 import predict18
from NN34 import predict34
from NN50 import predict50
from NN101 import predict101
from NN152 import predict152

st.set_option('deprecation.showfileUploaderEncoding', False)

# Set page title and favicon
st.set_page_config(
    page_title="Image Classification App",
    page_icon="🖼️",
    layout="centered",
)

# Set app title and description
st.title("🌟Image Classification App ")
st.write("Upload any image and get predictions from different AI-ResNet models.")

# Add a custom color style
st.markdown(
    """
    <style>
        div.Widget.row-widget.stRadio > div{flex-direction:row;}
        div.Widget.row-widget.stRadio > div > label{padding-top:5px; padding-right:20px;}
        .st-bw{border-width: 3px !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Add an optional description
st.write("This app uses various ResNet models for image classification.\nIt also gives us the accuracy score of each ResNet Model.")

file_up = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Classifying...")

    labels_functions = [predict18, predict34, predict50, predict101, predict152]
    model_names = ["ResNet 18", "ResNet 34", "ResNet 50", "ResNet 101", "ResNet 152"]

    st.subheader("Predictions:")

    for model_name, predict_func in zip(model_names, labels_functions):
        st.write(f"{model_name} Predictions:")
        labels = predict_func(file_up)
        for label in labels:
            st.write(f"   - {label[1]} (Index: {label[0]}, Score: {label[1]:.2f})")

# Add a footer with credits or additional information if needed
st.markdown(
    """
    *Built with ❤️ by NSCC*
    """,
    unsafe_allow_html=True,
)
'''
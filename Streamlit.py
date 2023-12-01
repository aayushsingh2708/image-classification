import streamlit as st
from PIL import Image
from NN18 import predict18
from NN34 import predict34
from NN50 import predict50
from NN101 import predict101
from NN152 import predict152

# Set page title and favicon
st.set_page_config(
    page_title="Image Classification App",
    page_icon="🖼️",
    layout="wide",
)

# Set app title and description with a colorful header
st.title("🌟 Image Classification App 🌟")
st.markdown(
    """
    *Upload any image and get predictions from different AI-ResNet models.*
    """
)

# Add a custom color style
st.markdown(
    """
    <style>
        .main {
            background-color: #f8f9fa;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .header {
            background-color: #007bff;
            color: #ffffff;
            padding: 1rem;
            border-radius: 10px 10px 0 0;
            margin-bottom: 1rem;
        }
        .footer {
            background-color: #007bff;
            color: #ffffff;
            padding: 1rem;
            border-radius: 0 0 10px 10px;
            margin-top: 1rem;
        }
        .prediction {
            margin-top: 1.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add an optional description
st.write("This app uses various ResNet models for image classification. It also provides the accuracy score of each ResNet Model.")

# File upload and model prediction
file_up = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if file_up is not None:
    image = Image.open(file_up)

    # Display uploaded image with a stylish border
    st.image(image, caption='Uploaded Image.', use_column_width=True, output_format="JPEG", channels="RGB")
    st.markdown("---")

    # Classify image and display predictions
    labels_functions = [predict18, predict34, predict50, predict101, predict152]
    model_names = ["ResNet 18", "ResNet 34", "ResNet 50", "ResNet 101", "ResNet 152"]

    st.subheader("Predictions:")
    for model_name, predict_func in zip(model_names, labels_functions):
        st.write(f"**{model_name} Predictions:**")
        labels = predict_func(file_up)
        for label in labels:
            st.write(f"   - Accuracy: {round(label[1],2)} (Index: {label[0]})")

# Add a footer with credits or additional information
st.markdown(
    """
    <div class="footer">
        <p>Built by NSCC</p>
    </div>
    """,
    unsafe_allow_html=True,
)

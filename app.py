
import streamlit as st
import numpy as np
from PIL import Image
import joblib
from streamlit_drawable_canvas import st_canvas

# Load your trained model
model = joblib.load('KNN_MNIST_USPS.joblib')  # Ensure the path is correct

# Function to preprocess the image
def preprocess_image(image):
    image = image.convert('L')  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to the input size of your model (28x28 for MNIST)
    image_array = np.array(image)  # Convert to NumPy array
    image_array = image_array / 255.0  # Normalize to [0, 1]
    image_array = image_array.flatten().reshape(1, -1)  # Flatten and reshape for the model
    return image_array

# Title of the app
st.title("Digit Recognition Application")

# File uploader for users to upload images
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

# Placeholder for the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    processed_image = preprocess_image(image)
else:
    # Draw a digit using the mouse
    st.write("Or draw a digit below:")
    canvas_result = st_canvas(
        fill_color="black",
        stroke_color="white",
        background_color="black",
        height=280,
        width=280,
        stroke_width=15,
        drawing_mode="freedraw",
        key="canvas"
    )

    # Convert drawn image to PIL for processing
    if canvas_result.image_data is not None:
        image = Image.fromarray(canvas_result.image_data)
        st.image(image, caption='Drawn Image', use_column_width=True)
        processed_image = preprocess_image(image)

# Make prediction if an image is available
if 'processed_image' in locals():
    with st.spinner("Making prediction..."):  # Add a loading spinner
        try:
            prediction = model.predict(processed_image)
            # Display prediction
            st.write(f"Predicted Digit: {prediction[0]}")
        except Exception as e:
            st.error("Error making prediction. Please ensure the image is valid.")
            st.error(str(e))  # Optionally display the error message

import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import numpy as np
import base64
import random
import cv2
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="ImageMagic - Your Image Processing Companion")

MAX_FILE_SIZE = 5 * 1024 * 1024


# Function to remove background using rembg library
def remove_background(image):
    return remove(image)

# Function to convert image to pencil sketch
def convert_to_pencil_sketch(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray_img)
    blur = cv2.GaussianBlur(invert, (111, 111), 0)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(gray_img, invertedblur, scale=256.0)
    sketch_image = Image.fromarray(sketch)
    return sketch_image

# Function to convert image to byte format for download
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Function to process uploaded image based on selected action
def process_image(upload, action):
    image = Image.open(upload)

    coli = st.columns(5)
    with coli[0]:
        st.image(image, caption="Original Image", width=300)
    with coli[3]:
        if action == "Remove Background":
            result = remove_background(image)
            st.image(result, caption="Background Removed", width=300)

        elif action == "Convert to Pencil Sketch":
            result = convert_to_pencil_sketch(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR))
            st.image(result, caption="Pencil Sketch", width=200)


    st.markdown(get_image_download_link(result), unsafe_allow_html=True)

# Function to generate download link for processed image

def get_image_download_link(img, filename="result.png"):
    """
    Generates a download link for the given image.

    Parameters:
        img (PIL.Image.Image): The image to be downloaded.
        filename (str): The filename to be used when downloading the image.

    Returns:
        str: The HTML string representing the download link.
    """
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:image/png;base64,{img_str}" download="{filename}">Download Image</a>'
    return href


def search_unsplash_images(query):
        try:
            # Send a request to Unsplash with the search query
            url = f"https://unsplash.com/s/photos/{query}"
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract image URLs from the parsed HTML
            image_urls = [img['src'] for img in soup.find_all('img') if img.get('src')]
            image_urls = image_urls[:40]
            random.shuffle(image_urls)
            # Display the images in columns with three images per column
            num_columns = 3
            images_per_column = len(image_urls) // num_columns
            for i in range(num_columns):
                col = st.columns(num_columns)
                start_index = i * images_per_column
                end_index = (i + 1) * images_per_column
                for j, image_url in enumerate(image_urls[start_index:end_index], start=start_index):

                        # Download the image
                        image_data = requests.get(image_url).content
                        image = Image.open(BytesIO(image_data))

                        # Display the image
                        col[j % num_columns].image(image, use_column_width=True)


        except requests.exceptions.RequestException as e:
            st.warning(f"Image Not Show Try Again ")

# App description
st.title("🎉Welcome to ImageMagic")
st.write("""
    ✨ImageMagic is a versatile image processing application🚀 that simplifies common image editing tasks.
    Upload an image and choose from the available options to enhance your images effortlessly⚡!
""")

# Sidebar for options
st.sidebar.title("Options")
selected_option = st.sidebar.radio("Select an option", ("Home", "Remove Background", "Convert to Pencil Sketch", "image with AI","Search image", "README.md"))

# Display README content within the Options section
if selected_option == "README.md":
    st.title("README")
    readme_content = """
    # ImageMagic

    ## Overview

    ImageMagic is a powerful image processing application that allows users to enhance their images with ease. Whether you want to remove backgrounds or create stunning pencil sketches, ImageMagic has you covered. This app offers a simple and intuitive interface, making it accessible to users of all skill levels.

    ## Features

    - **Background Removal:** Effortlessly remove backgrounds from images to isolate subjects and create stunning compositions.
    - **Pencil Sketch Conversion:** Transform your images into beautiful pencil sketches with just a click of a button.
    - **Upload and Download:** Easily upload your images for processing and download the results to your device.

    ## Usage

    1. **Upload Image:** Select an image file (supported formats include PNG, JPG, and JPEG) by clicking on the "Upload an image" button.
    2. **Select Action:** Choose from the available options in the sidebar to either remove the background or convert the image to a pencil sketch.
    3. **View Results:** The processed image will be displayed in the main window, allowing you to preview the changes.
    4. **Download:** Once you're satisfied with the result, you can download the processed image by clicking on the "Download Result" link.

    ## Installation

    To run ImageMagic locally, follow these steps:

    1. Clone this repository to your local machine:

    ```
    git clone https://github.com/codewithdark-git/ImageMagic.git
    ```

    2. Navigate to the project directory:

    ```
    cd ImageMagic
    ```

    3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

    4. Run the Streamlit app:

    ```
    streamlit run app.py
    ```

    5. Access the app in your web browser at `http://localhost:8501`.

    ## Credits

    - This app utilizes the [rembg](https://github.com/danielgatis/rembg) library for background removal.
    - Built with [Streamlit](https://streamlit.io/).

    ## License

    This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
    """
    st.markdown(readme_content)

elif selected_option == "Home":
        st.subheader("Home")
        st.write("## Welcome to Image Processing App")
        st.write("This app allows you to perform various image processing tasks such as background removal and converting images to pencil sketches.")

        # Introduction to Background Removal
        st.write("### Background Removal")
        st.write("With the background removal feature, you can easily separate the main object from its background.")
        st.write("Here's an example of an original image and its background removed version:")

        # Display original image and background removed image
        st.write("### Original Image and Background Removed")
        st.write('<div style="display: flex;">', unsafe_allow_html=True)
        with st.container():
            st.image("Background_remove.png", caption="Original Image", width=600)
        st.write('</div>', unsafe_allow_html=True)

        # Introduction to Pencil Sketch Conversion
        st.write("### Pencil Sketch Conversion")
        st.write("The app also provides an option to convert images into pencil sketches using OpenCV.")
        st.write("Here's an example of an original image and its corresponding pencil sketch:")

        # Display original image and pencil sketch image
        st.write("### Original Image and Pencil Sketch")
        st.write('<div style="display: flex;">', unsafe_allow_html=True)
        with st.container():
            st.image("pencil_sketch.png", caption="Original Image", width=600)
        st.write('</div>', unsafe_allow_html=True)

        # Summarize the App
        st.write("### Summary")
        st.write("This app offers a simple yet powerful interface for performing common image processing tasks.")
        st.write("Explore the various functionalities and unleash your creativity!")

        # Footer with Author Information
        st.write("---")
        st.write("### About the Author")
        st.write("This app was created by [Your Name].")
        st.write("For more projects and contact information, visit:")
        st.write("[GitHub](https://github.com/codewithdark-git) | [LinkedIn](https://www.linkedin.com/in/codewithdark)")

elif selected_option == "Search image":
    st.title("")  # No title for the search image section

    search_query = st.text_input("Enter search query:")
    if st.button("Search"):
        if search_query:
            search_unsplash_images(search_query)
        else:
            st.warning("Please enter a search query.")

# elif selected_option == "image with AI":
#     import gradio as gr
#
#     gr.load("models/stabilityai/stable-diffusion-xl-base-1.0").launch()

else:
    # Process uploaded image
    my_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if my_upload is not None:
        if my_upload.size > MAX_FILE_SIZE:
            st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
        else:
            process_image(upload=my_upload, action=selected_option)

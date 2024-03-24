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
  
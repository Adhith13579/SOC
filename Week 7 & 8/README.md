# AI Steel Surface QA Inspector

An AI-powered industrial quality assurance web application that detects surface defects on steel sheets using a trained YOLOv8 model and generates professional inspection reports using a local LLM (Llama 3.2 via Ollama).

## Features

- Upload a steel surface image through a web interface
- Detect defects using a custom-trained YOLOv8 model
- Display detected defects with bounding boxes drawn on the image
- Generate a professional inspection report using Llama 3.2 (running locally via Ollama)
- Download the generated report as a text file

## Requirements

- Python 3.9 or higher
- Ollama (for running the local LLM)

## Setup Instructions

1. Install Ollama from https://ollama.com and follow the installation steps for your operating system.

2. Pull the Llama 3.2 model:
   ```
   ollama pull llama3.2
   ```

3. Clone this repository and navigate into the project folder:
   ```
   git clone <your-repo-url>
   cd qa_app
   ```

4. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

5. Make sure `best.pt` (the trained YOLOv8 model file) is present in the project folder.

## Running the Application

Start the app with:
```
python -m streamlit run app.py
```

This will open the application in your default web browser. If it does not open automatically, copy the local URL shown in the terminal into your browser.

## Usage

1. Click the upload button and select a steel surface image (JPG or PNG).
2. The application will detect defects and display the image with bounding boxes.
3. A list of detected defects with confidence scores will be shown.
4. An AI-generated inspection report will be produced below, including a summary, severity rating, and recommended actions.
5. Use the download button to save the report as a text file.

## Project Structure

```
qa_app/
├── app.py              Main Streamlit application
├── best.pt              Trained YOLOv8 model weights
├── requirements.txt      Python dependencies
└── README.md            Project documentation
```

## Notes

- Ollama must be running in the background for report generation to work. It usually starts automatically after installation, but if report generation fails, run `ollama serve` in a separate terminal.
- Crazing defects may be harder to detect reliably compared to other defect classes due to their low visual contrast in the dataset.

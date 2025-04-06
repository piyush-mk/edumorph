# EduMorph: AI Course Plan & Intro Video Generator

EduMorph is a Streamlit-based web application that leverages Llama 3.1 Nemotron model to generate detailed course plans and concise introductory video scripts based on user-specified topics. The app provides learners with a structured course outline, while storing the video script for future AI-driven video generation and interactive course customization features.

## Features

- **User-Friendly Interface:**  
  An intuitive UI built with Streamlit, allowing users to simply enter a topic and instantly receive a comprehensive course plan.

- **AI-Powered Content Generation:**  
  Uses advanced AI to generate detailed course outlines—including objectives, topics, and descriptions—as well as engaging introductory video scripts.

- **Future Enhancements:**  
  Upcoming features include AI video generation to transform the intro video script into engaging videos, interactive course customization options, expanded subject coverage, and user feedback integration.

## Live Demo

Try out the live app here: [EduMorph App](https://edumorph.streamlit.app/)

## Installation

### Prerequisites

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- NVIDIA API integration via the `openai` Python package (configured for NVIDIA models)

### Steps

1. **Clone the Repository:**

    git clone https://github.com/yourusername/edumorph.git  
    cd edumorph

2. **Setup Virtual Environment (Optional but Recommended):**

    python -m venv .venv  
    source .venv/bin/activate  
    (On Windows: .venv\Scripts\activate)

3. **Install Dependencies:**

    pip install -r requirements.txt

## Configuration

### Secrets Setup

Create a folder named `.streamlit` in the root of your project and add a `secrets.toml` file with the following content:

    nvapi_key = "YOUR_API_KEY_HERE"

Replace `"YOUR_API_KEY_HERE"` with your actual NVIDIA API key.

## Usage

Run the application with:

    streamlit run main.py

The app will open in your default web browser. Enter a subject or topic to generate a structured course plan outline, while the accompanying video script is stored for future use.

## Project Structure

    edumorph/
    ├── .streamlit/
    │   └── secrets.toml       # API key configuration
    ├── main.py                # Main Streamlit application
    ├── requirements.txt       # List of dependencies
    └── README.md              # Project documentation

## Future Enhancements

- **AI Video Generation:**  
  Transform the generated intro video script into an engaging video using AI-powered video generation techniques.

- **Interactive Course Customization:**  
  Allow users to customize the generated course plan to better suit their learning preferences.

- **Expanded Subject Coverage:**  
  Integrate additional AI models and datasets to cover a wider range of educational topics.

- **User Feedback Integration:**  
  Implement a feedback system to improve the generated content based on user suggestions and reports.

Happy Learning with EduMorph!

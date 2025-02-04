# Sentence Cloud Generator

This project is a web application that generates a word cloud from user-provided sentences. It groups similar sentences and visualizes them in a word cloud format.

## Features

- Input sentences via a web form.
- Adjust similarity threshold to group similar sentences.
- Generate a word cloud based on the frequency of grouped sentences.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/aatuodcrd/sentences-cloud.git
    cd sentence-cloud-generator
    ```

2. Create and activate a conda environment:
    ```sh
    conda create --name sentence-cloud-env python=3.9
    conda activate sentence-cloud-env
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your Groq API key:
    ```env
    GROQ_API_KEY=your_groq_api_key
    ```
    You can generate your API key at [Groq Console](https://console.groq.com/keys).

## Usage

1. Run the Flask application:
    ```sh
    python main.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Enter sentences in the provided text area, adjust the similarity threshold if needed, and click "Generate Cloud".

## Project Structure

- `main.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the web interface.
- `utils/similarity.py`: Contains functions for grouping similar sentences.
- `utils/sentence_prompt.py`: Contains the prompt template for generating sentences.
- `utils/default_sentences.py`: Contains a list of default sentences.
- `requirements.txt`: Lists the required Python packages.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `.env`: Environment file containing the Groq API key.
# DataQuest : Conversational Data Analysis with Streamlit and PandasAI

https://github.com/user-attachments/assets/1bdd9a41-058d-4466-a1ef-1d6142fbd77d.mp4

![Screenshot 2024-10-23 191506](https://github.com/user-attachments/assets/a5d5fb9c-a91e-41b0-b7b2-5a4af7b12f52)
![Screenshot 2024-10-23 211300](https://github.com/user-attachments/assets/1904b11f-76d8-4e28-903d-cb30791f47d9)


## Overview

DataQuest is an interactive Streamlit application designed to process and analyze CSV files, providing meaningful insights through data visualizations and conversational interactions. This project integrates powerful AI models like Llama 3 and Ollama for natural language processing and PandasAI for intelligent data analysis. Users can interact with the data either via text or voice, making the exploration process more intuitive and user-friendly.

### Key Features:
- **CSV File Upload and Analysis**: Seamlessly upload CSV files and analyze the data through an intuitive dashboard.
- **Conversational Interface**: Interact with your data using text or voice commands, querying the dataset in natural language.
- **Interactive Visualizations**: Utilize Plotly to generate dynamic and interactive graphs.
- **Speech Recognition**: Implement voice commands for hands-free data querying and analysis.
- **Natural Language Processing**: Leverage Llama 3 and Ollama models for enhanced conversational understanding and generating insights from your data.

## Requirements

To run DataQuest, the following libraries are required:

- **Streamlit**: Web application framework for building interactive data applications.
- **Plotly**: Library for creating interactive graphs and visualizations.
- **Pandas**: Powerful data manipulation and analysis library.
- **NLTK**: Natural Language Toolkit for processing and analyzing text.
- **Pyttsx3**: Text-to-speech library for reading insights aloud.
- **SpeechRecognition**: For speech-to-text processing to enable voice commands.
- **PyAudio**: For capturing audio input from the microphone for voice commands.
- **PandasAI**: Integrates AI capabilities into Pandas for intelligent data analysis.
- **Ollama and Llama 3**: AI models for natural language understanding and interaction.

## Installation

### Step 1: Clone the Repository
```bash
[git clone https://github.com/your-username/AIplot.git](https://github.com/Raheesp/DataQuest.git)
cd AIplot
```

### Step 2: Create and Activate a Virtual Environment
Create a virtual environment to keep your dependencies isolated.

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### Step 3: Install the Required Libraries
```bash
pip install streamlit plotly pandas nltk pyttsx3 SpeechRecognition pyaudio pandasai
```

### Step 4: Install and Set Up Llama 3 and Ollama
Follow the installation guides for [Llama 3](https://llama.com) and [Ollama](https://ollama.com). Ensure these models are properly installed and accessible from your environment.

### Step 5: Install PyAudio
For speech recognition to work, you'll need to ensure PyAudio is installed correctly. For Windows users, you may need to download the appropriate wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

## How to Run AIplot

1. **Start the Application**  
   Launch the Streamlit app by running the following command:
   ```bash
   streamlit run app.py
   ```

2. **Upload Your CSV File**  
   Once the app is running, you will be prompted to upload a CSV file. The application will load and display the data in a table format.

3. **Conversational Interaction**  
   - Use the **Text Input** box to type queries, such as "Show the top 5 rows" or "What is the average sales for 2023?"

4. **Data Visualization**  
   The app uses Plotly to create real-time, interactive graphs. Visualizations will update based on your inputs or queries, allowing you to explore the data dynamically.

## Working Explanation

- **Natural Language Querying**: DataQuest uses Llama 3 and Ollama to process and understand user queries in natural language, allowing users to interact with their data seamlessly.
- **AI-Powered Data Analysis**: PandasAI is integrated to assist in data manipulation and insight generation, leveraging AI to enhance the analysis.
- **Visualization**: With Plotly, the app generates dynamic graphs and plots based on user-selected filters or queries, making it easier to interpret the results visually.

## Troubleshooting

1. **PyAudio Installation Issues**  
   If you encounter issues with installing PyAudio, refer to the [PyAudio section on PyPI](https://pypi.org/project/PyAudio/) or download the appropriate wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

2. **Streamlit File Upload Size Limit**  
   By default, Streamlit limits the size of file uploads. To modify this, update the `config.toml` file in `~/.streamlit/` to allow larger file uploads.

3. **Microphone Access**  
   If the microphone is not detected, check your system settings to ensure Python has permission to access your microphone.

## Future Enhancements

- Expanding support for more file types such as Excel and JSON.
- Adding advanced AI models to perform deeper data analysis.
- Improving voice command capabilities to support more complex queries.

## Contributing

We welcome contributions! To contribute to AIplot:
1. Fork the repository.
2. Create a new feature branch.
3. Submit a pull request with your changes.










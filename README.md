# YouTube Transcript Analyzer with Generative AI  

This project leverages Streamlit, Google's Gemini LLM, and the `youtube-transcript-api` library to provide a powerful tool for analyzing YouTube video transcripts. Users can input a YouTube video link, and the application extracts the transcript and allows various operations using Google's generative AI.  

## Features  
- **Input YouTube Link**: Users can input a YouTube link, and the application extracts the video ID using regex.  
- **Fetch Transcript**: Automatically retrieves the transcript using the `youtube-transcript-api`.  
- **LLM Operations**:
  - **Summarize**: Provides a concise summary of the video content.  
  - **Make Notes**: Generates structured notes from the transcript.  
  - **Custom Prompt**: Allows the user to give their own prompt for the LLM to process the transcript.  
- **Interactive Interface**: Built with Streamlit for an intuitive and easy-to-use interface.  

## Installation  

### Prerequisites  
- Python 3.8 or higher  
- An API key for Google's Generative AI (Gemini)  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/your-repo-name.git  
   cd your-repo-name  

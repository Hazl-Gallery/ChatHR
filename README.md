# ChatHR - Your Virtual HR Assistant

ChatHR is a Streamlit-based application that leverages OpenAI's GPT models to analyze and summarize resumes, helping HR professionals streamline their candidate review process.

## Features

- **Resume Analysis**: Extract key information from resumes in PDF or DOCX formats
- **Job Description Matching**: Compare candidate qualifications against job requirements
- **Candidate Ranking**: Rate multiple candidates on a scale of 1-10 based on job fit
- **Customizable Analysis**: Tailor the analysis query to focus on specific aspects
- **Secure API Key Management**: Store and manage your OpenAI API keys securely

## Sample Output

When you provide a job description and multiple resumes, ChatHR will:
1. Summarize the key requirements from the job description
2. Rate each candidate based on their match to the requirements
3. Provide individual summaries for each candidate

## Installation

### Prerequisites
- Python 3.11 or higher
- OpenAI API key

### Local Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/chathr.git
   cd chathr
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run app.py
   ```

### Docker Deployment

You can also deploy ChatHR using Docker:

1. Build the Docker image:
   ```
   docker build -t chathr .
   ```

2. Run the container:
   ```
   docker run -p 8501:8501 chathr
   ```

3. Access the application at http://localhost:8501

## Usage

1. **Add your OpenAI API Key**:
   - Enter a name and your API key in the sidebar
   - Click "Save New Key"

2. **Enter Job Description**:
   - Paste or type the job description in the designated text area
   - Sample job descriptions are included in the download

3. **Upload Resumes**:
   - Upload one or multiple resumes in PDF or DOCX format
   - Sample resumes are included in the download

4. **Customize Your Query** (optional):
   - Modify the default query in the "Ask ChatHR" text area

5. **Generate Analysis**:
   - Click the "chat" button to analyze the resumes

6. **Review Results**:
   - ChatHR will provide a summary of the job requirements, candidate rankings, and individual candidate summaries

## Sample Files

ChatHR includes sample files to help you get started:
- Job description for a Data Scientist position
- Sample resumes in both PDF and DOCX formats

To access these samples, click the "Download Samples" button in the sidebar.

## Default Query

The default analysis query asks ChatHR to:
```
Firstly, summarize the job description listing all required skills. 
Secondly, rate each candidate's qualifications against the job description on a scale from 1 to 10, 
where 1 is the least fit and 10 is the best fit. 
Lastly, write a summary for each candidate.
```

You can customize this query to focus on specific aspects of candidate evaluation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- This project is developed and maintained by [Hazl AI](https://hazl.ca/)
- Powered by OpenAI's GPT models 
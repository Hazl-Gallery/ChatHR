import streamlit as st
# st.set_page_config(layout="wide")
import os
from PyPDF2 import PdfReader
from docx import Document
import openai
openai.api_key = os.getenv('OPENAI_API_KEY')

from io import StringIO

st.set_page_config(
    page_title= "ChatHR by HAZEL",
    layout = "wide",
)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


def read_pdf(file_path):
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages)
    combined_text = ""

    for i in range(number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        if i == 0:
            combined_text = text
        else:
            combined_text += "\n" + text
    return combined_text

def read_docx(file_path):
    doc = Document(file_path)
    combined_text = ""

    for i, paragraph in enumerate(doc.paragraphs):
        if i == 0:
            combined_text = paragraph.text
        else:
            combined_text += "\n" + paragraph.text
    return combined_text

def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a human resource assistant."},
            {"role": "user", "content": prompt},
        ],
        n= 1,
        temperature=1,

    )
    text = response['choices'][0]['message']['content']
    return text

def main():
    
    st.sidebar.markdown('''

        Powered by ChatGPT, ChatHR (Beta) can help you summarize 
        resumes, greatly shortening the lengthy candidate 
        review process. Due to the token size limit of 
        approximately 4000 words, we recommend starting with 
        3 resumes and increasing the number accordingly.\n 
        To help you get started, plesae download the sample 
        job description and resume files. 

    ''')


    with open('samples/samples.zip','rb') as file:
        download_btn = st.sidebar.download_button(
            label = 'Download Samples',
            data = file,
            file_name = 'samples.zip',
        ) 

    st.title('ChatHR - Your Virtual HR Assistant')

    # with open('samples/job.txt', 'r') as file:
    #     job_info_sample = file.read()


    job_info = st.text_area(
        label = '**:orange[Job Description]**',
        # value = job_info_sample,
        height = 200

    )


    files = st.file_uploader(
        label = "**:orange[Upload Resumes]**", 
        type = ['pdf', 'docx'],
        accept_multiple_files = True
    )

    ask_text = '''Firstly, summarize the job description
      listing all required skills. Secondly, rate each 
      candidate's qualifications against the job description 
      on a scale from 1 to 10, where 1 is the least fit 
      and 10 is the best fit. Lastly, write a summary 
      for each candidate.
    '''
    ask_text = ask_text.replace('\n', ' ')
    ask_text = ' '.join(ask_text.split())

    question = st.text_area(
        label = '**:orange[Ask ChatHR]**',
        value = ask_text
    )

    btn = st.button('chat')

    if btn:
        resume_bucket = []
        for fi in files:
            file_ext = os.path.splitext(fi.name)[1]
            if file_ext == '.pdf':
                resume_str = read_pdf(fi)
            elif file_ext == '.docx':
                resume_str = read_docx(fi)
            else:
                raise ValueError('Unsupported file extension')

            resume_bucket.append(resume_str)


        prompt = '''
            You are a human resource assistant. You will
            be first given a job description, then followed by candidates' resumes. 
            The task will be given at the end.
        '''


        prompt = prompt + '\n' + 'JOB DESCRIPTION: ' + job_info + '\n\n'
        for idx, resume in enumerate(resume_bucket):
            count = idx + 1
            prompt = prompt + 'CANDIDATE RESUME #{}: '.format(count) + '\n\n' + resume +'\n\n'

        prompt = prompt + 'THE TASK IS:' + '\n\n' + question

        # st.write(prompt)
        # # # print(prompt)

        # st.write('================================================================')
        res = chat(prompt)
        print(res)
        st.write(res)

if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print (e)
        st.error(e)

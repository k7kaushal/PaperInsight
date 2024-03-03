## PaperInsight : Chat with any scientific document

### Problem Statement : Chat with any scientific document 
### Document format supported : .pdf , .pptx, .docx, .txt 
### Introduction : <br>
> Documents are fundamental to research and professional 
communication, but existing solutions primarily focus on parsing PDF 
files. This leaves a gap in handling diverse formats like DOCX, TEX, and 
PPT, hindering efficient information extraction. <br>
> Our project aims to develop a robust framework to parse multiple formats 
beyond PDF, integrated with language models for intuitive user interaction 
and query answering. <br>
> This will streamline document analysis and knowledge dissemination, 
fostering a more efficient ecosystem for research and collaboration. <br>

### There are several compelling reasons to choose our solution: 
> Comprehensive Format Support: Our solution offers support for a wide range of document 
formats, including PDF, TXT, PPTX,Tex and DOCX. This ensures versatility and flexibility, 
allowing users to work with documents in their preferred formats without constraints. <br>
> Advanced Language Model Integration: We integrated Gemini 1.0 Pro, a powerful language 
model, into our solution. This enables advanced natural language understanding capabilities, 
including document analysis, summarization, and query answering. Users can leverage 
Gemini 1.0 Pro to gain valuable insights from their documents quickly and accurately. <br>
> User-Friendly Interface: Our solution features a user-friendly web-based interface developed 
using Streamlit and Django frameworks. This interface makes it easy for users to upload 
documents, input queries, and interact with the system seamlessly. The intuitive design 
enhances user experience and productivity. <br>

### Nougat pipeline flow for parsing documents:  
![image](https://github.com/k7kaushal/PaperInsight/assets/82771451/4364c1ae-c9b0-4aed-bd03-eb5ce34dbdcf)

### Interface: 
![image](https://github.com/k7kaushal/PaperInsight/assets/82771451/c3bcd715-9731-418f-a65f-c8dc8cad6221) <br></br>
Initial stage working demo: https://drive.google.com/file/d/1bZftENO0wlf9DJcHVDgVy2XpYyaDtqLg/view?usp=drive_link <br></br>

### Project setup

> The first thing to do is to clone the repository: (https://github.com/k7kaushal/PaperInsight.git) <br>
> Install requirements using: <br>
`pip install -r requirements.txt`
> Once pip has finished installing the requirements:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
> Optional :
``` python manage.py createsuperuser ``` <br>
Enter username, email address and password and login at http://127.0.0.1:8000/admin with these credentials for admin access. <br>
> Navigate to http://127.0.0.1:8000/

### Recognition: Mined hackathon hosted by Nirma University, Ahmedabad, Gujarat, India and sponsored by the Binghamton University
First place winners in Cactus track <br>
Third place winners in Grand prize winners among all tracks






!pip install -qq nougat-ocr
!pip -q install langchain openai tiktoken


from nougat.utils.checkpoint import get_checkpoint
CHECKPOINT = get_checkpoint('nougat')

import subprocess
import uuid
import requests
import re

# Download pdf from a given link
def get_pdf(pdf_link):
  # Generate a unique filename
  unique_filename = f"/content/input/downloaded_paper_{uuid.uuid4().hex}.pdf"

  # Send a GET request to the PDF link
  response = requests.get(pdf_link)

  if response.status_code == 200:
      # Save the PDF content to a local file
      with open(unique_filename, 'wb') as pdf_file:
          pdf_file.write(response.content)
      print("PDF downloaded successfully.")
  else:
      print("Failed to download the PDF.")
  return unique_filename


# Run nougat on the pdf file
def nougat_ocr(file_name):

  # Command to run
  cli_command = [
      'nougat',
      '--out', 'output',
      'pdf', file_name,
      '--checkpoint', CHECKPOINT,
      '--markdown'
  ]

  # Run the command
  subprocess.run(cli_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

  return


# predict function / driver function
def paper_read(pdf_file=None, pdf_link=None):
  if pdf_file is None:
    if pdf_link == '':
      print("No file is uploaded and No link is provided")
      return "No data provided. Upload a pdf file or provide a pdf link and try again!"
    else:
      file_name = get_pdf(pdf_link)
  else:
    file_name = pdf_file

  nougat_ocr(file_name)

  # Open the file for reading
  file_name = file_name.split('/')[-1][:-4]
  with open(f'/content/output/{file_name}.mmd', 'r') as file:
      content = file.read()

  return content

import os
os.makedirs('input', exist_ok=True)
os.makedirs('output', exist_ok=True)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# content = paper_read("/content/input/2205.14135.pdf")
# print(content)

# Specify the filename
filename = "/content/flash_attention.txt"

# Open the file in write mode ('w') and write the string to it
with open(filename, 'w') as file:
    file.write(content)

# Commented out IPython magic to ensure Python compatibility.
# %%time
    #If the user provides with a link
# content = paper_read(None, 'https://arxiv.org/pdf/2309.03883v1.pdf')
# print(content)

## Remove references
import re
refs_re = re.compile(r'(References|REFERENCES)')
noref_content = refs_re.split(content)[0]
print(len(noref_content), len(content))

noref_content

"""As shown above the model has converted the paper to Latex. Typical PDF readers convert the PDF to text where all information about the tables and mathematical equations is lost


"""


import urllib.request
import shutil

# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg') as response, open('plik2', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
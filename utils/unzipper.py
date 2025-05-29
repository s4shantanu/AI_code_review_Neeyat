import zipfile
import os

def unzip_code(zip_path, extract_to='temp_project'):
    if os.path.exists(extract_to):
        return extract_to
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return extract_to

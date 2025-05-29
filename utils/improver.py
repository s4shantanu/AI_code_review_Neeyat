import os
import subprocess
import shutil

def improve_code(input_path, output_path='output/improved_project'):
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    shutil.copytree(input_path, output_path)

    for root, _, files in os.walk(output_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                subprocess.run(['autopep8', '--in-place', '--aggressive', file_path])
    return output_path

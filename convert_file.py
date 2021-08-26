import subprocess

def convert(file_name_in, file_name_out):
    subprocess.Popen(["pandoc", file_name_in, "-o", file_name_out])
    return print("File converted")

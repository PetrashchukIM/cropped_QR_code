for the normal operation of both scripts there are the following key directories

"input_all_qr_code" - Here you should upload the number of files you need to process
"output_QR" - are created and updated automatically. The generated pdf is displayed here
"output_QR_code" -are created and updated automatically. These are the technical directories that are required for the scripts to work.
"temp" -are created and updated automatically. These are the technical directories that are required for the scripts to work.
"template_background" -are created and updated automatically. These are the technical directories that are required for the scripts to work.

these directories, as well as files and they do not need to be opened by third-party programs and

for WINDOWS 10(64 bit), 11(64 bit)

if you're using Windows, you just need to run "first_run.bat" as an administrator.
It will install Python for you if it is not there and will install the necessary libraries

for Linux, MacOS
1.Install the latest version of python
    https://www.python.org/downloads/
2.install pip
    sudo apt update
    sudo apt install python3-pip
3.install the libraries
    pip install opencv-python Pillow reportlab
4.Run the script qr-code.py
5.Run the script create_pdf.py

You can also run the scripts individually manually if you already have paytne and the necessary libraries installed
---
# Task-2 ---- Pixelated Problem solver
---

It scans an simple algebraic expression like 2+2 and outputs the answer.

---

## Steps before running the python program.

We should install an virtual environment in-order to make this work.Steps to install an virtual machine.

1.Make sure you have installed the latest version of python.
`python3 --version`

2.Install the venv module by using the command, `sudo apt install python3-venv`

3.To create a virtual environment in your system use the command, `python3 -m venv <env_name>`.(Make sure to create the virtual environment in the same directory as the file)

4.In order to activate the virtual environment in your system use the command, `source <env_name>/bin/activate`.

---

## Steps required to run the program.

1.First clone this repository into your local machine

2.Make sure to create a virtual environment in your system in the same directory as the file and activate the virtual enviroment.

3.Make sure to download the libraries given below in-order for the program to work

4.After activating the virtual environment, we need to download the libraries

`pip install pytesseract`

`pip install pillow`

`sudo apt update`

`sudo apt install tesseract-ocr`

5.Now run the file "pyt.py" using the command `python3 pyt.py`

6.As there is 2 images, you can check with both the images.Just change the name of the image.(If image is not in the same directory then u need to specify the full location of the image)

## Note: Make sure that tesseract installs in the default location or you need to change its location.

The default location for tesseract to install is

Ubuntu:`/usr/bin/tesseract`

Windows:`C:\Program Files\Tesseract-OCR\tesseract.exe`

Mac OS:`/usr/local/bin/tesseract`

You can find the location of the tesseract using the command, `which tesseract` or for windows its `where tesseract`

---

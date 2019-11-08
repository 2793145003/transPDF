#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import io
import certifi
import urllib.request as urllib
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from docx import Document
from googletrans import Translator
def google_translate(content):
    translator = Translator()
    return translator.translate(content, dest='zh-CN').text

def read_from_pdf(path):
    with open(path, 'rb') as file:
        resource_manager = PDFResourceManager()
        return_str = io.StringIO()
        lap_params = LAParams()

        device = TextConverter(
            resource_manager, return_str, laparams=lap_params)
        process_pdf(resource_manager, device, file)
        device.close()

        content = return_str.getvalue()
        return_str.close()
        return content

def remove_control_characters(content):
    mpa = dict.fromkeys(range(32))
    return content.translate(mpa)

def save_text(content):
    doc = open('result.txt','w')
    for line in content.split('\n'):
        line = remove_control_characters(line)
        doc.write(line + "\n")
        trans = remove_control_characters(google_translate(line))
        doc.write(trans + "\n")
    doc.close()

def pdf_to_cn(pdf_file_path):
    content = read_from_pdf(pdf_file_path)
    content = content.replace("-\n", "").replace(".\n", ".回车").replace("\n", " ").replace("回车", "\n").replace("ﬁ", "fi")
    save_text(content)

def main():
    print("Downloading...")
    url = "https://arxiv.org/pdf/1810.03243.pdf"
    data = urllib.urlopen(url, cafile=certifi.where()).read()
    f = open("tmp.pdf", "wb")
    f.write(data)
    f.close()
    print("Downloaded.")

    file = "tmp.pdf"
    extension_name = os.path.splitext(file)[1]
    if extension_name != '.pdf':
        return
    pdf_file = file
    print('正在处理: ', file)
    pdf_to_cn(pdf_file)

if __name__ == '__main__':
    main()
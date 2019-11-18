#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import io
import fitz
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
    try:
        return translator.translate(content, dest='zh-CN').text
    except:
        try:
            translator.translate("English", dest='zh-CN').text
            print("Google is fine.")
            return "Unknown."
        except:
            print("Google is down.")
            return "Google down."

def clear_txt(txt):
    return txt.replace("-\n", "").replace("\n", " ")

def pdf_to_cn(pdf_file_path):
    result = open('result.txt','w')
    doc = fitz.open(pdf_file_path)
    for page in doc:
        blocks = page.getText("blocks")
        for txt in blocks:
            line = clear_txt(txt[4])
            result.write(line + "\n")
            trans = google_translate(line)
            result.write(trans + "\n")
    result.close()

def main():
    print("Downloading...")
    url = "https://www.ipol.im/pub/art/2012/gjmr-lsd/article.pdf"
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
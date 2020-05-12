#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import io
import fitz
import certifi
import urllib.request as urllib
from translate import translate

def clear_txt(txt):
    return txt.replace("-\n", "").replace("\n", " ")

def pdf_to_cn(pdf_file_path):
    result = open('result.html','w')
    doc = fitz.open(pdf_file_path)
    for page in doc:
        # blocks = page.getText("blocks")
        # for txt in blocks:
        #     line = clear_txt(txt[4])
        #     result.write(line + "\n")
        #     trans = translate(line)
        #     result.write(trans + "\n")
        for line in page.getText("xhtml").splitlines():
            result.write(line + "\n")
    result.close()

def main():
    print("Downloading...")
    url = "pdf_url.pdf"
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
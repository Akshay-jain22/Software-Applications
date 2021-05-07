from PyPDF2 import PdfFileMerger
import os
from tkinter import *
from tkinter import filedialog
import os
import sys

# Function for relative paths
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Setup Root
root = Tk()
root.title("PDF Merger")
root.geometry("300x110")
root.resizable(False, False)
root.iconbitmap(resource_path("Merge Pdfs - Icon.ico"))

def mergePDF():
    DIRECTORY_NAME = filedialog.askdirectory()

    if(len(DIRECTORY_NAME)>1):
        locError.config(text=DIRECTORY_NAME, fg="green")
    else:
        locError.config(text="Please Choose Folder", fg="red")
        return

    try:
        merger = PdfFileMerger()
        items = os.listdir(DIRECTORY_NAME)
        if len(items) == 0:
            locError.config(text="Empty Folder", fg="red")
            return
        
        for item in items:
            if item.endswith('.pdf'):
                merger.append(DIRECTORY_NAME + "/" + item)

        merger.write(DIRECTORY_NAME + "/Merged_pdf.pdf")
        merger.close()
        locError.config(text="Successfully Merged : Merged_pdf.pdf", fg="green")
    
    except:
        locError.config(text="Cannot Merge the PDFs", fg="red")
    

label = Label(root, text="Select the Folder", font=('jost', 15))
label.pack(pady=5)

selectFolder = Button(root, bg="red", fg="white", text=" Choose Folder ", command=mergePDF)
selectFolder.pack(pady=5)

locError = Label(root, text="", fg="red", font=('jost', 10))
locError.pack(pady=5)

root.mainloop()
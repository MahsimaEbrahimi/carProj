import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF
from PIL import Image, ImageTk
import arabic_reshaper
from bidi.algorithm import get_display

# Function to render a preview of the first page
def preview_pdf(pdf_output):
    pdf_document = fitz.open(stream=pdf_output, filetype="pdf")
    page = pdf_document.load_page(0)
    pix = page.get_pixmap()
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return image

# Function to save the PDF to a file
def save_pdf(pdf_output):
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                             filetypes=[("PDF files", "*.pdf")])
    if file_path:
        with open(file_path, "wb") as f:
            f.write(pdf_output.getbuffer())
        print(f"فایل در {file_path} ذخیره شد")

# Setting up the tkinter GUI
def show_preview(pdf_output):
    # Render the PDF preview
    image = preview_pdf(pdf_output)
    
    # Display the image in a tkinter window
    root = tk.Tk()
    root.title("پیش نمایش پرینت")

    img_tk = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=img_tk)
    label.pack()

    # Save button
    save_button = tk.Button(root, text="ذخیره فایل", command=lambda: save_pdf(pdf_output))
    save_button.pack()

    root.mainloop()

def process_rtl_text(text):
    reshaped_text = arabic_reshaper.reshape(text)  # Reshape the text for proper ligatures
    bidi_text = get_display(reshaped_text)  # Apply bidi algorithm to get proper display
    return bidi_text
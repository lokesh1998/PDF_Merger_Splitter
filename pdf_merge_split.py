import PyPDF2
from tkinter import filedialog
import tkinter as tk
import shutil
import os

filepath = []
window = tk.Tk()
window.title( 'Merge/ Split PDFs' )
window.geometry( "300x200+10+10" )


def clear_output_folder():
    # Clear the output folder contents
    if os.path.exists( f'{os.getcwd()}' + '\\output' ):
        shutil.rmtree( f'{os.getcwd()}' + '\\output' )
    if not os.path.exists( f'./output_pdf' ):
        os.makedirs( f'./output_pdf' )


def merge_files():
    # merge the files browsed
    clear_output_folder()
    merger = PyPDF2.PdfFileMerger()
    filepath = list( filedialog.askopenfilenames( parent=window,
                                                  initialdir=os.getcwd(),
                                                  title="Please select one or more files:",
                                                  filetypes=[('PDF', '*.pdf')] ) )
    for pdf in filepath:
        merger.append( pdf )
    merger.write( './output_pdf/merger.pdf' )


def split_files():
    # split the files selected
    clear_output_folder()
    filepath = list( filedialog.askopenfilenames( parent=window,
                                                  initialdir=os.getcwd(),
                                                  title="Please select one or more files:",
                                                  filetypes=[('PDF', '*.pdf')] ) )

    for pdf in filepath:
        template = PyPDF2.PdfFileReader( open( pdf, 'rb' ) )
        for i in range( template.getNumPages() ):
            writer = PyPDF2.PdfFileWriter()
            page = template.getPage( i )
            writer.addPage( page )
            pdf_name = os.path.basename( pdf ).split( '.pdf' )[0]
            with open( f'./output_pdf/{pdf_name}_{i + 1}.pdf', 'wb' ) as new_file:
                writer.write( new_file )


btn1 = tk.Button( window, text='Browse for Merging', command=lambda: merge_files() )
btn2 = tk.Button( window, text='Browse for Split', command=lambda: split_files() )
btn1.pack()
btn2.pack()
window.mainloop()

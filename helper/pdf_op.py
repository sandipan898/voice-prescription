from fpdf import FPDF
  
def save_pdf(text):  
    # save FPDF() class into a 
    # variable pdf
    pdf = FPDF()
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 12)
    
    # create a cell
    pdf.cell(
        200, 10, 
        txt = "Prescription", 
        ln = 1, align = 'C'
    )

    # add another cell
    pdf.cell(
        200, 10, 
        txt = text,
        ln = 2, align = 'C'
    )
    
    # save the pdf with name .pdf
    pdf.output("Prescription.pdf")
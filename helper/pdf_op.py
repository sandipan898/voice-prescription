from fpdf import FPDF
  
def save_pdf(medicines):  
    # save FPDF() class into a 
    # variable pdf
    pdf = FPDF()
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 12)
    pdf.cell(
            200, 10, 
            txt = "Generated Prscription", 
            ln = 1, align = 'C'
        )
    for medicine in medicines:
        print(medicines[medicine]["Medicine Name"])
        
        # create a cell
        pdf.cell(
            200, 10, 
            txt = medicine, 
            ln = 1, align = 'C'
        )

        pdf.cell(
            200, 10, 
            txt = "Medicine Name: " + medicines[medicine]["Medicine Name"],
            ln = 2,
        )
        pdf.cell(
            200, 10, 
            txt = "Instruction to use: " + medicines[medicine]["Medicine Instruction"],
            ln = 2,
        )
    
    # save the pdf with name .pdf
    pdf.output("Prescription.pdf")
import pdfplumber  
import pandas as pd  

def pdf_to_excel(pdf_file, excel_file):  
    # Open the PDF file using pdfplumber  
    with pdfplumber.open(pdf_file) as pdf:  
        all_tables = []  
        
        # Iterate through each page of the PDF  
        for page in pdf.pages:  
            # Extract tables from the current page  
            tables = page.extract_tables()  
            
            # Iterate through each table extracted from the page  
            for table in tables:  
                if table:   
                    # Create a DataFrame from the table  
                    df = pd.DataFrame(table)  
                    all_tables.append(df)  # Append the DataFrame to the list  

        # Check if no tables were found and append a message if true  
        if not all_tables:  
            all_tables.append(pd.DataFrame([["No Table Found"]]))  
        
        # Write all DataFrames to an Excel file  
        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:  
            for idx, df in enumerate(all_tables):  
                df.to_excel(writer, sheet_name=f'sheet{idx + 1}', index=False)  

# Call the function to convert PDF to Excel  
pdf_to_excel('myfile.pdf', 'myfile.xlsx')

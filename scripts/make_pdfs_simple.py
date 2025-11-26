# make_pdfs_simple.py
# Simple PDF generator using pypandoc with wkhtmltopdf
import os
import pypandoc

SRC_DIR = os.path.join(os.path.dirname(__file__), 'docs')
OUT_DIR = os.path.join(os.path.dirname(__file__), 'docs_pdf')

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

files = [f for f in os.listdir(SRC_DIR) if f.endswith('.md')]

print("Converting Markdown files to PDF...\n")

for f in files:
    src = os.path.join(SRC_DIR, f)
    out_pdf = os.path.join(OUT_DIR, f.replace('.md', '.pdf'))
    
    try:
        # Try PDF with wkhtmltopdf
        pypandoc.convert_file(
            src, 
            'pdf', 
            outputfile=out_pdf,
            extra_args=['--pdf-engine=wkhtmltopdf']
        )
        print(f'✓ Created PDF: {f.replace(".md", ".pdf")}')
    except Exception as e:
        # Fallback to HTML
        print(f'⚠ PDF failed for {f}, creating HTML instead')
        out_html = os.path.join(OUT_DIR, f.replace('.md', '.html'))
        pypandoc.convert_file(
            src, 
            'html', 
            outputfile=out_html,
            extra_args=['--standalone', '--css=style.css']
        )
        print(f'✓ Created HTML: {f.replace(".md", ".html")}')

print('\n✓ Done! Files saved to docs_pdf/')
print('\nNote: To generate PDF files, install wkhtmltopdf:')
print('  winget install wkhtmltopdf')

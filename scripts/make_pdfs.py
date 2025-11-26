# make_pdfs.py
# Requires: pypandoc + pandoc installed on system
import pypandoc
import os

SRC_DIR = os.path.join(os.path.dirname(__file__), 'docs')
OUT_DIR = os.path.join(os.path.dirname(__file__), 'docs_pdf')

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

files = [f for f in os.listdir(SRC_DIR) if f.endswith('.md')]

for f in files:
    src = os.path.join(SRC_DIR, f)
    out_pdf = os.path.join(OUT_DIR, f.replace('.md', '.pdf'))
    try:
        pypandoc.convert_file(src, 'pdf', outputfile=out_pdf)
        print('Created:', out_pdf)
    except Exception as e:
        print('Failed to create PDF for', f, '— fallback: create HTML')
        out_html = os.path.join(OUT_DIR, f.replace('.md', '.html'))
        pypandoc.convert_file(src, 'html', outputfile=out_html)
        print('Created HTML:', out_html)

print('Done')

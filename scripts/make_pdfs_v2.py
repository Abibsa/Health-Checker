# make_pdfs_v2.py
# Alternative PDF generator using markdown2 + weasyprint or pdfkit
import os
import markdown2

SRC_DIR = os.path.join(os.path.dirname(__file__), 'docs')
OUT_DIR = os.path.join(os.path.dirname(__file__), 'docs_pdf')

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

# HTML template with better styling
HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            color: #333;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
        }}
        h3 {{
            color: #7f8c8d;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        pre {{
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        pre code {{
            background: none;
            padding: 0;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin-left: 0;
            color: #555;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #3498db;
            color: white;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
{content}
</body>
</html>
"""

files = [f for f in os.listdir(SRC_DIR) if f.endswith('.md')]

for f in files:
    src = os.path.join(SRC_DIR, f)
    
    # Read markdown
    with open(src, 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    # Convert to HTML
    html_content = markdown2.markdown(md_content, extras=['fenced-code-blocks', 'tables'])
    full_html = HTML_TEMPLATE.format(content=html_content)
    
    # Save HTML
    out_html = os.path.join(OUT_DIR, f.replace('.md', '.html'))
    with open(out_html, 'w', encoding='utf-8') as file:
        file.write(full_html)
    print(f'✓ Created HTML: {f.replace(".md", ".html")}')
    
    # Try to create PDF using weasyprint
    try:
        from weasyprint import HTML
        out_pdf = os.path.join(OUT_DIR, f.replace('.md', '.pdf'))
        HTML(string=full_html).write_pdf(out_pdf)
        print(f'✓ Created PDF: {f.replace(".md", ".pdf")}')
    except ImportError:
        print(f'⚠ weasyprint not installed. Install with: pip install weasyprint')
        print(f'  Skipping PDF for {f}')
    except Exception as e:
        print(f'⚠ Failed to create PDF for {f}: {e}')

print('\n✓ Done! Check the docs_pdf folder.')

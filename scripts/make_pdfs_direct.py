# make_pdfs_direct.py
# Direct PDF generation using markdown2 + wkhtmltopdf
import os
import subprocess
import markdown2

SRC_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs')
OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs_pdf')

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

# Improved HTML template with better PDF styling
HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        @page {{
            margin: 2cm;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.8;
            color: #333;
            font-size: 11pt;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 12px;
            margin-top: 0;
            font-size: 24pt;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
            font-size: 18pt;
            border-bottom: 1px solid #ddd;
            padding-bottom: 8px;
        }}
        h3 {{
            color: #7f8c8d;
            font-size: 14pt;
            margin-top: 20px;
        }}
        h4 {{
            color: #95a5a6;
            font-size: 12pt;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', Consolas, monospace;
            font-size: 10pt;
            color: #c7254e;
        }}
        pre {{
            background: #f8f8f8;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #3498db;
            overflow-x: auto;
            font-size: 9pt;
        }}
        pre code {{
            background: none;
            padding: 0;
            color: #333;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin-left: 0;
            color: #555;
            font-style: italic;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            font-size: 10pt;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}
        th {{
            background-color: #3498db;
            color: white;
            font-weight: 600;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 8px 0;
        }}
        strong {{
            color: #2c3e50;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #3498db;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            text-align: center;
            font-size: 9pt;
            color: #999;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <p style="color: #7f8c8d;">Health Checker - Rule-Based System</p>
    </div>
    {content}
    <div class="footer">
        <p>Generated from {filename} | Health Checker Documentation</p>
    </div>
</body>
</html>
"""

files = [f for f in os.listdir(SRC_DIR) if f.endswith('.md')]

print("🔄 Converting Markdown files to PDF...\n")

for f in files:
    src = os.path.join(SRC_DIR, f)
    
    # Read markdown
    with open(src, 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    # Convert to HTML
    html_content = markdown2.markdown(
        md_content, 
        extras=['fenced-code-blocks', 'tables', 'header-ids', 'code-friendly']
    )
    
    # Get title from first heading or filename
    title = f.replace('.md', '').replace('_', ' ').title()
    
    full_html = HTML_TEMPLATE.format(
        title=title,
        content=html_content,
        filename=f
    )
    
    # Save HTML first
    out_html = os.path.join(OUT_DIR, f.replace('.md', '.html'))
    with open(out_html, 'w', encoding='utf-8') as file:
        file.write(full_html)
    print(f'✓ Created HTML: {f.replace(".md", ".html")}')
    
    # Try to create PDF using wkhtmltopdf
    out_pdf = os.path.join(OUT_DIR, f.replace('.md', '.pdf'))
    wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    try:
        result = subprocess.run(
            [wkhtmltopdf_path, '--enable-local-file-access', out_html, out_pdf],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            print(f'✓ Created PDF: {f.replace(".md", ".pdf")}')
        else:
            print(f'⚠ wkhtmltopdf error for {f}: {result.stderr[:100]}')
    except FileNotFoundError:
        print(f'⚠ wkhtmltopdf not found in PATH. HTML created instead.')
        break
    except Exception as e:
        print(f'⚠ Error creating PDF for {f}: {str(e)[:100]}')

print('\n✅ Done! Check the docs_pdf folder.')
print(f'   Location: {os.path.abspath(OUT_DIR)}')

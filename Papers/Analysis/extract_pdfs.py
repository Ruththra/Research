import subprocess, sys

# Install PyPDF2 if needed
try:
    import PyPDF2
    print("PyPDF2 already installed")
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2", "-q"])
    import PyPDF2
    print("PyPDF2 installed")

files = [
    ("/home/ruththra/Desktop/Research/Papers/Analysis/2021-ACL/2021.findings-acl.297.pdf",
     "/home/ruththra/Desktop/Research/Papers/Analysis/2021-ACL/2021.findings-acl.297.txt"),
    ("/home/ruththra/Desktop/Research/Papers/Analysis/2022-ACL 01/2022.acl-long.404.pdf",
     "/home/ruththra/Desktop/Research/Papers/Analysis/2022-ACL 01/2022.acl-long.404.txt"),
    ("/home/ruththra/Desktop/Research/Papers/Analysis/2022-ACL 02/2022.acl-long.543.pdf",
     "/home/ruththra/Desktop/Research/Papers/Analysis/2022-ACL 02/2022.acl-long.543.txt"),
    ("/home/ruththra/Desktop/Research/Papers/Analysis/2022-EMNLP/2022.emnlp-main.481.pdf",
     "/home/ruththra/Desktop/Research/Papers/Analysis/2022-EMNLP/2022.emnlp-main.481.txt"),
]

for pdf_path, txt_path in files:
    print(f"Extracting: {pdf_path}")
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for i, page in enumerate(reader.pages):
                pt = page.extract_text()
                if pt:
                    text += pt + "\n"
        with open(txt_path, "w") as f:
            f.write(text)
        lines = text.count("\n") + 1
        print(f"  -> {lines} lines, {len(text)} chars saved to {txt_path}")
    except Exception as e:
        print(f"  ERROR: {e}")

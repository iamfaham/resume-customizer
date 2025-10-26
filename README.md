# Resume Customizer 🚀

AI-powered resume customization tool that uses Google Gemini API to tailor your resume for specific job descriptions. The tool generates professional LaTeX-formatted resumes that can be exported to PDF or Word format.

## Features ✨

- **AI-Powered Customization**: Uses Google Gemini API to intelligently adapt your resume
- **Multiple Input Formats**: Supports TXT, PDF, and DOCX resume files
- **Multiple Output Formats**: Generate PDF, Word (DOCX), or LaTeX source files
- **Professional LaTeX Template**: Clean, ATS-friendly resume template
- **Custom Instructions**: Add specific requirements for resume customization
- **Command-Line & Programmatic APIs**: Use via CLI or integrate into your Python code
- **Smart Content Tailoring**: Emphasizes relevant skills and experiences for target jobs

## Quick Start 🏃‍♂️

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd resume-customizer

# Install dependencies
pip install -e .
```

### 2. Set Up API Key

Get your free Google Gemini API key from: https://ai.google.dev/

```bash
# Linux/Mac
export GEMINI_API_KEY='your-api-key-here'

# Windows CMD
set GEMINI_API_KEY=your-api-key-here

# Windows PowerShell
$env:GEMINI_API_KEY='your-api-key-here'
```

Or create a `.env` file:

```
GEMINI_API_KEY=your-api-key-here
```

### 3. Install System Dependencies (Optional)

For **PDF generation**, install LaTeX:

- **Windows**: [MiKTeX](https://miktex.org/download)
- **Mac**: `brew install mactex`
- **Linux**: `sudo apt-get install texlive-full`

For **Word document generation**, install Pandoc:

- **Windows/Mac/Linux**: [Pandoc Downloads](https://pandoc.org/installing.html)

Check your setup:

```bash
python main.py check
```

## Usage 📖

### Command Line Interface

#### Basic Usage

```bash
python main.py customize my_resume.pdf job_description.txt output_resume.pdf
```

#### Specify Output Format

```bash
# Generate PDF (default)
python main.py customize resume.txt job.txt output.pdf --format pdf

# Generate Word document
python main.py customize resume.docx job.txt output.docx --format docx

# Generate LaTeX source only
python main.py customize resume.pdf job.txt output.tex --format tex
```

#### Add Custom Instructions

```bash
python main.py customize resume.pdf job.txt output.pdf \
  --instructions "Emphasize leadership experience and quantify all achievements"
```

#### Use Different Gemini Model

```bash
python main.py customize resume.pdf job.txt output.pdf \
  --model gemini-2.0-flash-exp
```

#### Check System Requirements

```bash
python main.py check
```

### Programmatic Usage

#### Basic Example

```python
from resume_customizer import ResumeCustomizer

# Initialize
customizer = ResumeCustomizer()

# Customize resume
result = customizer.customize_resume(
    resume_path='my_resume.pdf',
    job_description='job_description.txt',
    output_path='customized_resume.pdf',
    output_format='pdf'
)

if result['success']:
    print(f"✅ Resume generated: {result['output_file']}")
    print(f"📝 LaTeX source: {result['latex_file']}")
else:
    print(f"❌ Error: {result['error']}")
```

#### With Custom Instructions

```python
customizer = ResumeCustomizer()

result = customizer.customize_resume(
    resume_path='resume.txt',
    job_description='Full Stack Developer position at XYZ Corp...',
    output_path='output.pdf',
    output_format='pdf',
    custom_instructions="""
    - Highlight Python and React experience
    - Emphasize leadership and team collaboration
    - Use metrics where possible
    """
)
```

#### Simplified API

```python
from resume_customizer.app import customize_resume_simple

result = customize_resume_simple(
    resume_path='resume.pdf',
    job_description='job.txt',
    output_path='output.pdf',
    output_format='pdf'
)
```

### Run Examples

```bash
python test_example.py
```

## Project Structure 📁

```
resume-customizer/
├── resume_customizer/
│   ├── __init__.py           # Package initialization
│   ├── app.py                # Main application logic
│   ├── gemini_client.py      # Gemini API integration
│   ├── latex_template.py     # LaTeX resume template
│   ├── latex_converter.py    # PDF/DOCX conversion
│   └── resume_parser.py      # Resume file parser
├── main.py                   # CLI entry point
├── test_example.py           # Usage examples
├── pyproject.toml            # Project dependencies
├── .env.example              # Environment variable template
└── README.md                 # This file
```

## How It Works 🔧

1. **Parse Resume**: Extracts text from your current resume (TXT/PDF/DOCX)
2. **Parse Job Description**: Reads the target job description
3. **AI Generation**: Sends both to Google Gemini with professional instructions
4. **LaTeX Generation**: Receives customized resume in LaTeX format
5. **Format Conversion**: Converts to your desired output format (PDF/DOCX/TEX)

## API Key Setup 🔑

### Get Your API Key

1. Visit [Google AI Studio](https://ai.google.dev/)
2. Sign in with your Google account
3. Click "Get API Key"
4. Create a new API key or use an existing one

### Set Environment Variable

The tool automatically reads from the `GEMINI_API_KEY` environment variable. You can also:

- Pass the key directly when initializing: `ResumeCustomizer(api_key='your-key')`
- Use a `.env` file (requires `python-dotenv`)

## Supported Formats 📄

### Input Formats

- **Resume**: `.txt`, `.pdf`, `.docx`
- **Job Description**: Plain text or any of the above formats

### Output Formats

- **PDF**: Professional PDF document (requires LaTeX installation)
- **DOCX**: Microsoft Word document (requires Pandoc)
- **TEX**: LaTeX source code (no extra dependencies)

## Configuration ⚙️

### Gemini Models

You can use different Gemini models:

- `gemini-2.0-flash-exp` (default, fast and efficient)
- `gemini-2.5-flash` (latest flash model)
- `gemini-pro` (more capable for complex tasks)

### Custom LaTeX Template

You can provide your own LaTeX template:

```python
my_template = r"""
\documentclass{article}
...
"""

result = customizer.customize_resume(
    resume_path='resume.pdf',
    job_description='job.txt',
    output_path='output.pdf',
    template=my_template  # Not directly exposed, modify latex_template.py
)
```

## Troubleshooting 🔍

### "pdflatex not found"

Install LaTeX distribution for your OS (see Installation section)

### "Pandoc not found"

Install Pandoc from https://pandoc.org/installing.html

### "API key not set"

Make sure `GEMINI_API_KEY` environment variable is set or pass it directly

### "Resume content is too short"

Ensure your resume has at least 100 characters of actual content

### LaTeX Compilation Errors

- Check the saved `.tex` file for syntax errors
- View the LaTeX log file for detailed error messages
- Ensure all special characters are properly escaped

## Examples 💡

### Example 1: Quick Resume Customization

```bash
python main.py customize \
  my_resume.pdf \
  "Senior Python Developer role requiring Django and AWS experience" \
  customized_resume.pdf
```

### Example 2: With Custom Instructions

```bash
python main.py customize \
  resume.docx \
  job_posting.txt \
  output.pdf \
  --instructions "Focus on backend development and database optimization"
```

### Example 3: Generate Word Document

```bash
python main.py customize \
  resume.txt \
  job.txt \
  output.docx \
  --format docx
```

## Contributing 🤝

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License 📝

This project is open source and available under the MIT License.

## Acknowledgments 🙏

- Google Gemini API for AI-powered content generation
- LaTeX community for the resume template design
- PyPDF2, python-docx, and pypandoc for file format handling

## Support 💬

For issues, questions, or suggestions:

- Open an issue on GitHub
- Check existing issues for solutions
- Review the documentation

---

**Made with ❤️ for job seekers everywhere**

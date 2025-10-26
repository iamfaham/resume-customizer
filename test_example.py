"""
Example script demonstrating how to use the Resume Customizer programmatically.
"""

import os
from src.app import ResumeCustomizer, customize_resume_simple


def example_basic_usage():
    """Basic example of customizing a resume."""
    print("=" * 60)
    print("EXAMPLE 1: Basic Usage")
    print("=" * 60)

    # Initialize customizer (will read GEMINI_API_KEY from environment)
    customizer = ResumeCustomizer()

    # Check if API key is set
    try:
        if not customizer.gemini_client.api_key:
            print("⚠️  Please set GEMINI_API_KEY environment variable")
            return
    except:
        print("⚠️  Please set GEMINI_API_KEY environment variable")
        return

    # Example resume text (in practice, this would be read from a file)
    sample_resume = """
John Doe
john.doe@email.com | (555) 123-4567 | linkedin.com/in/johndoe | github.com/johndoe

SUMMARY
Software Engineer with 5 years of experience in full-stack development, specializing in Python and JavaScript.

EDUCATION
Bachelor of Science in Computer Science
University of Technology | San Francisco, CA | May 2018

EXPERIENCE
Senior Software Engineer | Tech Corp | San Francisco, CA | Jan 2020 - Present
- Developed and maintained web applications using React and Node.js
- Implemented RESTful APIs serving 1M+ requests per day
- Led team of 3 junior developers

Software Engineer | StartUp Inc | San Francisco, CA | Jun 2018 - Dec 2019
- Built scalable backend services using Python and Django
- Optimized database queries, reducing response time by 40%

PROJECTS
E-commerce Platform | Python, Django, PostgreSQL | 2022
- Built full-stack e-commerce application with payment integration
- Implemented user authentication and authorization

TECHNICAL SKILLS
Languages: Python, JavaScript, Java, SQL
Frameworks: React, Node.js, Django, Flask
Tools: Git, Docker, AWS, PostgreSQL
"""

    job_description = """
We are seeking a Senior Python Developer to join our backend team.

Requirements:
- 5+ years of Python development experience
- Strong knowledge of Django and Flask frameworks
- Experience with REST API design
- Proficiency in SQL and database optimization
- Experience with AWS cloud services
- Strong leadership and mentoring skills

Responsibilities:
- Design and implement scalable backend services
- Optimize application performance
- Mentor junior developers
- Collaborate with frontend team
"""

    # Create sample files for testing
    with open("sample_resume.txt", "w") as f:
        f.write(sample_resume)

    with open("sample_job.txt", "w") as f:
        f.write(job_description)

    print("\n📝 Sample files created: sample_resume.txt, sample_job.txt")
    print("\n🚀 Starting resume customization...")

    # Customize resume
    result = customizer.customize_resume(
        resume_path="sample_resume.txt",
        job_description="sample_job.txt",
        output_path="customized_resume.pdf",
        output_format="pdf",
        save_latex=True,
    )

    if result["success"]:
        print("\n✅ Resume customized successfully!")
        print(f"📄 PDF: {result['output_file']}")
        print(f"📝 LaTeX: {result['latex_file']}")
    else:
        print(f"\n❌ Error: {result['error']}")


def example_with_custom_instructions():
    """Example with custom instructions."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: With Custom Instructions")
    print("=" * 60)

    customizer = ResumeCustomizer()

    custom_instructions = """
- Emphasize leadership and team management experience
- Highlight Python and Django expertise prominently
- Use metrics and quantifiable achievements wherever possible
- Keep the summary section concise (2 sentences maximum)
- Prioritize backend development projects
"""

    result = customizer.customize_resume(
        resume_path="sample_resume.txt",
        job_description="sample_job.txt",
        output_path="customized_resume_v2.pdf",
        output_format="pdf",
        custom_instructions=custom_instructions,
        save_latex=True,
    )

    if result["success"]:
        print("\n✅ Resume with custom instructions generated!")
        print(f"📄 PDF: {result['output_file']}")


def example_simplified_api():
    """Example using the simplified API."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Simplified API")
    print("=" * 60)

    result = customize_resume_simple(
        resume_path="sample_resume.txt",
        job_description="sample_job.txt",
        output_path="customized_resume_simple.pdf",
        output_format="pdf",
    )

    if result["success"]:
        print("\n✅ Resume generated using simplified API!")
        print(f"📄 PDF: {result['output_file']}")


def example_generate_latex_only():
    """Example generating only LaTeX source."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Generate LaTeX Only")
    print("=" * 60)

    customizer = ResumeCustomizer()

    result = customizer.customize_resume(
        resume_path="sample_resume.txt",
        job_description="sample_job.txt",
        output_path="customized_resume.tex",
        output_format="tex",
    )

    if result["success"]:
        print("\n✅ LaTeX source generated!")
        print(f"📝 LaTeX: {result['output_file']}")


def example_check_requirements():
    """Example checking system requirements."""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Check System Requirements")
    print("=" * 60)

    customizer = ResumeCustomizer()
    status = customizer.check_system_requirements()

    if status["all_ready"]:
        print("\n✅ All systems ready!")
    else:
        print("\n⚠️  Some dependencies missing:")
        if not status["pdf_support"]:
            print("  - PDF generation not available (install LaTeX)")
        if not status["docx_support"]:
            print("  - Word generation not available (install Pandoc)")
        if not status["api_key"]:
            print("  - Gemini API key not set")


def main():
    """Run all examples."""
    print("\n🎯 RESUME CUSTOMIZER - USAGE EXAMPLES\n")

    # First check requirements
    example_check_requirements()

    # Check if API key is available
    if not os.getenv("GEMINI_API_KEY"):
        print("\n" + "=" * 60)
        print("⚠️  GEMINI_API_KEY not set in environment")
        print("=" * 60)
        print("\nTo run the examples, set your API key:")
        print("  export GEMINI_API_KEY='your-api-key-here'  # Linux/Mac")
        print("  set GEMINI_API_KEY=your-api-key-here       # Windows CMD")
        print("  $env:GEMINI_API_KEY='your-api-key-here'    # Windows PowerShell")
        print("\nOr create a .env file with:")
        print("  GEMINI_API_KEY=your-api-key-here")
        return

    try:
        # Run examples
        example_basic_usage()

        # Uncomment to run other examples:
        # example_with_custom_instructions()
        # example_simplified_api()
        # example_generate_latex_only()

    except Exception as e:
        print(f"\n❌ Error running examples: {str(e)}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()

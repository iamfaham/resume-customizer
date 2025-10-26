"""Main application logic for resume customization."""

from pathlib import Path
from typing import Literal, Optional, Union
from .gemini_client import GeminiResumeGenerator
from .resume_parser import ResumeParser
from .latex_converter import LaTeXConverter


class ResumeCustomizer:
    """Main application class for resume customization."""

    def __init__(
        self, api_key: Optional[str] = None, model: str = "gemini-2.0-flash-exp"
    ):
        """
        Initialize the Resume Customizer.

        Args:
            api_key: Google Gemini API key (optional, reads from GEMINI_API_KEY env var if not provided)
            model: Gemini model to use
        """
        self.gemini_client = GeminiResumeGenerator(api_key=api_key, model=model)
        self.parser = ResumeParser()
        self.converter = LaTeXConverter()

    def customize_resume(
        self,
        resume_path: Union[str, Path],
        job_description: Union[str, Path],
        output_path: Union[str, Path],
        output_format: Literal["pdf", "docx", "tex"] = "pdf",
        custom_instructions: Optional[str] = None,
        save_latex: bool = True,
        two_pass: bool = True,
    ) -> dict:
        """
        Customize a resume for a specific job description.

        Args:
            resume_path: Path to the current resume file (supports .txt, .pdf, .docx)
            job_description: Job description text or path to file
            output_path: Path for the output file
            output_format: Output format ('pdf', 'docx', or 'tex')
            custom_instructions: Additional instructions for customization
            save_latex: Whether to also save the LaTeX source code
            two_pass: Use two-pass generation (generate + validate/enhance)

        Returns:
            dict: Dictionary containing paths to generated files and status
        """
        result = {
            "success": False,
            "output_file": None,
            "latex_file": None,
            "error": None,
        }

        try:
            # Step 1: Parse resume
            print("📄 Parsing resume...")
            resume_text = self.parser.parse_resume(resume_path)

            if not self.parser.validate_resume_content(resume_text):
                raise ValueError("Resume content is too short or empty")

            print(f"✓ Resume parsed successfully ({len(resume_text)} characters)")

            # Step 2: Parse job description
            print("📋 Parsing job description...")
            job_desc_text = self.parser.parse_job_description(job_description)
            print(
                f"✓ Job description parsed successfully ({len(job_desc_text)} characters)"
            )

            # Step 3: Generate customized LaTeX
            if two_pass:
                print("🤖 Pass 1/2: Generating customized resume with Gemini API...")
            else:
                print("🤖 Generating customized resume with Gemini API...")

            if custom_instructions:
                latex_code = self.gemini_client.generate_with_custom_instructions(
                    current_resume=resume_text,
                    job_description=job_desc_text,
                    custom_instructions=custom_instructions,
                    two_pass=two_pass,
                )
            else:
                latex_code = self.gemini_client.generate_customized_resume(
                    current_resume=resume_text,
                    job_description=job_desc_text,
                    two_pass=two_pass,
                )

            if two_pass:
                print("✓ Two-pass generation completed (generated + validated)")
            else:
                print("✓ LaTeX code generated successfully")

            # Step 4: Save LaTeX if requested or if output format is 'tex'
            output_path = Path(output_path)
            if save_latex or output_format == "tex":
                latex_path = output_path.with_suffix(".tex")
                self.converter.save_latex(latex_code, latex_path)
                result["latex_file"] = str(latex_path)
                print(f"✓ LaTeX source saved to: {latex_path}")

            # Step 5: Convert to desired format
            if output_format == "tex":
                result["output_file"] = result["latex_file"]
                result["success"] = True
            else:
                print(f"📦 Converting to {output_format.upper()}...")
                output_file = self.converter.convert(
                    latex_code=latex_code,
                    output_path=str(output_path),
                    output_format=output_format,
                )
                result["output_file"] = output_file
                result["success"] = True
                print(f"✓ Resume generated successfully: {output_file}")

        except Exception as e:
            result["error"] = str(e)
            print(f"❌ Error: {str(e)}")

        return result

    def check_system_requirements(self) -> dict:
        """
        Check if all system requirements are met.

        Returns:
            dict: Status of system requirements
        """
        print("🔍 Checking system requirements...")

        dependencies = self.converter.check_dependencies()

        print("\n📋 Dependency Status:")
        print(
            f"  • pdflatex: {'✓ Installed' if dependencies['pdflatex'] else '✗ Not found'}"
        )
        print(
            f"  • pandoc:   {'✓ Installed' if dependencies['pandoc'] else '✗ Not found'}"
        )

        # Check API key
        try:
            api_key_set = bool(self.gemini_client.api_key)
        except:
            api_key_set = False

        print(f"  • Gemini API Key: {'✓ Set' if api_key_set else '✗ Not set'}")

        print("\n📝 Notes:")
        if not dependencies["pdflatex"]:
            print("  - Install LaTeX to generate PDF files (TeX Live, MiKTeX, etc.)")
        if not dependencies["pandoc"]:
            print("  - Install Pandoc to generate Word documents")
        if not api_key_set:
            print(
                "  - Set GEMINI_API_KEY environment variable or pass API key to constructor"
            )

        return {
            "pdflatex": dependencies["pdflatex"],
            "pandoc": dependencies["pandoc"],
            "api_key": api_key_set,
            "pdf_support": dependencies["pdflatex"],
            "docx_support": dependencies["pandoc"],
            "all_ready": all(
                [dependencies["pdflatex"], dependencies["pandoc"], api_key_set]
            ),
        }


def customize_resume_simple(
    resume_path: str,
    job_description: str,
    output_path: str,
    output_format: Literal["pdf", "docx", "tex"] = "pdf",
    api_key: Optional[str] = None,
    two_pass: bool = True,
) -> dict:
    """
    Simplified function to customize a resume.

    Args:
        resume_path: Path to current resume
        job_description: Job description text or file path
        output_path: Path for output file
        output_format: Output format ('pdf', 'docx', or 'tex')
        api_key: Gemini API key (optional)
        two_pass: Use two-pass generation (default: True)

    Returns:
        dict: Result dictionary with file paths and status
    """
    customizer = ResumeCustomizer(api_key=api_key)
    return customizer.customize_resume(
        resume_path=resume_path,
        job_description=job_description,
        output_path=output_path,
        output_format=output_format,
        two_pass=two_pass,
    )

"""LaTeX to PDF/Word converter."""

import os
import subprocess
import tempfile
from pathlib import Path
from typing import Literal, Optional
import pypandoc


class LaTeXConverter:
    """Converter for LaTeX documents to PDF and Word formats."""

    def __init__(self):
        """Initialize the converter."""
        self.temp_dir = None

    def convert(
        self,
        latex_code: str,
        output_path: str,
        output_format: Literal["pdf", "docx"] = "pdf",
        cleanup: bool = True,
    ) -> str:
        """
        Convert LaTeX code to PDF or Word document.

        Args:
            latex_code: LaTeX source code
            output_path: Path for the output file
            output_format: Output format ('pdf' or 'docx')
            cleanup: Whether to cleanup temporary files

        Returns:
            str: Path to the generated file

        Raises:
            Exception: If conversion fails
        """
        output_path = Path(output_path)

        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if output_format == "pdf":
            return self._latex_to_pdf(latex_code, output_path, cleanup)
        elif output_format == "docx":
            return self._latex_to_docx(latex_code, output_path, cleanup)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")

    def _latex_to_pdf(
        self, latex_code: str, output_path: Path, cleanup: bool = True
    ) -> str:
        """
        Convert LaTeX to PDF using pdflatex.

        Args:
            latex_code: LaTeX source code
            output_path: Path for output PDF
            cleanup: Whether to cleanup temporary files

        Returns:
            str: Path to generated PDF
        """
        # Create temporary directory for compilation
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            tex_file = temp_path / "resume.tex"

            # Write LaTeX code to file
            with open(tex_file, "w", encoding="utf-8") as f:
                f.write(latex_code)

            try:
                # Run pdflatex twice (for references and TOC if any)
                for _ in range(2):
                    result = subprocess.run(
                        [
                            "pdflatex",
                            "-interaction=nonstopmode",
                            "-output-directory",
                            str(temp_path),
                            str(tex_file),
                        ],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )

                    # Check if compilation was successful
                    pdf_file = temp_path / "resume.pdf"
                    if not pdf_file.exists():
                        # Try to extract error from log
                        log_file = temp_path / "resume.log"
                        error_msg = "PDF compilation failed"
                        if log_file.exists():
                            with open(
                                log_file, "r", encoding="utf-8", errors="ignore"
                            ) as f:
                                log_content = f.read()
                                # Extract error lines
                                error_lines = [
                                    line
                                    for line in log_content.split("\n")
                                    if "!" in line
                                ]
                                if error_lines:
                                    error_msg = f"LaTeX Error: {error_lines[0]}"
                        raise Exception(error_msg)

                # Copy PDF to output location
                import shutil

                shutil.copy(pdf_file, output_path)

                return str(output_path)

            except subprocess.TimeoutExpired:
                raise Exception("PDF compilation timed out after 30 seconds")
            except FileNotFoundError:
                raise Exception(
                    "pdflatex not found. Please install LaTeX (e.g., TeX Live, MiKTeX) "
                    "to enable PDF generation."
                )
            except Exception as e:
                raise Exception(f"Error converting LaTeX to PDF: {str(e)}")

    def _latex_to_docx(
        self, latex_code: str, output_path: Path, cleanup: bool = True
    ) -> str:
        """
        Convert LaTeX to Word document using pandoc.

        Args:
            latex_code: LaTeX source code
            output_path: Path for output DOCX
            cleanup: Whether to cleanup temporary files

        Returns:
            str: Path to generated DOCX
        """
        try:
            # Create temporary LaTeX file
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".tex", delete=False, encoding="utf-8"
            ) as temp_file:
                temp_file.write(latex_code)
                temp_tex_path = temp_file.name

            try:
                # Convert using pandoc
                pypandoc.convert_file(
                    temp_tex_path,
                    "docx",
                    outputfile=str(output_path),
                    extra_args=["--standalone"],
                )

                return str(output_path)

            finally:
                # Cleanup temp file
                if cleanup and os.path.exists(temp_tex_path):
                    os.unlink(temp_tex_path)

        except RuntimeError as e:
            if "pandoc" in str(e).lower():
                raise Exception(
                    "Pandoc not found. Please install Pandoc to enable Word document generation. "
                    "Visit: https://pandoc.org/installing.html"
                )
            raise Exception(f"Error converting LaTeX to DOCX: {str(e)}")
        except Exception as e:
            raise Exception(f"Error converting LaTeX to DOCX: {str(e)}")

    def save_latex(self, latex_code: str, output_path: str) -> str:
        """
        Save LaTeX code to a .tex file.

        Args:
            latex_code: LaTeX source code
            output_path: Path for output .tex file

        Returns:
            str: Path to saved file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(latex_code)

        return str(output_path)

    @staticmethod
    def check_dependencies() -> dict:
        """
        Check if required dependencies are installed.

        Returns:
            dict: Dictionary with dependency status
        """
        dependencies = {"pdflatex": False, "pandoc": False}

        # Check pdflatex
        try:
            result = subprocess.run(
                ["pdflatex", "--version"], capture_output=True, timeout=5
            )
            dependencies["pdflatex"] = result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        # Check pandoc
        try:
            pypandoc.get_pandoc_version()
            dependencies["pandoc"] = True
        except Exception:
            pass

        return dependencies

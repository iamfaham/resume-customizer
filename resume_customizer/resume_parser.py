"""Resume parser for different file formats."""

import os
from pathlib import Path
from typing import Union
import docx
from PyPDF2 import PdfReader


class ResumeParser:
    """Parser for extracting text content from resume files."""

    SUPPORTED_FORMATS = [".txt", ".pdf", ".docx", ".doc"]

    @staticmethod
    def parse_resume(file_path: Union[str, Path]) -> str:
        """
        Parse a resume file and extract text content.

        Args:
            file_path: Path to the resume file

        Returns:
            str: Extracted text content from the resume

        Raises:
            ValueError: If file format is not supported
            FileNotFoundError: If file doesn't exist
        """
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"Resume file not found: {file_path}")

        file_ext = file_path.suffix.lower()

        if file_ext not in ResumeParser.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported file format: {file_ext}. "
                f"Supported formats: {', '.join(ResumeParser.SUPPORTED_FORMATS)}"
            )

        if file_ext == ".txt":
            return ResumeParser._parse_txt(file_path)
        elif file_ext == ".pdf":
            return ResumeParser._parse_pdf(file_path)
        elif file_ext in [".docx", ".doc"]:
            return ResumeParser._parse_docx(file_path)
        else:
            raise ValueError(f"Unsupported format: {file_ext}")

    @staticmethod
    def _parse_txt(file_path: Path) -> str:
        """Parse a text file."""
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def _parse_pdf(file_path: Path) -> str:
        """Parse a PDF file."""
        try:
            reader = PdfReader(file_path)
            text = []
            for page in reader.pages:
                text.append(page.extract_text())
            return "\n".join(text)
        except Exception as e:
            raise Exception(f"Error parsing PDF file: {str(e)}")

    @staticmethod
    def _parse_docx(file_path: Path) -> str:
        """Parse a DOCX file."""
        try:
            doc = docx.Document(file_path)
            text = []
            for paragraph in doc.paragraphs:
                text.append(paragraph.text)
            return "\n".join(text)
        except Exception as e:
            raise Exception(f"Error parsing DOCX file: {str(e)}")

    @staticmethod
    def parse_job_description(job_desc: Union[str, Path]) -> str:
        """
        Parse job description from string or file.

        Args:
            job_desc: Job description as string or path to file

        Returns:
            str: Job description text
        """
        # If it's a string and doesn't exist as a file, treat it as direct text
        if isinstance(job_desc, str) and not Path(job_desc).exists():
            return job_desc

        # Otherwise, parse as a file
        return ResumeParser.parse_resume(job_desc)

    @staticmethod
    def validate_resume_content(resume_text: str) -> bool:
        """
        Validate that resume content is not empty and has minimum content.

        Args:
            resume_text: Resume text content

        Returns:
            bool: True if valid, False otherwise
        """
        if not resume_text or not resume_text.strip():
            return False

        # Check minimum length (at least 100 characters)
        if len(resume_text.strip()) < 100:
            return False

        return True

"""Google Gemini API integration for resume generation."""

import os
from typing import Optional
from google import genai
from dotenv import load_dotenv
from .latex_template import RESUME_LATEX_TEMPLATE, get_template_instructions

# Load environment variables from .env file
load_dotenv()


class GeminiResumeGenerator:
    """Client for generating customized resumes using Google Gemini API."""

    def __init__(
        self, api_key: Optional[str] = None, model: str = "gemini-2.5-flash-lite"
    ):
        """
        Initialize the Gemini client.

        Args:
            api_key: Google Gemini API key. If None, reads from GEMINI_API_KEY env variable.
            model: Model name to use (default: gemini-2.5-flash-lite)
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key must be provided either as argument or via GEMINI_API_KEY environment variable"
            )

        self.model = model
        self.client = genai.Client(api_key=self.api_key)

    def generate_customized_resume(
        self,
        current_resume: str,
        job_description: str,
        template: Optional[str] = None,
        two_pass: bool = True,
    ) -> str:
        """
        Generate a customized resume based on the current resume and job description.

        Args:
            current_resume: The user's current resume content (text format)
            job_description: The target job description
            template: LaTeX template to use (defaults to built-in template)
            two_pass: If True, uses two-pass generation (generate + validate/enhance)

        Returns:
            str: Generated LaTeX code for the customized resume
        """
        if template is None:
            template = RESUME_LATEX_TEMPLATE

        # First pass: Generate initial resume
        prompt = self._construct_prompt(current_resume, job_description, template)

        try:
            response = self.client.models.generate_content(
                model=self.model, contents=prompt
            )

            latex_code = response.text
            latex_code = self._clean_latex_response(latex_code)

            # Second pass: Validate and enhance if requested
            if two_pass:
                print("   🔍 Pass 2/2: Validating and enhancing LaTeX code...")
                latex_code = self._validate_and_enhance_latex(latex_code, template)

            return latex_code

        except Exception as e:
            raise Exception(f"Error generating resume with Gemini API: {str(e)}")

    def _construct_prompt(
        self, current_resume: str, job_description: str, template: str
    ) -> str:
        """Construct the prompt for the LLM."""
        instructions = get_template_instructions()

        prompt = f"""{instructions}

---

CURRENT RESUME:
{current_resume}

---

JOB DESCRIPTION:
{job_description}

---

LATEX TEMPLATE TO USE:
{template}

---

Now generate the complete LaTeX code for the customized resume. Output ONLY the LaTeX code, nothing else.
"""
        return prompt

    def _clean_latex_response(self, response: str) -> str:
        """
        Clean the LLM response to extract pure LaTeX code.

        Removes markdown code blocks and any surrounding text.
        """
        # Remove markdown code block syntax if present
        if "```latex" in response:
            # Extract content between ```latex and ```
            start = response.find("```latex") + 8
            end = response.find("```", start)
            if end != -1:
                response = response[start:end]
        elif "```" in response:
            # Extract content between ``` and ```
            start = response.find("```") + 3
            end = response.find("```", start)
            if end != -1:
                response = response[start:end]

        # Strip whitespace
        response = response.strip()

        return response

    def _validate_and_enhance_latex(self, latex_code: str, template: str) -> str:
        """
        Second pass: Validate and enhance the generated LaTeX code.

        Args:
            latex_code: Generated LaTeX code from first pass
            template: Original template for reference

        Returns:
            str: Enhanced and validated LaTeX code
        """
        validation_prompt = self._construct_validation_prompt(latex_code, template)

        try:
            response = self.client.models.generate_content(
                model=self.model, contents=validation_prompt
            )

            enhanced_latex = response.text
            enhanced_latex = self._clean_latex_response(enhanced_latex)

            return enhanced_latex

        except Exception as e:
            # If validation fails, return original code
            print(f"⚠️  Validation pass failed, using original output: {str(e)}")
            return latex_code

    def _construct_validation_prompt(self, latex_code: str, template: str) -> str:
        """Construct the validation prompt for the second LLM pass."""
        prompt = f"""You are a LaTeX expert and resume quality reviewer. Your task is to review and enhance the generated LaTeX resume code.

ORIGINAL TEMPLATE FOR REFERENCE:
{template}

---

GENERATED LATEX CODE TO REVIEW:
{latex_code}

---

YOUR TASK:
Review the generated LaTeX code and fix any issues. Then output the CORRECTED and ENHANCED version.

CHECK FOR THESE ISSUES:

1. **LaTeX SYNTAX ERRORS:**
   - Missing or mismatched braces {{}}
   - Incorrect command usage (\\resumeSubheading, \\resumeItem, etc.)
   - Special characters that need escaping (%, &, $, #, _, {{, }})
   - Malformed URLs or email addresses
   - Missing required arguments in commands

2. **TEMPLATE COMPLIANCE:**
   - Ensure ALL commands match the template exactly
   - No extra packages or modifications to template structure
   - Correct usage of \\resumeSubheading, \\resumeProjectHeading, etc.
   - Proper nesting of \\resumeItemListStart and \\resumeItemListEnd

3. **ONE-PAGE CONSTRAINT:**
   - If content seems too long, condense bullet points
   - Remove less impactful items
   - Ensure it will fit on ONE PAGE when compiled

4. **FORMATTING ISSUES:**
   - Consistent spacing and indentation
   - Proper date formats
   - Correct use of emphasis (\\textbf, \\emph)
   - No orphaned or incomplete sections

5. **CONTENT QUALITY:**
   - Bullet points are concise (1-2 lines max)
   - Action verbs used effectively
   - Metrics included where present
   - No placeholder text like "ABC Company" or "Your Name"
   - Professional language throughout

6. **SPECIAL CHARACTER ESCAPING:**
   - Escape: % \# $ & _ {{ }}
   - Use \\& for ampersands
   - Use \\% for percentages
   - Use \\$ for dollar signs
   - Use \\# for hashtags

CRITICAL RULES:
✅ Fix all LaTeX syntax errors
✅ Ensure template structure is followed exactly
✅ Maintain one-page length
✅ Improve clarity and impact
✅ Return ONLY the complete, corrected LaTeX code
❌ Do NOT add explanations or comments
❌ Do NOT modify the template structure itself
❌ Do NOT add new packages

Output the COMPLETE corrected LaTeX document, ready to compile without errors.
"""
        return prompt

    def generate_with_custom_instructions(
        self,
        current_resume: str,
        job_description: str,
        custom_instructions: str,
        template: Optional[str] = None,
        two_pass: bool = True,
    ) -> str:
        """
        Generate a customized resume with custom instructions.

        Args:
            current_resume: The user's current resume content
            job_description: The target job description
            custom_instructions: Additional custom instructions for the LLM
            template: LaTeX template to use
            two_pass: If True, uses two-pass generation (generate + validate/enhance)

        Returns:
            str: Generated LaTeX code
        """
        if template is None:
            template = RESUME_LATEX_TEMPLATE

        base_instructions = get_template_instructions()
        full_instructions = (
            f"{base_instructions}\n\nADDITIONAL INSTRUCTIONS:\n{custom_instructions}"
        )

        prompt = f"""{full_instructions}

---

CURRENT RESUME:
{current_resume}

---

JOB DESCRIPTION:
{job_description}

---

LATEX TEMPLATE TO USE:
{template}

---

Now generate the complete LaTeX code for the customized resume. Output ONLY the LaTeX code, nothing else.
"""

        try:
            response = self.client.models.generate_content(
                model=self.model, contents=prompt
            )

            latex_code = response.text
            latex_code = self._clean_latex_response(latex_code)

            # Second pass: Validate and enhance if requested
            if two_pass:
                print("   🔍 Pass 2/2: Validating and enhancing LaTeX code...")
                latex_code = self._validate_and_enhance_latex(latex_code, template)

            return latex_code

        except Exception as e:
            raise Exception(f"Error generating resume with Gemini API: {str(e)}")

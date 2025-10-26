"""
Resume Customizer - Main entry point

This script provides a command-line interface to customize resumes using Google Gemini API.
"""

import sys
import argparse
from pathlib import Path
from src.app import ResumeCustomizer


def main():
    parser = argparse.ArgumentParser(
        description="Customize your resume for specific job descriptions using AI"
    )

    # Add subcommands
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Customize command
    customize_parser = subparsers.add_parser("customize", help="Customize a resume")
    customize_parser.add_argument(
        "resume", help="Path to your current resume (txt, pdf, or docx)"
    )
    customize_parser.add_argument(
        "job_description", help="Job description text or path to file"
    )
    customize_parser.add_argument("output", help="Output file path")
    customize_parser.add_argument(
        "--format",
        "-f",
        choices=["pdf", "docx", "tex"],
        default="pdf",
        help="Output format (default: pdf)",
    )
    customize_parser.add_argument(
        "--api-key",
        "-k",
        help="Google Gemini API key (or set GEMINI_API_KEY env variable)",
    )
    customize_parser.add_argument(
        "--model",
        "-m",
        default="gemini-2.0-flash-exp",
        help="Gemini model to use (default: gemini-2.0-flash-exp)",
    )
    customize_parser.add_argument(
        "--instructions", "-i", help="Additional custom instructions for the AI"
    )
    customize_parser.add_argument(
        "--no-save-latex", action="store_true", help="Do not save the LaTeX source code"
    )
    customize_parser.add_argument(
        "--single-pass",
        action="store_true",
        help="Use single-pass generation (faster but less validation)",
    )

    # Check command
    check_parser = subparsers.add_parser("check", help="Check system requirements")
    check_parser.add_argument("--api-key", "-k", help="Google Gemini API key to verify")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "customize":
        # Create customizer instance
        customizer = ResumeCustomizer(
            api_key=args.api_key if hasattr(args, "api_key") else None,
            model=args.model if hasattr(args, "model") else "gemini-2.0-flash-exp",
        )

        # Customize resume
        result = customizer.customize_resume(
            resume_path=args.resume,
            job_description=args.job_description,
            output_path=args.output,
            output_format=args.format,
            custom_instructions=(
                args.instructions if hasattr(args, "instructions") else None
            ),
            save_latex=(
                not args.no_save_latex if hasattr(args, "no_save_latex") else True
            ),
            two_pass=not args.single_pass if hasattr(args, "single_pass") else True,
        )

        if result["success"]:
            print("\n✅ Success!")
            print(f"📄 Output file: {result['output_file']}")
            if result["latex_file"]:
                print(f"📝 LaTeX source: {result['latex_file']}")
        else:
            print(f"\n❌ Failed: {result['error']}")
            sys.exit(1)

    elif args.command == "check":
        # Check system requirements
        customizer = ResumeCustomizer(
            api_key=args.api_key if hasattr(args, "api_key") else None
        )
        status = customizer.check_system_requirements()

        if status["all_ready"]:
            print("\n✅ All requirements met! You're ready to go.")
        else:
            print("\n⚠️  Some requirements are missing. See notes above.")
            sys.exit(1)


if __name__ == "__main__":
    main()

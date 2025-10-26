"""LaTeX template for resume generation."""

RESUME_LATEX_TEMPLATE = r"""
%-------------------------
% Resume in Latex
% Author : Jake Gutierrez
% Based off of: https://github.com/sb2nov/resume
% License : MIT
%------------------------

\documentclass[letterpaper,11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\input{glyphtounicode}


%----------FONT OPTIONS----------
% sans-serif
% \usepackage[sfdefault]{FiraSans}
% \usepackage[sfdefault]{roboto}
% \usepackage[sfdefault]{noto-sans}
% \usepackage[default]{sourcesanspro}

% serif
% \usepackage{CormorantGaramond}
% \usepackage{charter}


\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & #2 \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%


\begin{document}

%----------HEADING----------
% \begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
%   \textbf{\href{http://sourabhbajaj.com/}{\Large Sourabh Bajaj}} & Email : \href{mailto:sourabh@sourabhbajaj.com}{sourabh@sourabhbajaj.com}\\
%   \href{http://sourabhbajaj.com/}{http://www.sourabhbajaj.com} & Mobile : +1-123-456-7890 \\
% \end{tabular*}

\begin{center}
    \textbf{\Huge \scshape Jake Ryan} \\ \vspace{1pt}
    \small 123-456-7890 $|$ \href{mailto:x@x.com}{\underline{jake@su.edu}} $|$ 
    \href{https://linkedin.com/in/...}{\underline{linkedin.com/in/jake}} $|$
    \href{https://github.com/...}{\underline{github.com/jake}}
\end{center}


%-----------EDUCATION-----------
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {Southwestern University}{Georgetown, TX}
      {Bachelor of Arts in Computer Science, Minor in Business}{Aug. 2018 -- May 2021}
    \resumeSubheading
      {Blinn College}{Bryan, TX}
      {Associate's in Liberal Arts}{Aug. 2014 -- May 2018}
  \resumeSubHeadingListEnd


%-----------EXPERIENCE-----------
\section{Experience}
  \resumeSubHeadingListStart

    \resumeSubheading
      {Undergraduate Research Assistant}{June 2020 -- Present}
      {Texas A\&M University}{College Station, TX}
      \resumeItemListStart
        \resumeItem{Developed a REST API using FastAPI and PostgreSQL to store data from learning management systems}
        \resumeItem{Developed a full-stack web application using Flask, React, PostgreSQL and Docker to analyze GitHub data}
        \resumeItem{Explored ways to visualize GitHub collaboration in a classroom setting}
      \resumeItemListEnd
      
% -----------Multiple Positions Heading-----------
%    \resumeSubSubheading
%     {Software Engineer I}{Oct 2014 - Sep 2016}
%     \resumeItemListStart
%        \resumeItem{Apache Beam}
%          {Apache Beam is a unified model for defining both batch and streaming data-parallel processing pipelines}
%     \resumeItemListEnd
%    \resumeSubHeadingListEnd
%-------------------------------------------

    \resumeSubheading
      {Information Technology Support Specialist}{Sep. 2018 -- Present}
      {Southwestern University}{Georgetown, TX}
      \resumeItemListStart
        \resumeItem{Communicate with managers to set up campus computers used on campus}
        \resumeItem{Assess and troubleshoot computer problems brought by students, faculty and staff}
        \resumeItem{Maintain upkeep of computers, classroom equipment, and 200 printers across campus}
    \resumeItemListEnd

    \resumeSubheading
      {Artificial Intelligence Research Assistant}{May 2019 -- July 2019}
      {Southwestern University}{Georgetown, TX}
      \resumeItemListStart
        \resumeItem{Explored methods to generate video game dungeons based off of \emph{The Legend of Zelda}}
        \resumeItem{Developed a game in Java to test the generated dungeons}
        \resumeItem{Contributed 50K+ lines of code to an established codebase via Git}
        \resumeItem{Conducted  a human subject study to determine which video game dungeon generation technique is enjoyable}
        \resumeItem{Wrote an 8-page paper and gave multiple presentations on-campus}
        \resumeItem{Presented virtually to the World Conference on Computational Intelligence}
      \resumeItemListEnd

  \resumeSubHeadingListEnd


%-----------PROJECTS-----------
\section{Projects}
    \resumeSubHeadingListStart
      \resumeProjectHeading
          {\textbf{Gitlytics} $|$ \emph{Python, Flask, React, PostgreSQL, Docker}}{}
          \resumeItemListStart
            \resumeItem{Developed a full-stack web application using with Flask serving a REST API with React as the frontend}
            \resumeItem{Implemented GitHub OAuth to get data from user’s repositories}
            \resumeItem{Visualized GitHub data to show collaboration}
            \resumeItem{Used Celery and Redis for asynchronous tasks}
          \resumeItemListEnd
      \resumeProjectHeading
          {\textbf{Simple Paintball} $|$ \emph{Spigot API, Java, Maven, TravisCI, Git}}{}
          \resumeItemListStart
            \resumeItem{Developed a Minecraft server plugin to entertain kids during free time for a previous job}
            \resumeItem{Published plugin to websites gaining 2K+ downloads and an average 4.5/5-star review}
            \resumeItem{Implemented continuous delivery using TravisCI to build the plugin upon new a release}
            \resumeItem{Collaborated with Minecraft server administrators to suggest features and get feedback about the plugin}
          \resumeItemListEnd
    \resumeSubHeadingListEnd



%
%-----------PROGRAMMING SKILLS-----------
\section{Technical Skills}
 \begin{itemize}[leftmargin=0.15in, label={}]
    \small{\item{
     \textbf{Languages}{: Java, Python, C/C++, SQL (Postgres), JavaScript, HTML/CSS, R} \\
     \textbf{Frameworks}{: React, Node.js, Flask, JUnit, WordPress, Material-UI, FastAPI} \\
     \textbf{Developer Tools}{: Git, Docker, TravisCI, Google Cloud Platform, VS Code, Visual Studio, PyCharm, IntelliJ, Eclipse} \\
     \textbf{Libraries}{: pandas, NumPy, Matplotlib}
    }}
 \end{itemize}


%-------------------------------------------
\end{document}
"""


def get_template_instructions():
    """Get instructions for the LLM on how to fill the template."""
    return """
You are a professional resume writer. You will receive:
1. A user's current resume content
2. A job description they're applying for
3. A LaTeX resume template

Your task is to generate a customized LaTeX resume that:
- Uses ONLY information from the user's resume (do not fabricate or add information)
- PRESERVES MAXIMUM content from the original resume while tailoring to the job description
- Maintains professional language and formatting
- Follows the provided LaTeX template structure EXACTLY - DO NOT modify the template structure, commands, or formatting
- MUST fit on ONE PAGE ONLY - this is CRITICAL and NON-NEGOTIABLE

⚠️ CRITICAL CONSTRAINTS:

1. CONTENT PRESERVATION PRIORITY:
   - Include ALL experiences from the original resume if possible
   - Keep ALL education entries
   - Preserve ALL key projects mentioned
   - Maintain ALL technical skills listed
   - Only condense/remove if absolutely necessary for one-page constraint

2. JOB DESCRIPTION ALIGNMENT (WITHOUT REMOVING CONTENT):
   - REORDER experiences to put most relevant first
   - REWRITE bullet points to emphasize skills matching the JD
   - HIGHLIGHT keywords from JD in the summary
   - PRIORITIZE metrics and achievements relevant to the target role
   - ADD emphasis (using existing LaTeX commands) to JD-relevant skills

3. ONE PAGE MAXIMUM - If content won't fit, use this priority for condensing:
   a) Shorten bullet points (keep ALL experiences, just more concise)
   b) Combine similar experiences if they're from same company/timeframe
   c) Remove only the LEAST relevant project (if you must)
   d) As last resort, remove oldest/least relevant experience
   - DO NOT remove education, contact info, or technical skills section
   
2. STRICT TEMPLATE ADHERENCE:
   - DO NOT add any extra LaTeX packages
   - DO NOT modify spacing, margins, or formatting commands
   - DO NOT add new sections beyond what's in the template
   - USE ONLY the custom commands provided (\\resumeItem, \\resumeSubheading, etc.)
   - Keep the EXACT structure of the template

IMPORTANT INSTRUCTIONS:
1. Replace ALL placeholder content with actual information:
   - Name, phone, email, LinkedIn, GitHub in the header
   - Keep contact info on ONE LINE in the header

2. For EDUCATION (typically 1-2 entries max):
   \\resumeSubheading{University Name}{Location}{Degree and Major}{Graduation Date}

3. For EXPERIENCE (2-4 entries, 2-3 bullets each):
   \\resumeSubheading{Company Name}{Date Range}{Job Title}{Location}
   \\resumeItemListStart
     \\resumeItem{Achievement or responsibility with METRICS when possible}
     \\resumeItem{Another impactful bullet point}
     \\resumeItem{Third bullet if space permits}
   \\resumeItemListEnd

4. For PROJECTS (1-3 entries, 1-2 bullets each):
   \\resumeProjectHeading{\\textbf{Project Name} $|$ \\emph{Technologies Used}}{Date}
   \\resumeItemListStart
     \\resumeItem{Concise project description with impact}
   \\resumeItemListEnd

5. For TECHNICAL SKILLS (concise categories):
   \\textbf{Languages}{: Python, JavaScript, Java, C++} \\\\
   \\textbf{Frameworks}{: React, Node.js, Django, Flask} \\\\
   \\textbf{Developer Tools}{: Git, Docker, AWS, VS Code} \\\\
   \\textbf{Libraries}{: pandas, NumPy, Matplotlib}

CONTENT OPTIMIZATION STRATEGY:
6. Emphasize achievements with METRICS (e.g., "Improved performance by 40%", "Reduced costs by $50K")
7. Use strong ACTION VERBS that match JD keywords (Developed, Implemented, Designed, Led, Optimized, Built, etc.)
8. Keep bullet points CONCISE but INFORMATIVE - maximum 1-2 lines each
9. REORDER sections to show JD-relevant content first
10. For each experience, rewrite bullets to emphasize JD-relevant aspects
11. Extract keywords from JD and naturally incorporate them into bullets

ONE-PAGE STRATEGY (MAXIMIZE CONTENT):
- Education: ALL entries from resume (no bullet points unless critical)
- Experience: Include ALL positions, 2-3 concise bullets each (most relevant bullets from original)
- Projects: Include ALL projects if space permits, 1-2 bullets each
- Skills: ALL skills mentioned, organized by relevance to JD
- Order: Most JD-relevant items first in each section

CONTENT PRESERVATION EXAMPLES:

BAD (Removes too much):
Experience: Only 2 most recent jobs → Removes 3 older positions

GOOD (Keeps everything, condenses):
Experience: All 5 positions included, with 2 bullets each instead of 3-4

BAD (Generic):
"Developed web applications using React"

GOOD (Tailored to JD while preserving facts):
"Developed scalable web applications using React and Node.js, aligning with [JD requirement]"

FORBIDDEN:
❌ DO NOT exceed one page under any circumstances
❌ DO NOT modify the LaTeX template structure
❌ DO NOT add extra sections or packages
❌ DO NOT fabricate information not in the original resume
❌ DO NOT completely remove experiences unless absolutely necessary
❌ DO NOT ignore or omit major portions of the original resume

MANDATORY INCLUSIONS:
✅ ALL contact information from original resume
✅ ALL education entries
✅ ALL work experiences (condensed if needed)
✅ ALL technical skills mentioned
✅ ALL significant projects (minimum top 3)

APPROACH:
Think: "How can I fit ALL of the user's experience into one page while making it highly relevant to this JD?"
NOT: "What can I remove to fit the page limit?"

Output ONLY the complete LaTeX code ready to be compiled. Follow the template EXACTLY.
"""

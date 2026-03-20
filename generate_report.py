import subprocess
import os

REPORT_DIR = os.path.dirname(os.path.abspath(__file__))
TEX_FILE = os.path.join(REPORT_DIR, "Cooper_Morgan_Lab2.tex")
PDF_FILE = os.path.join(REPORT_DIR, "Cooper_Morgan_Lab2.pdf")

# --- IMAGE PATHS (update these to point to your saved plot files) ---
FIGURE_1 = "PLACEHOLDER_figure1.png"  # e.g., deterministic value/policy heatmap
FIGURE_2 = "PLACEHOLDER_figure2.png"  # e.g., stochastic value/policy heatmap
FIGURE_3 = "PLACEHOLDER_figure3.png"  # e.g., convergence comparison plot
FIGURE_4 = "PLACEHOLDER_figure4.png"  # e.g., FrozenLake results

tex_content = r"""
\documentclass[12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{amsmath}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{parskip}
\usepackage{float}

\titleformat{\section}{\large\bfseries}{}{0em}{}
\titleformat{\subsection}{\normalsize\bfseries}{}{0em}{}

\title{Lab 2: Dynamic Programming}
\author{Morgan Cooper \\ MSDS 684 --- Reinforcement Learning}
\date{\today}

\begin{document}
\maketitle

\section{Section 1: Project Overview}

% PLACEHOLDER: 400-500 words
% - Problem/Question: What RL problem are you investigating?
% - Core Concepts: What RL concepts from Sutton & Barto Ch. 4 are you exploring?
% - Theoretical Grounding: How does this connect to theory from the readings?
% - Environment Description:
%     - State space (discrete/continuous, dimensions)
%     - Action space (discrete/continuous, number of actions)
%     - Reward structure
%     - Episode termination conditions
% - Expected Behavior: What do you hypothesize will happen and why?

PLACEHOLDER: Write your project overview here.


\section{Section 2: Deliverables}

\subsection{GitHub Repository}
\begin{verbatim}
GitHub Repository: PLACEHOLDER_GITHUB_URL
\end{verbatim}

\subsection{Implementation Summary}

% PLACEHOLDER: 100-150 words
% - What you implemented (algorithms, environments)
% - Experimental setup (grid size, gamma, theta, deterministic vs stochastic)
% - Key hyperparameters chosen
% - NOT detailed pseudocode or line-by-line methods

PLACEHOLDER: Write your implementation summary here.


\subsection{Key Results \& Analysis}

% PLACEHOLDER: 400-600 words + 2-4 visualizations
% - NO raw code listings
% - NO console output dumps
% - Discussion must address:
%     - What do results show about algorithm behavior?
%     - How do they relate to theory from Sutton & Barto? (cite chapters/sections)
%     - What didn't work as expected? Why?
%     - How did hyperparameters affect performance?
%     - What does this teach you about the RL concept?

PLACEHOLDER: Write your key results and analysis here.

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{""" + FIGURE_1 + r"""}
\caption{PLACEHOLDER: Write an interpretive caption for Figure 1.}
\label{fig:figure1}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{""" + FIGURE_2 + r"""}
\caption{PLACEHOLDER: Write an interpretive caption for Figure 2.}
\label{fig:figure2}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{""" + FIGURE_3 + r"""}
\caption{PLACEHOLDER: Write an interpretive caption for Figure 3.}
\label{fig:figure3}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{""" + FIGURE_4 + r"""}
\caption{PLACEHOLDER: Write an interpretive caption for Figure 4.}
\label{fig:figure4}
\end{figure}


\section{Section 3: AI Use Reflection}

% PLACEHOLDER: 250-350 words total

\subsection{Initial Interaction}

% PLACEHOLDER: 50-75 words
% - What did you ask the AI to help you with?
% - What was the first approach suggested?

PLACEHOLDER: Write your initial interaction here.

\subsection{Iteration Cycle}

% PLACEHOLDER: 100-150 words
% - Document 2-3 specific debugging/iteration cycles
% - What broke? What did you change? Why?

\textbf{Iteration 1:}

PLACEHOLDER: Describe iteration 1 here.

\textbf{Iteration 2:}

PLACEHOLDER: Describe iteration 2 here.

\textbf{Iteration 3:}

PLACEHOLDER: Describe iteration 3 here.

\subsection{Critical Evaluation}

% PLACEHOLDER: 50-75 words
% - Where was the AI wrong or incomplete?
% - How did you verify results?

PLACEHOLDER: Write your critical evaluation here.

\subsection{Learning Reflection}

% PLACEHOLDER: 50-75 words
% - What did you learn through the process?
% - What would you do differently next time?

PLACEHOLDER: Write your learning reflection here.


\section{Section 4: Speaker Notes}

% PLACEHOLDER: 5-7 bullet points for a 3-5 minute presentation

\begin{itemize}
  \item \textbf{Problem:} PLACEHOLDER
  \item \textbf{Method:} PLACEHOLDER
  \item \textbf{Design choice:} PLACEHOLDER
  \item \textbf{Key result:} PLACEHOLDER
  \item \textbf{Insight:} PLACEHOLDER
  \item \textbf{Challenge:} PLACEHOLDER
  \item \textbf{Connection:} PLACEHOLDER
\end{itemize}

\section{References}

\begin{enumerate}
  \item Sutton, R. S., \& Barto, A. G. (2018). \textit{Reinforcement learning: An introduction} (2nd ed.). MIT Press.
  \item Anthropic. (2025). Claude Code [Large language model CLI tool]. \texttt{https://claude.ai}
  \item PLACEHOLDER: Add any additional references used.
\end{enumerate}

\end{document}
"""

def main():
    # Write temporary .tex file
    with open(TEX_FILE, "w") as f:
        f.write(tex_content)

    # Compile to PDF (run twice to resolve cross-references)
    for pass_num in (1, 2):
        print(f"Compiling to PDF (pass {pass_num})...")
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", TEX_FILE],
            cwd=REPORT_DIR,
            capture_output=True,
            text=True,
        )

    if result.returncode == 0:
        print(f"PDF generated: {PDF_FILE}")
    else:
        print("pdflatex encountered issues:")
        print(result.stdout[-2000:] if len(result.stdout) > 2000 else result.stdout)

    # Clean up all LaTeX artifacts (keep only the PDF)
    for ext in [".tex", ".aux", ".log", ".out"]:
        artifact = os.path.join(REPORT_DIR, f"Cooper_Morgan_Lab2{ext}")
        if os.path.exists(artifact):
            os.remove(artifact)


if __name__ == "__main__":
    main()

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

This project is focused on solving a known Markov Decision Process (MDP)
with dynamic programming (DP). DP requires complete knowledge of the environment
that the agent will be operating within. This is different than Lab 1 where
the agent had no knowledge of the environment and had to store the expected
action-reward values in a Q-Table. Since we already know the world view of
the environment via the MDP, we can focus on planning and developing an optimal
policy.

This project explores concepts from Sutton and Barto (2020) including policy
evaluation, policy improvement, policy iteration, and value iteration. A
policy is a mapping over each state to an action. It explains which actions
to take given each state. A value function provides a cumulative expected value
for each state by combining the current reward and all future rewards. Policy
evaluation involves identifying a value function for a given policy. Policy
improvement focuses on starting with a value function and improving the policy.
Policy evaluation asks "what is the value of each state under 
this policy?" and policy improvement asks "given the value of each state, can we
pick better actions?" 

Policy iteration works by running policy evaluation loops over each state and
collecting their values. During each loop
the reward continues to propagate up the chain of states until the value of
each state stops changing, and the value function converges. Then a loop is
run performing policy improvement where the policy is updated by selecting the
action with the highest value at each state. This process of evaluation and
policy improvement is run until there is no more change and the optimal policy
is found.

Value iteration is a different algorithm that runs loops over each state, collecting
the best value at each state by checking all possible actions. This repeats until the value function stabilizes,
then a final loop is run to collect the optimal policy by selecting the action with the
highest value for each state.

To work through these different DP algorithms, this project utilizes two environments:

\textbf{Custom GridWorld:}
\begin{itemize}
  \item State space: 16 discrete states (4$\times$4 grid), integer-encoded
  \item Action space: 4 discrete (up, right, down, left)
  \item Rewards: $-1$ per step, $0$ at goal --- incentivizes shortest paths
  \item Terminal condition: reaching the goal state
  \item Two configurations: deterministic (100\% intended) and stochastic (80/10/10)
  \item Obstacles that block movement
\end{itemize}

\textbf{FrozenLake-v1:}
\begin{itemize}
  \item State space: 16 discrete states (4$\times$4 grid), from Gymnasium
  \item Action space: 4 discrete (left, down, right, up)
  \item Rewards: $0$ for each step, $+1$ for reaching the goal
  \item Terminal conditions: reaching the goal or falling into a hole
  \item Stochastic by default ($\frac{1}{3}$ probability for each direction)
\end{itemize}





\section{Section 2: Deliverables}

\subsection{GitHub Repository}
\begin{verbatim}
GitHub Repository: https://github.com/cooper-rm/rl-dynamic-programming

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

import subprocess
import os

REPORT_DIR = os.path.dirname(os.path.abspath(__file__))
TEX_FILE = os.path.join(REPORT_DIR, "Cooper_Morgan_Lab2.tex")
PDF_FILE = os.path.join(REPORT_DIR, "Cooper_Morgan_Lab2.pdf")

# --- IMAGE PATHS (update these to point to your saved plot files) ---
FIGURE_1 = "figures/deterministic_value_policy.png"
FIGURE_2 = "figures/stochastic_value_policy.png"
FIGURE_3 = "figures/convergence_comparison.png"
FIGURE_4 = "figures/frozenlake_value_policy.png"

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
collecting their values. During each loop,
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

I expect that all four DP algorithms will find the optimal solution, but I 
anticipate in-place value iteration to work quicker than the rest. I also think 
the stochastic environments will be more difficult to find a solution for since 
they incorporate randomness into the action outcomes. The agent will be required 
to think differently relative to the stochastic environment. 


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

For this project I implemented a custom GridWorld environment following 
Gymnasium's API with a full transition model P[s][a], specifically to 
facilitate DP. For GridWorld, I implemented four DP algorithms: synchronous 
policy iteration, synchronous value iteration, in-place policy iteration, 
and in-place value iteration. I ran experiments in both deterministic and 
stochastic environments, and applied all the same ideas to Gymnasium's 
FrozenLake-v1. The key hyperparameters were gamma=0.99, theta=1e-8, and 
a step reward of -1.


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

In the deterministic environment, all four algorithms converged successfully
to the same optimal policy (Figure~\ref{fig:figure1}). Since the step reward was $-1$, states near the
goal have values close to $0$, whereas states that are far away from the goal
are more negative.

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{""" + FIGURE_1 + r"""}
\caption{Deterministic GridWorld value function (left) and optimal policy (right),
computed via VI In-Place. The heatmap displays $V(s)$ at each grid cell with obstacles
marked as X and the goal marked as G. The quiver plot shows the greedy action at
each non-terminal state.}
\label{fig:figure1}
\end{figure}

In the stochastic environment (Figure~\ref{fig:figure2}), the values became even more negative everywhere
because each action no longer leads to a guaranteed state. The policy also shifted
towards avoiding risky positions where a slip would cost the agent more penalty.

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{""" + FIGURE_2 + r"""}
\caption{Stochastic GridWorld value function (left) and optimal policy (right),
computed via VI In-Place with slip\_prob $= 0.1$. Same layout as Figure 1 but with
80/10/10 transition probabilities. The heatmap shows $V(s)$ and the quiver plot shows
the greedy action at each state.}
\label{fig:figure2}
\end{figure}

As shown in Figure~\ref{fig:figure3}, in-place algorithms converge quicker than
synchronous algorithms. This is because values propagate faster through all of
the states in the environment. Faster propagation is a result of in-place updates
having access to state $N-1$'s new value in the same sweep, whereas synchronous algorithms
must wait for the entire sweep to finish before seeing state value changes.

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{""" + FIGURE_3 + r"""}
\caption{Convergence curves showing max value change (delta) on a log scale per
sweep across all three environments. Each line represents one of the four algorithm
variants (PI Sync, PI In-Place, VI Sync, VI In-Place).}
\label{fig:figure3}
\end{figure}

Finally, in the FrozenLake-v1 (Figure~\ref{fig:figure4}) application we see the exact 
same reaction to determinism, stochasticity, in-place, and synchronous algorithms. Despite
the differing environment structure, the same algorithms converge the quickest to
an optimal policy. This validates my hypothesis that all four algorithms
converge to the same optimal policy regardless of environment structure, and that the
in-place value iteration algorithm converges the fastest.


\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{""" + FIGURE_4 + r"""}
\caption{FrozenLake-v1 value function (left) and optimal policy (right), computed
via VI In-Place. Holes are marked as X (terminal, reward $= 0$) and the goal as G
(terminal, reward $= 1$). The environment is stochastic with $\frac{1}{3}$ probability
for each direction.}
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

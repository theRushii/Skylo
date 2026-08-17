\# Skylo — AI Coding Workspace



> \*\*Initial Project Name:\*\* Skylo  

> \*\*Project Type:\*\* AI-Powered Developer Tool  

> \*\*Status:\*\* Research / MVP Development  

> \*\*Primary Model:\*\* NVIDIA Nemotron  

> \*\*Target Users:\*\* Developers, Students, and Programming Learners



\---



\## 1. Project Overview



Skylo is an AI-powered coding workspace designed to help developers, students, and programming learners understand, create, modify, and improve software through natural-language interaction.



The project is inspired by modern AI coding assistants such as Claude and aims to explore how an AI coding assistant can combine conversational assistance, persistent code artifacts, project context, and eventually tool-based code development and verification within a single environment.



The initial version of Skylo will focus on providing a lightweight coding assistant powered by a Nemotron-based large language model, with an interactive Artifact Window for viewing and iterating on generated code.



The project will progressively evolve from a simple AI coding assistant into a context-aware and tool-using developer workspace.



\---



\# 2. Problem Statement



Modern AI coding assistants can generate code, explain errors, debug programs, and assist developers with software projects. However, the development workflow can become fragmented when users have to switch between separate tools for conversation, code generation, editing, previewing, debugging, and project management.



Students and developers also need more than simply generated code. They need to understand the reasoning behind implementations, provide relevant project context, iterate on generated code, and verify whether the resulting code actually works.



Skylo aims to address this problem by providing an integrated AI coding workspace that combines:



\- Conversational coding assistance

\- Persistent code artifacts

\- Relevant project context

\- Code generation and modification

\- Interactive development

\- Future tool-based execution and verification



The initial implementation will focus on building a practical and lightweight MVP while establishing an architecture that can later support agentic development workflows.



\---



\# 3. Project Goals



\## 3.1 Primary Goals



Skylo aims to:



1\. Provide an AI assistant specifically focused on software development.

2\. Generate and explain programming code using natural-language instructions.

3\. Provide an interactive Artifact Window for generated code.

4\. Maintain relevant conversation and project context.

5\. Allow users to iteratively modify generated code.

6\. Establish an architecture capable of supporting tool-based AI agents.

7\. Eventually support code execution and verification.

8\. Maintain human control over important development actions.



\---



\# 4. Target Users



Skylo is primarily designed for:



\### Developers



Developers can use Skylo for:



\- Code generation

\- Debugging

\- Refactoring

\- Code explanation

\- Code review

\- Documentation

\- Project assistance



\### Students



Students can use Skylo to:



\- Learn programming concepts

\- Understand existing code

\- Generate project prototypes

\- Debug assignments and projects

\- Practice programming

\- Ask technical questions



\### Programming Learners



Learners can use Skylo as an interactive programming assistant that explains concepts and provides guided assistance rather than simply returning answers.



\---



\# 5. Core Features



\## 5.1 AI Coding Chat



Skylo will provide a conversational interface where users can ask programming-related questions.



Examples:



\- "Create a FastAPI REST API."

\- "Explain this Python function."

\- "Why am I getting this error?"

\- "Refactor this code."

\- "Add authentication to this API."



\---



\## 5.2 Artifact Window



Skylo will provide an interactive Artifact Window for generated code.



Instead of displaying code only as a chat response, the generated code can become a persistent artifact that can be viewed and modified.



Planned capabilities include:



\- Artifact creation

\- Artifact editing

\- Syntax highlighting

\- Preview

\- Code regeneration

\- Iteration

\- Download/export

\- Artifact history/versioning



\---



\## 5.3 Context Management



Skylo will eventually use a Context Manager to determine which information should be provided to the language model.



Potential context sources include:



\- Current conversation

\- User instructions

\- Uploaded files

\- Current artifact

\- Relevant project files

\- Tool execution results



The system should avoid unnecessarily sending the entire project to the model when only a small subset of files is relevant.



\---



\## 5.4 Project Context



Future versions of Skylo will support project-level context.



Example:



```text

project/

├── src/

│   ├── main.py

│   ├── auth.py

│   └── database.py

├── tests/

├── requirements.txt

└── README.md


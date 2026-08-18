# Skylo — System Architecture Overview

## 1. Purpose

Skylo is an AI-powered coding workspace designed specifically for:

- New programmers
- Programming students
- Beginner developers
- Experienced developers

The goal is to provide an AI coding environment that combines conversational assistance, project context, code generation, file creation, code execution, debugging, verification, and deployment assistance.

Skylo is intended to be a free/open-source alternative to AI coding assistants such as Claude Code.

---

## 2. Core Product Idea

Skylo is not intended to be only a chatbot.

The core workflow is:

User
↓
Chat Interface
↓
Backend Orchestrator
↓
Context Manager
↓
LLM
↓
Tool Layer
↓
Execution / Verification
↓
Result
↓
LLM
↓
User

The LLM generates reasoning and proposed actions, while the tool layer performs actual operations.

---

## 3. Initial Target Capabilities

### 3.1 Conversational Coding

Skylo should allow users to:

- Ask programming questions
- Generate code
- Explain code
- Debug code
- Refactor code
- Improve existing code
- Learn programming concepts
- Ask questions about their project

### 3.2 Project Context

Skylo should eventually understand:

- Project structure
- Source files
- Configuration files
- Dependencies
- Documentation
- Existing code
- Relevant previous conversation

### 3.3 File Operations

Skylo should eventually be able to:

- Create files
- Read files
- Modify files
- Delete files with appropriate safeguards
- Show proposed changes
- Track changed files

### 3.4 Artifact Window

Skylo should provide an Artifact Window where generated files and code can be:

- Viewed
- Edited
- Created
- Organized
- Previewed when possible
- Downloaded/exported

The Artifact Window is a core product feature rather than simply a code block inside chat.

### 3.5 Code Execution

Skylo should eventually be able to:

- Execute supported code
- Run tests
- Capture stdout
- Capture stderr
- Detect exit codes
- Return execution results to the LLM

### 3.6 Verification Loop

Skylo should use an iterative workflow:

1. Understand the request
2. Inspect relevant project context
3. Plan the change
4. Generate or modify code
5. Execute or test the change
6. Observe the result
7. Diagnose failures
8. Correct the implementation
9. Verify again
10. Present the final result

---

## 4. Minimum Architecture

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Frontend     │
                    │ Chat + Artifact │
                    │     Window      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Backend     │
                    │  Orchestrator   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Context Manager │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      LLM        │
                    │   Nemotron      │
                    └────────┬────────┘
                             │
                       Tool Calls
                             │
                             ▼
                    ┌─────────────────┐
                    │   Tool Layer    │
                    │ Files / Search  │
                    │ Shell / Git     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Execution &   │
                    │   Verification  │
                    └────────┬────────┘
                             │
                             └──────────► LLM
                                            │
                                            ▼
                                          User
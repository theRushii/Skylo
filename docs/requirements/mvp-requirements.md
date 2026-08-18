# Skylo — MVP Requirements

## 1. Purpose

This document defines the Minimum Viable Product (MVP) requirements for Skylo.

The MVP should establish the core foundation of an AI-powered coding assistant before advanced features are implemented.

---

## 2. Target Users

Skylo initially targets:

1. New programmers
2. Programming students
3. Beginner developers
4. Experienced developers

---

## 3. Core User Problems

Skylo should help users:

- Understand programming concepts
- Write code
- Modify existing code
- Debug code
- Understand project structure
- Create project files
- Run code
- Run tests
- Understand execution failures
- Iterate on implementations

---

## 4. MVP Functional Requirements

### FR-001 — Chat

The user must be able to send a programming-related message and receive an AI response.

### FR-002 — LLM Integration

The backend must be able to communicate with the configured LLM.

Initial target:

- NVIDIA Nemotron

The model provider should be abstracted so that another model can be added later without rewriting the entire application.

### FR-003 — Conversation State

Skylo must maintain the conversation context required for the current session.

### FR-004 — Project Awareness

Skylo must eventually be able to inspect files inside an authorized project directory.

### FR-005 — File Reading

The system must be able to read an authorized project file.

### FR-006 — File Creation

The system must be able to create a new file inside an authorized project directory.

### FR-007 — File Modification

The system must be able to modify an existing authorized file.

### FR-008 — File Visibility

The user should be able to see which files Skylo creates or modifies.

### FR-009 — Artifact Window

Skylo must provide a dedicated Artifact Window for generated files and code.

The Artifact Window should eventually support:

- File display
- Code editing
- File creation
- File organization
- Preview where applicable

### FR-010 — Tool Execution

The LLM must be able to request controlled tools.

Initial tool candidates:

- Read file
- Write file
- List files
- Search files
- Execute command
- Run tests
- Git status
- Git diff

### FR-011 — Code Execution

Skylo must be able to execute supported code through a controlled execution environment.

### FR-012 — Test Execution

Skylo must be able to run project tests and return their results.

### FR-013 — Verification

Skylo should be able to use execution and test results to determine whether a generated change worked.

### FR-014 — Iterative Agent Loop

Skylo must eventually support:

User Request
→ Inspect
→ Plan
→ Act
→ Execute
→ Observe
→ Correct
→ Verify
→ Respond

### FR-015 — Error Handling

Tool and execution failures must be returned to the agent in a structured way.

---

# 5. Non-Functional Requirements

## NFR-001 — Security

Skylo must not provide unrestricted access to the user's computer.

Tool permissions must be controlled.

## NFR-002 — Reliability

The system should prefer verified execution results over assumptions made by the LLM.

## NFR-003 — Extensibility

The architecture should allow:

- Additional LLM providers
- Additional tools
- Additional programming languages
- Additional artifact types

without major architectural changes.

## NFR-004 — Maintainability

Code should be separated into clear responsibilities.

## NFR-005 — Observability

Important operations should eventually be logged so failures can be diagnosed.

## NFR-006 — Performance

The system should avoid sending unnecessary project data to the LLM.

---

# 6. MVP Non-Goals

The MVP will not attempt to:

- Build a complete IDE
- Train a foundation model
- Replace every Claude feature
- Support every programming language
- Provide unrestricted shell access
- Automatically deploy arbitrary applications
- Guarantee generated code is correct
- Build a custom operating system sandbox
- Implement every possible MCP integration

---

# 7. MVP Success Criteria

The MVP should eventually allow a user to perform a workflow such as:

1. Open a Skylo project.
2. Ask Skylo to create a small application.
3. Skylo understands the request.
4. Skylo creates the required files.
5. The files appear in the Artifact Window.
6. Skylo runs the application or tests.
7. Skylo observes the result.
8. If something fails, Skylo analyzes the failure.
9. Skylo modifies the appropriate file.
10. Skylo runs the verification again.
11. Skylo reports the final result to the user.

---

# 8. Development Priority

## Phase 1 — Foundation

- Project structure
- Backend
- Frontend
- API
- Configuration
- Logging
- Testing

## Phase 2 — Chat

- LLM provider abstraction
- Nemotron integration
- Chat API
- Streaming
- Conversation state

## Phase 3 — Project Awareness

- File tree
- File reading
- Context management
- Project search

## Phase 4 — Artifacts

- Artifact Window
- File creation
- File editing
- File preview

## Phase 5 — Agent

- Tool definitions
- Tool execution
- Agent loop
- Iteration limits
- Error handling

## Phase 6 — Verification

- Code execution
- Test execution
- Execution results
- Automatic correction loop

## Phase 7 — Developer Workflow

- Git integration
- Diff visualization
- Commit assistance
- Deployment assistance

---

# 9. Core Product Principle

Skylo should not be judged by how much code it can generate.

It should be judged by how reliably it can help a user go from:

Problem
→ Understanding
→ Implementation
→ Execution
→ Verification
→ Working Result

The goal is not simply to generate code.

The goal is to help produce **working software**.ch0
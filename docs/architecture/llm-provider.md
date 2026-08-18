# Skylo — LLM Provider Architecture

## 1. Purpose

Skylo must communicate with Large Language Models through an abstraction layer.

The application should not be tightly coupled to a single model provider.

---

## 2. Initial Model

The initial target model is:

- NVIDIA Nemotron

Nemotron will be implemented as the first LLM provider.

---

## 3. Provider Abstraction

The rest of Skylo should communicate with a common LLM interface.

Conceptually:

    Skylo Application
           |
           v
      LLM Service
           |
           v
    Provider Interface
           |
       +---+---+
       |       |
       v       v
    Nemotron  Future Provider

---

## 4. Responsibilities

### LLM Service

The LLM Service is responsible for:

- Sending messages to the selected model
- Receiving model responses
- Managing model configuration
- Handling provider errors
- Supporting streaming responses
- Providing a consistent interface to the rest of Skylo

---

## 5. Provider Responsibilities

Each provider is responsible for:

- Authentication
- API communication
- Request formatting
- Response parsing
- Provider-specific errors
- Provider-specific configuration

---

## 6. Application Rule

Application components must NOT directly call a specific model provider.

Bad:

    nemotron.generate(...)

inside random application modules.

Preferred:

    llm.generate(...)

The LLM service decides which provider handles the request.

---

## 7. Future Providers

The architecture should allow future support for:

- Local models
- OpenAI-compatible APIs
- Ollama
- Additional NVIDIA models
- Other cloud providers

Adding a provider should require implementing the provider interface rather than rewriting the application.

---

## 8. Configuration

Model configuration should eventually be controlled through environment variables or application configuration.

Examples:

    LLM_PROVIDER=nemotron
    LLM_MODEL=<configured-model>
    LLM_API_KEY=<secret>

Secrets must never be committed to Git.

---

## 9. Streaming

Skylo should eventually support streaming responses.

Instead of:

    User waits
        ↓
    Complete response
        ↓
    Display

Skylo should support:

    User
      ↓
    LLM
      ↓
    Token stream
      ↓
    Backend
      ↓
    Frontend
      ↓
    User sees response progressively

---

## 10. Tool Calling

The LLM provider layer should support model responses that request tools.

Conceptually:

    User
      ↓
    LLM
      ↓
    Tool Request
      ↓
    Skylo Tool Manager
      ↓
    Tool Execution
      ↓
    Tool Result
      ↓
    LLM
      ↓
    Final Response

The LLM does not directly receive unrestricted operating-system access.

---

## 11. Security Boundary

The LLM is untrusted from the operating system's perspective.

The backend must control:

- Which tools are available
- Which directories can be accessed
- Which commands can be executed
- What files can be modified
- Maximum execution time
- Maximum tool iterations

The model may request an operation, but the Skylo backend decides whether the operation is permitted.

---

## 12. Error Handling

Provider failures must be converted into structured application errors.

Examples:

- Authentication failure
- Invalid API request
- Rate limit
- Model unavailable
- Network failure
- Timeout
- Invalid model response

The frontend should receive a useful error rather than a raw provider exception.

---

## 13. Design Goal

The LLM provider architecture should allow Skylo to evolve from:

    One model

to:

    Multiple models
    Multiple providers
    Local models
    Cloud models

without requiring a redesign of the entire application.
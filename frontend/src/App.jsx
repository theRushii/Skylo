import { useEffect, useRef, useState } from 'react'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'

import './App.css'


function getArtifactFilename(language, code) {
  const normalizedLanguage = language.toLowerCase()

  if (normalizedLanguage === 'java') {
    const classMatch = code.match(
      /public\s+class\s+([A-Za-z_][A-Za-z0-9_]*)/
    )

    if (classMatch) {
      return `${classMatch[1]}.java`
    }

    return 'Main.java'
  }

  const filenames = {
    python: 'main.py',
    py: 'main.py',
    javascript: 'app.js',
    js: 'app.js',
    jsx: 'App.jsx',
    typescript: 'app.ts',
    ts: 'app.ts',
    tsx: 'App.tsx',
    html: 'index.html',
    css: 'styles.css',
    c: 'main.c',
    cpp: 'main.cpp',
    csharp: 'Program.cs',
    cs: 'Program.cs',
    go: 'main.go',
    rust: 'main.rs',
    rs: 'main.rs',
    json: 'data.json',
    sql: 'query.sql',
    bash: 'script.sh',
    shell: 'script.sh',
    sh: 'script.sh',
  }

  return filenames[normalizedLanguage] || 'artifact.txt'
}


function extractLatestArtifact(text) {
  const codeBlockPattern = /```([A-Za-z0-9_+-]*)\s*\n([\s\S]*?)```/g

  let match
  let latestMatch = null

  while ((match = codeBlockPattern.exec(text)) !== null) {
    latestMatch = match
  }

  if (!latestMatch) {
    return null
  }

  const language = latestMatch[1] || 'text'
  const code = latestMatch[2].trim()

  return {
    language,
    filename: getArtifactFilename(language, code),
    content: code,
  }
}


function App() {
  const [message, setMessage] = useState('')
  const [messages, setMessages] = useState([])
  const [isStreaming, setIsStreaming] = useState(false)
  const [artifact, setArtifact] = useState(null)

  const messagesEndRef = useRef(null)

  const conversationId = 'skylo-local-session'


  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: 'smooth',
    })
  }, [messages])


  async function sendMessage() {
    const trimmedMessage = message.trim()

    if (!trimmedMessage || isStreaming) {
      return
    }

    const userMessage = {
      role: 'user',
      content: trimmedMessage,
    }

    setMessages((current) => [
      ...current,
      userMessage,
      {
        role: 'assistant',
        content: '',
      },
    ])

    setMessage('')
    setIsStreaming(true)

    try {
      const response = await fetch(
        'http://127.0.0.1:8000/chat/stream',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            conversation_id: conversationId,
            message: trimmedMessage,
          }),
        }
      )

      if (!response.ok) {
        throw new Error(`Request failed: ${response.status}`)
      }

      if (!response.body) {
        throw new Error('Streaming response body is missing.')
      }

      const reader = response.body.getReader()
      const decoder = new TextDecoder()

      while (true) {
        const { value, done } = await reader.read()

        if (done) {
          break
        }

        const chunk = decoder.decode(value, {
          stream: true,
        })

        setMessages((current) => {
          const updated = [...current]
          const lastIndex = updated.length - 1
          const lastMessage = updated[lastIndex]

          const updatedContent =
            lastMessage.content + chunk

          updated[lastIndex] = {
            ...lastMessage,
            content: updatedContent,
          }

          const detectedArtifact =
            extractLatestArtifact(updatedContent)

          if (detectedArtifact) {
            setArtifact(detectedArtifact)
          }

          return updated
        })
      }
    } catch (error) {
      setMessages((current) => {
        const updated = [...current]

        updated[updated.length - 1] = {
          role: 'assistant',
          content: `Error: ${error.message}`,
        }

        return updated
      })
    } finally {
      setIsStreaming(false)
    }
  }


  function handleKeyDown(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault()
      sendMessage()
    }
  }


  return (
    <main className="skylo-app">
      <section className="chat-panel">
        <header className="panel-header">
          <h1>Skylo</h1>
          <span>AI Coding Workspace</span>
        </header>

        <div className="messages">
          {messages.length === 0 ? (
            <div className="empty-state">
              <h2>What are we building?</h2>

              <p>
                Ask Skylo to write, explain, debug, or improve code.
              </p>
            </div>
          ) : (
            <div className="message-list">
              {messages.map((item, index) => (
                <div
                  className={`message ${item.role}`}
                  key={index}
                >
                  <span className="message-role">
                    {item.role === 'user'
                      ? 'You'
                      : 'Skylo'}
                  </span>

                  <div className="message-content">
                    {item.role === 'assistant' ? (
                      item.content ? (
                        <ReactMarkdown
                          remarkPlugins={[remarkGfm]}
                        >
                          {item.content}
                        </ReactMarkdown>
                      ) : (
                        isStreaming &&
                        index === messages.length - 1 && (
                          <span>Thinking...</span>
                        )
                      )
                    ) : (
                      item.content
                    )}
                  </div>
                </div>
              ))}

              <div ref={messagesEndRef} />
            </div>
          )}
        </div>

        <div className="composer">
          <textarea
            value={message}
            onChange={(event) =>
              setMessage(event.target.value)
            }
            onKeyDown={handleKeyDown}
            placeholder="Ask Skylo about your code..."
            rows="3"
            disabled={isStreaming}
          />

          <button
            type="button"
            onClick={sendMessage}
            disabled={isStreaming}
          >
            {isStreaming
              ? 'Generating...'
              : 'Send'}
          </button>
        </div>
      </section>

      <aside className="artifact-panel">
        <header className="panel-header">
          <h2>Artifact</h2>

          <span>
            {artifact
              ? artifact.filename
              : 'No artifact yet'}
          </span>
        </header>

        <div className="artifact-content">
          {artifact ? (
            <div className="artifact-code">
              <div className="artifact-toolbar">
                <span>{artifact.filename}</span>
                <span>{artifact.language}</span>
              </div>

              <pre>
                <code>{artifact.content}</code>
              </pre>
            </div>
          ) : (
            <p>
              Generated code and files will appear here.
            </p>
          )}
        </div>
      </aside>
    </main>
  )
}

export default App
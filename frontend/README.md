# Frontend – AI Campus Assistant

Goal: Simple, clean **chat UI** that talks to the `/chat` backend endpoint.

## Tasks

- Build a single-page app:
  - Text input + send button
  - Chat history display (user + assistant messages)
- Call the backend API:
  - `POST https://{api-id}.execute-api.{region}.amazonaws.com/prod/chat`
  - Body: `{ "message": "..." }`
- Render responses as chat bubbles and simple cards.

## Dev

For now, this is plain HTML/CSS/JS.

Later, we *may* convert to React/Vite if time allows.

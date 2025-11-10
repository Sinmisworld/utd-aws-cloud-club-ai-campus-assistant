# Backend – Chat Handler & Tools

This folder contains:

- `chat-handler/app.py` – main Lambda handler for `/chat`
- `tools/dining_tool.py` – Dining intent
- `tools/events_tool.py` – Events intent
- `tools/parking_tool.py` – Parking intent

The Chat Lambda:
1. Receives `{ "message": "..." }`
2. Calls Amazon Bedrock (Claude 3.5) with a system prompt + tool descriptions
3. Decides which tool to call
4. Invokes the tool function and returns a formatted answer

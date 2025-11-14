import json
import os
import boto3


REGION = os.getenv("AWS_REGION", "us-east-1")
MODEL = os.getenv("BEDROCK_MODEL", "anthropic.claude-3-5-sonnet-20240620-v1:0")

SYSTEM_PROMPT = """
    You are an intent classifier + argument extractor for a UTD Campus Assistant.

    Return ONLY JSON:
    {
        "intent": "dining | events | parking | general",
        "args": {},
        "answer": ""
    }
"""


def classify_with_bedrock(message: str):
    client = boto3.client("bedrock-runtime", region_name=REGION)

    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "system": SYSTEM_PROMPT,
        "max_tokens": 300,
        "temperature": 0.2,
        "messages": [{"role": "user", "content": [{"type": "text", "text": message}]}],
    }

    response = client.invoke_model(
        modelId=MODEL,
        body=json.dumps(payload).encode("utf-8"),
        contentType="application/json",
        accept="application/json",
    )

    result = json.loads(response["body"].read())
    print("Result from Bedrock (invoke_model):", result)

    # Extract raw text from model output
    output = ""
    for part in result.get("content", []):
        if part.get("type") == "text":
            output += part["text"]

    output = output.strip()

    # Try to parse JSON from model
    try:
        parsed = json.loads(output)
    except:
        return "general", {"answer": output}

    return parsed.get("intent", "general"), parsed.get("args", {})


def lambda_handler(event, context):
    try:
        body_raw = event.get("body", "{}")
        if isinstance(body_raw, str):
            body = json.loads(body_raw)
        else:
            body = body_raw

        message = (body.get("message") or "").strip()
        if not message:
            return _response(400, {"error": "Message is required."})

        intent, args = classify_with_bedrock(message)

        return _response(200, {"intent": intent, "tool_args": args})

    except Exception as e:
        return _response(500, {"error": str(e)})


def _response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": body,
    }

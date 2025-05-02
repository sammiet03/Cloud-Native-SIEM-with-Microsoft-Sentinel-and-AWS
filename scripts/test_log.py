import json, requests, hashlib, hmac, base64
from datetime import datetime, timezone

workspace_id = os.getenv("SENTINEL_WORKSPACE_ID")
shared_key = os.getenv("SENTINEL_SHARED_KEY")
log_type = 'TestLog'
url = f'https://{workspace_id}.ods.opinsights.azure.com/api/logs?api-version=2016-04-01'

def build_signature(workspace_id, shared_key, date, content_length, method, content_type, resource):
    x_headers = f'x-ms-date:{date}'
    string_to_hash = f'{method}\n{content_length}\n{content_type}\n{x_headers}\n{resource}'
    bytes_to_hash = bytes(string_to_hash, encoding='utf-8')
    decoded_key = base64.b64decode(shared_key)
    encoded_hash = base64.b64encode(
        hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()
    ).decode()
    return f'SharedKey {workspace_id}:{encoded_hash}'

# Generate a compliant UTC timestamp in RFC 3339 format
body = json.dumps([{
    "Message": "🚀 This is a test log from EC2 with fixed timestamp",
    "Source": "ManualTest",
    "Level": "Info",
    "TimeGenerated": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
}])

method = 'POST'
content_type = 'application/json'
resource = '/api/logs'
rfc1123date = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
content_length = len(body)
signature = build_signature(workspace_id, shared_key, rfc1123date, content_length, method, content_type, resource)

headers = {
    'Content-Type': content_type,
    'Authorization': signature,
    'Log-Type': log_type,
    'x-ms-date': rfc1123date
}

r = requests.post(url, data=body, headers=headers)
print(r.status_code, r.text)


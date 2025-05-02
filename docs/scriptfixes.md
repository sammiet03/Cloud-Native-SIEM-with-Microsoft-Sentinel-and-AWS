### No logs on Azure Sentinel

## send_logs_to_sentinel.py 
- lines skipping
- no logs on Azure Sentinel 
- TimeGenerated is present and in proper format
- Logs will appear in SysmonLogs_CL in Sentinel immediately after being sent
- proper RFC 3339 UTC timestamps for Sentinel compatibility:
```
import json, requests, hashlib, hmac, base64
from datetime import datetime, timezone
```
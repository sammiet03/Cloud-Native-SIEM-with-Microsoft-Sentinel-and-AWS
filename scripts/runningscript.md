### For best practice storing variables

Before runing the script: 
- On Powershell: 
```
$env:SENTINEL_WORKSPACE_ID = "your-id-here"
$env:SENTINEL_SHARED_KEY = "your-key-here"
```

Then: 
```
python send_logs_to_sentinel.py
```


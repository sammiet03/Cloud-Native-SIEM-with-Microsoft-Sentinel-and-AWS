### 🔍 1. T1003.001 – Credential Dumping (LSASS)
Simulated using: Invoke-AtomicTest T1003.001 -TestNumbers 2 -Force

### 🔎 Sentinel Query:
```
SysmonLogs_CL
| where CommandLine_s has "procdump" or CommandLine_s has "lsass"
| sort by TimeGenerated desc
```
- ✅ This captures any attempt to dump lsass.exe memory — either simulated or real.

### 🔍 2. T1055.001 – Process Injection
Simulated using: Invoke-AtomicTest T1055.001 -TestNumbers 1 -Force

### 🔎 Sentinel Query:
```
SysmonLogs_CL
| where CommandLine_s has "ProcessInjection" or Description_s has "Inject"
| sort by TimeGenerated desc
```
- ✅ Also check EventID 8 or 10 if you parse those in your Sysmon config:

```
SysmonLogs_CL
| where Id_d in (8, 10)
```


### 🔍 3. T1547.001 – Persistence via Registry Run Keys
Simulated using: Invoke-AtomicTest T1547.001 -TestNumbers 1 -Force

### 🔎 Sentinel Query:
```
SysmonLogs_CL
| where CommandLine_s has "reg" or TargetObject_s has "Run"
| sort by TimeGenerated desc
```

- ✅ This targets reg add commands and Registry value sets that persist on reboot.

### Bonus: 🧠 Confirm Log Volume per Technique
### 🔎 Count all events with "powershell":
```
SysmonLogs_CL
| where CommandLine_s has "powershell"
| summarize count() by bin(TimeGenerated, 1h)
```

### 🔎 Count by Event ID:
```
SysmonLogs_CL
| summarize count() by Id_d
```
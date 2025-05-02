```
SysmonLogs_CL
| extend logtext = tostring(pack_all())
| where logtext has_any (
    "powershell",
    "procdump",
    "reg add",
    "ProcessInjection",
    "tasklist",
    "inject.txt",
    "notepad",
    "lsass",
    "Credential Dump",
    "mimikatz"
)
| summarize Count = count() by Technique = case(
    logtext has "powershell", "T1059 - PowerShell Execution",
    logtext has "reg add", "T1547 - Registry Persistence (Run Key)",
    logtext has_any ("procdump", "lsass", "Credential Dump", "mimikatz"), "T1003.001 - Credential Dumping (LSASS)",
    logtext has "ProcessInjection", "T1055 - Process Injection",
    logtext has_any ("tasklist", "inject.txt", "notepad"), "T1055/T1082 - Discovery or Injection Sim (tasklist)",
    "Other"
)
```
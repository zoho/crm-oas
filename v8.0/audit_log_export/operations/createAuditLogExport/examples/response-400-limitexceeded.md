More than one audit_log_export item supplied

```json
{
  "audit_log_export": [
    {
      "code": "LIMIT_EXCEEDED",
      "status": "error",
      "message": "The audit_log_export jsonarray size should not exceed one",
      "details": {
        "api_name": "audit_log_export",
        "json_path": "$.audit_log_export[1]",
        "limit": "1"
      }
    }
  ]
}
```

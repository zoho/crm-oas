Audited time range exceeds 6 months

```json
{
  "audit_log_export": [
    {
      "code": "NOT_ALLOWED",
      "status": "error",
      "message": "Logs only within 6 month intervals are allowed to be fetched",
      "details": {
        "api_name": "value",
        "json_path": "$.audit_log_export[0].criteria.value"
      }
    }
  ]
}
```

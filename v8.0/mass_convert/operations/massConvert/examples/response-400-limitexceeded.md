Example of ids array exceeds the maximum limit of 50 entries.

```json
{
  "code": "LIMIT_EXCEEDED",
  "message": "Limit exceeded for mass convert",
  "status": "error",
  "details": {
    "limit": 50,
    "limit_due_to": [
      {
        "api_name": "ids",
        "json_path": "$.ids"
      }
    ]
  }
}
```

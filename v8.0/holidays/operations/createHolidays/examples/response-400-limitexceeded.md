Holiday limit exceeded for the specified type

```json
{
  "holidays": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 52,
        "limit_due_to": [
          {
            "api_name": "type",
            "json_path": "$.holidays[0].type"
          }
        ]
      },
      "message": "Holidays limit exceeds",
      "status": "error"
    }
  ]
}
```

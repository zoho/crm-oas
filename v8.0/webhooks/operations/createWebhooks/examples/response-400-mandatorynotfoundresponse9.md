Error response when the name key is missing.

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.webhooks[*].name"
      },
      "status": "error"
    }
  ]
}
```

Error response when the authentication is missing.

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "authentication",
        "json_path": "$.webhooks[*].authentication"
      },
      "status": "error"
    }
  ]
}
```

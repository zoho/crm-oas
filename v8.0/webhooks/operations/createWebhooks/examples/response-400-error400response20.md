Error response when type is missing in authentication.

```json
{
  "webhooks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "type",
      "json_path": "$.webhooks[*].authentication.type"
    },
    "status": "error"
  }
}
```

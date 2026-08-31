Error response when type is missing in body.

```json
{
  "webhooks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "type",
      "json_path": "$.webhooks[*].body.type"
    },
    "status": "error"
  }
}
```

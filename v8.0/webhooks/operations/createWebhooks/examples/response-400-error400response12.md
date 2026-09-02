Error response when format is missing in body.

```json
{
  "webhooks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "format",
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```

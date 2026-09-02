Error response when body.type value is not accepted.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.webhooks[0].body.type"
      },
      "message": "invalid body type passed",
      "status": "error"
    }
  ]
}
```

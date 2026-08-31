Error response for an empty URL field.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "url",
        "json_path": "$.webhooks[0].url"
      },
      "message": "Empty value is not allowed",
      "status": "error"
    }
  ]
}
```

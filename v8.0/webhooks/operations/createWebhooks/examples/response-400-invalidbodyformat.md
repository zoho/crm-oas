Error respons when body.format value is not accepted.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "format",
        "json_path": "$.webhooks[0].body.format"
      },
      "message": "invalid format passed in body",
      "status": "error"
    }
  ]
}
```

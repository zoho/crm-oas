Error response when url key value fails SSRF validation.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "url",
        "json_path": "$.webhooks[0].url"
      },
      "message": "Url you've configured is not secure",
      "status": "error"
    }
  ]
}
```

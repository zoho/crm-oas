INVALID_DATA error for invalid webhook ID in the request body

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.webhooks[0].id"
      },
      "message": "The ID given is invalid",
      "status": "error"
    }
  ]
}
```

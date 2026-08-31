Error response when invalid ID given for module.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.webhooks[0].module.id"
      },
      "message": "the module id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

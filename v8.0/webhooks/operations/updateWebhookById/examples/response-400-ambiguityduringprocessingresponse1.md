Module id and api_name refer to different modules

```json
{
  "webhooks": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.webhooks[0].module.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.webhooks[0].module.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

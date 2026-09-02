API name and ID do not match

```json
{
  "data": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "api_name",
            "json_path": "$.data[0].convert_to[0].module.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.data[0].convert_to[0].module.id"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

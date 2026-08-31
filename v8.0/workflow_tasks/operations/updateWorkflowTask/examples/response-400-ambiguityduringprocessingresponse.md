AMBIGUITY_DURING_PROCESSING: field.id and field.api_name conflict

```json
{
  "tasks": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.tasks[0].field_mappings[0].field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.tasks[0].field_mappings[0].field.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

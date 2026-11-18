AMBIGUITY_DURING_PROCESSING error for a different field ID in a draft clone

```json
{
  "blueprints": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "type",
            "json_path": "$.blueprints[0].type"
          },
          {
            "api_name": "id",
            "json_path": "$.blueprints[0].field.id"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

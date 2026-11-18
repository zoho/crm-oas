AMBIGUITY_DURING_PROCESSING error for the field property

```json
{
  "blueprints": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.blueprints[0].field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.blueprints[0].field.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

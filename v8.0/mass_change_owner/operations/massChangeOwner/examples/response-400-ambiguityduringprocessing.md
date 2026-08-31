Example of ambiguous criteria field with both id and api_name provided.

```json
{
  "code": "AMBIGUITY_DURING_PROCESSING",
  "details": {
    "ambiguity_due_to": [
      {
        "api_name": "id",
        "json_path": "$.criteria.field.id"
      },
      {
        "api_name": "api_name",
        "json_path": "$.criteria.field.api_name"
      }
    ]
  },
  "message": "required field not found",
  "status": "error"
}
```

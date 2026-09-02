Module ID and module API name refer to different modules

```json
{
  "code": "AMBIGUITY_DURING_PROCESSING",
  "status": "error",
  "message": "ambiguous module identifiers",
  "details": {
    "ambiguity_due_to": [
      {
        "api_name": "id",
        "json_path": "$.mass_delete[0].module.id"
      },
      {
        "api_name": "api_name",
        "json_path": "$.mass_delete[0].module.api_name"
      }
    ]
  }
}
```

Example of conflicting api_name and ID in a related_modules entry.

```json
{
  "code": "AMBIGUITY_DURING_PROCESSING",
  "message": "two modules are different",
  "status": "error",
  "details": {
    "ambiguity_due_to": [
      {
        "api_name": "id",
        "json_path": "$.related_modules[0].id"
      },
      {
        "api_name": "api_name",
        "json_path": "$.related_modules[0].api_name"
      }
    ]
  }
}
```

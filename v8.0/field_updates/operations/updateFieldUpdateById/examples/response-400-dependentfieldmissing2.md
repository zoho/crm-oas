Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: notify)

```json
{
  "field_updates": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.field_updates[0].field"
        },
        "api_name": "notify",
        "json_path": "$.field_updates.notify"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

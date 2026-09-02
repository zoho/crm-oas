Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: dependent_fields)

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
        "api_name": "dependent_fields",
        "json_path": "$.field_updates[0].dependent_fields"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

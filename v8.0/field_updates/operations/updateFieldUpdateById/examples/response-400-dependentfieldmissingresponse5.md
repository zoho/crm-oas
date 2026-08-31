Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: related_records)

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
        "api_name": "related_records",
        "json_path": "$.field_updates[0].related_records"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

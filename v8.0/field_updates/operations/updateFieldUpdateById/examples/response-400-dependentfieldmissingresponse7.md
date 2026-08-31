Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: apply_assignment_threshold)

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
        "api_name": "apply_assignment_threshold",
        "json_path": "$.field_updates[0].apply_assignment_threshold"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

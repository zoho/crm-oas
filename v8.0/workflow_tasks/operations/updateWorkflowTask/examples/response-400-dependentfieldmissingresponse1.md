Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: field_name)

```json
{
  "tasks": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "api_name",
          "json_path": "$.tasks[0].field_mapping[1].field.api_name"
        },
        "api_name": "field_name",
        "json_path": "$.tasks[0].field_mapping[1].value.field_name"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

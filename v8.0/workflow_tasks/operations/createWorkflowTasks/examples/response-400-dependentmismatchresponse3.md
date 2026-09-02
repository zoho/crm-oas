Error response with code DEPENDENT_MISMATCH: Dependent Field is not matching

```json
{
  "tasks": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "id",
          "json_path": "$.tasks[0].field_mappings[2].field.id"
        },
        "api_name": "type",
        "json_path": "$.tasks[0].field_mappings[2].type"
      },
      "message": "Dependent Field is not matching",
      "status": "error"
    }
  ]
}
```

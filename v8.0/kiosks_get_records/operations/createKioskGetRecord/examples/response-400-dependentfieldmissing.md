parent_record_field required when type is child

```json
{
  "get_records": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.get_records[*].type"
        },
        "api_name": "parent_record_field",
        "json_path": "$.get_records[*].parent_record_field"
      },
      "status": "error"
    }
  ]
}
```

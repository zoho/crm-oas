Error response with code INVALID_DATA: Invalid data type (Field: field)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.tasks[*].field_mappings[*].field"
      },
      "status": "error"
    }
  ]
}
```

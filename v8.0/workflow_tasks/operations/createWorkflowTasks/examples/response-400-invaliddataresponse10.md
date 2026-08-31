Error response with code INVALID_DATA: Invalid data (Field: field)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "The field given seems to be invalid",
      "details": {
        "api_name": "field",
        "maximum_length": 2,
        "json_path": "$.tasks[*].field_mappings[*].field"
      },
      "status": "error"
    }
  ]
}
```

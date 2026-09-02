Error response with code INVALID_DATA: Invalid data (Field: value)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "The field given seems to be invalid",
      "details": {
        "api_name": "value",
        "maximum_length": 6,
        "json_path": "$.tasks[*].field_mappings[*].value"
      },
      "status": "error"
    }
  ]
}
```

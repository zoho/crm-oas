Error response with code DEPENDENT_MISMATCH: the given value is invalid (Field: value)

```json
{
  "tasks": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "api_name": "value",
        "json_path": "$.tasks[0].field_mapping[1].value",
        "dependee": {
          "api_name": "api_name",
          "json_path": "$.tasks[0].field_mapping[1].field.api_name"
        },
        "maximum_length": 150
      },
      "message": "the given value is invalid",
      "status": "error"
    }
  ]
}
```

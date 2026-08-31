Error response with code INVALID_DATA: Invalid data (Field: name)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "The field given seems to be invalid",
      "details": {
        "api_name": "name",
        "maximum_length": 7,
        "json_path": "$.tasks[*].name"
      },
      "status": "error"
    }
  ]
}
```

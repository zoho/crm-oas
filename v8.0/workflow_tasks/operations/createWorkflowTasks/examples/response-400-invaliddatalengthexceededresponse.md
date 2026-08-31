Error response with code INVALID_DATA: The length of the value exceeded the max limit

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "The length of the value exceeded the max limit",
      "details": {
        "maximum_length": 16,
        "api_name": "value",
        "json_path": "$.tasks[0].field_mappings[2].value"
      },
      "status": "error"
    }
  ]
}
```

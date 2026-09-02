Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "static",
          "merge_field",
          "execution_time"
        ],
        "json_path": "$.tasks[*].field_mappings[*].type"
      },
      "status": "error"
    }
  ]
}
```

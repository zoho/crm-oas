Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "text",
          "integer",
          "boolean",
          "date",
          "float"
        ],
        "json_path": "$.variables[*].type"
      },
      "status": "error"
    }
  ]
}
```

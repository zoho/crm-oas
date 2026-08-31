Error response with code INVALID_DATA: Invalid data (Field: update_type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "update_type",
        "supported_values": [
          "overwrite",
          "append"
        ],
        "json_path": "$.field_updates[*].update_type"
      },
      "status": "error"
    }
  ]
}
```

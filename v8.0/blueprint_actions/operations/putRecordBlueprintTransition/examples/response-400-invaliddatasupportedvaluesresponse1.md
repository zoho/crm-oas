Error response when a field value is not among the supported values

```json
{
  "blueprint": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "state",
        "json_path": "$.blueprint[*].state",
        "supported_values": [
          "draft",
          "completed"
        ]
      },
      "message": "Invalid data",
      "status": "error"
    }
  ]
}
```

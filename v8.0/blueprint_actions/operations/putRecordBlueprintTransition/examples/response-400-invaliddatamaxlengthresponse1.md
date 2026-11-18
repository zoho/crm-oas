Error response when a field value exceeds the allowed length

```json
{
  "blueprint": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "state",
        "maximum_length": 50,
        "json_path": "$.blueprint[*].state"
      },
      "message": "Invalid data",
      "status": "error"
    }
  ]
}
```

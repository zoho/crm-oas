INVALID_DATA error for a to_state value exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "to_state",
        "maximum_length": 1,
        "json_path": "$.blueprints[*].connections[*].to_state"
      },
      "status": "error"
    }
  ]
}
```

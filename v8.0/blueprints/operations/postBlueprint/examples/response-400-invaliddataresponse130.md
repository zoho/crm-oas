INVALID_DATA error for an invalid api_name field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].transitions[*].layout.api_name"
      },
      "status": "error"
    }
  ]
}
```

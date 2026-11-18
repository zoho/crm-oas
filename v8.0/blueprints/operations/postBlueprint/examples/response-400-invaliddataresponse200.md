Error response with code INVALID_DATA: Invalid data (Field: details)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "details",
        "maximum_length": 1,
        "json_path": "$.blueprints[*].transitions[*].actions[*].details"
      },
      "status": "error"
    }
  ]
}
```

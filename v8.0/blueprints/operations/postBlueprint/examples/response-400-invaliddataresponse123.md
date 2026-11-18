INVALID_DATA error for an invalid api_name value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 5,
        "json_path": "$.blueprints[*].transitions[*].module.api_name"
      },
      "status": "error"
    }
  ]
}
```

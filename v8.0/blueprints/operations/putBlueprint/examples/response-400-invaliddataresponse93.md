Error — invalid api_name value (INVALID_DATA)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].connections[*].to_state.api_name"
      },
      "status": "error"
    }
  ]
}
```

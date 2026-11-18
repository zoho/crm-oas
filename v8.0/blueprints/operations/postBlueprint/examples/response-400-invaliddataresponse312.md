Error response with code INVALID_DATA: Invalid data (Field: name)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].connections[*].transitions.name"
      },
      "status": "error"
    }
  ]
}
```

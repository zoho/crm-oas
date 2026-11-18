INVALID_DATA error for an invalid name field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].transitions[*].layout.name"
      },
      "status": "error"
    }
  ]
}
```

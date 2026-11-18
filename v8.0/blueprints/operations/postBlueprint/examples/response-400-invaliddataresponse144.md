INVALID_DATA error for invalid data in the type field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].transitions[*].owners[*].type"
      },
      "status": "error"
    }
  ]
}
```

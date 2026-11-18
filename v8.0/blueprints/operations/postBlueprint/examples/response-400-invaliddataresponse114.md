INVALID_DATA error for invalid data in the type field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 5,
        "json_path": "$.blueprints[*].transitions[*].criteria.type"
      },
      "status": "error"
    }
  ]
}
```

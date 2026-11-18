INVALID_DATA error for invalid data in the value field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 3,
        "json_path": "$.blueprints[*].transitions[*].criteria.value"
      },
      "status": "error"
    }
  ]
}
```

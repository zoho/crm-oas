INVALID_DATA error for invalid data in the ID field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.blueprints[*].transitions[*].criteria.field.id"
      },
      "status": "error"
    }
  ]
}
```

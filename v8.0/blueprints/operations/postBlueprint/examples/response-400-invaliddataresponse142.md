INVALID_DATA error for invalid data in the ID field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 30,
        "json_path": "$.blueprints[*].transitions[*].owners[*].resources[*].id"
      },
      "status": "error"
    }
  ]
}
```

INVALID_DATA error for an incorrect data type in the transition name

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].transitions[*].name"
      },
      "status": "error"
    }
  ]
}
```

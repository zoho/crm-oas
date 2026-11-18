INVALID_DATA error for invalid data in the trigger_type field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "trigger_type",
        "maximum_length": 10,
        "json_path": "$.blueprints[*].transitions[*].trigger_type"
      },
      "status": "error"
    }
  ]
}
```

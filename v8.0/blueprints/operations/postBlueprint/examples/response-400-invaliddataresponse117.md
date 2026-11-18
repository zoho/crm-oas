INVALID_DATA error for an incorrect data type in the trigger_type field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "trigger_type",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].transitions[*].trigger_type"
      },
      "status": "error"
    }
  ]
}
```

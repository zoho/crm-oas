INVALID_DATA error for an incorrect data type in the transition_type field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "transition_type",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].transitions[*].transition_type"
      },
      "status": "error"
    }
  ]
}
```

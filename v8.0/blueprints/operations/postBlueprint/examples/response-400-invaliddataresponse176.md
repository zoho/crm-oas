INVALID_DATA error for a non-integer during_inputs sequence value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "sequence",
        "expected_data_type": "integer",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].sequence"
      },
      "status": "error"
    }
  ]
}
```

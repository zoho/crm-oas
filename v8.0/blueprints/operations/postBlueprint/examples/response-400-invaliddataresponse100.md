INVALID_DATA error for an invalid data type in the transitions field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "transitions",
        "expected_data_type": "jsonarray",
        "json_path": "$.blueprints[*].transitions"
      },
      "status": "error"
    }
  ]
}
```

INVALID_DATA error for an incorrect data type in the value field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "bigint",
        "json_path": "$.blueprints[*].transitions[*].criteria.value"
      },
      "status": "error"
    }
  ]
}
```

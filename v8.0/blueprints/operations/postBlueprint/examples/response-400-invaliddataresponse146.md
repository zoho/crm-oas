INVALID_DATA error for an invalid data type in the common field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "common",
        "expected_data_type": "boolean",
        "json_path": "$.blueprints[*].transitions[*].common"
      },
      "status": "error"
    }
  ]
}
```

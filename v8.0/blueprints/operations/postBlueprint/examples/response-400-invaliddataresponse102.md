INVALID_DATA error for an invalid data type in the criteria field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "criteria",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].transitions[*].criteria"
      },
      "status": "error"
    }
  ]
}
```

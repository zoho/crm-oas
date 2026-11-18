INVALID_DATA error for an invalid data type in the resources field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "resources",
        "expected_data_type": "jsonarray",
        "json_path": "$.blueprints[*].transitions[*].owners[*].resources"
      },
      "status": "error"
    }
  ]
}
```

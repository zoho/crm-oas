INVALID_DATA error: invalid data type for the resources field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "resources",
        "expected_data_type": "jsonarray",
        "json_path": "$.blueprints[*].owners[*].resources"
      },
      "status": "error"
    }
  ]
}
```

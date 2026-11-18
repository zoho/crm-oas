INVALID_DATA error when the owners value has an incorrect data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "owners",
        "expected_data_type": "jsonarray",
        "json_path": "$.blueprints[*].owners"
      },
      "status": "error"
    }
  ]
}
```

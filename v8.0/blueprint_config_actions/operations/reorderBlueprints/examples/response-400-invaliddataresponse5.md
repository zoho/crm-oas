INVALID_DATA error when ID is not a bigint.


```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.blueprints[*].id"
      },
      "status": "error"
    }
  ]
}
```

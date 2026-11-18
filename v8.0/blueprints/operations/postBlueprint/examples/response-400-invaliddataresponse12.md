INVALID_DATA error for an invalid ID field type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.blueprints[*].owners[*].resources[*].id"
      },
      "status": "error"
    }
  ]
}
```

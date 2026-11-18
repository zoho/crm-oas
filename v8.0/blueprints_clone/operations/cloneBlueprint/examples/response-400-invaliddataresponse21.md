INVALID_DATA error for an invalid pipeline ID data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.blueprints[*].pipeline.id"
      },
      "status": "error"
    }
  ]
}
```

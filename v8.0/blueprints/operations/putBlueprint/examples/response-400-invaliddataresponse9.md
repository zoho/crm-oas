Error — invalid data type for resources (INVALID_DATA)

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

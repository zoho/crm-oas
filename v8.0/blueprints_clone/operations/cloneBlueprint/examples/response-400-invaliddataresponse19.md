INVALID_DATA error for an invalid pipeline object data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "pipeline",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].pipeline"
      },
      "status": "error"
    }
  ]
}
```

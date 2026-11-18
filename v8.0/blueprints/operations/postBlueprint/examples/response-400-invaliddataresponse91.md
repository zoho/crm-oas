INVALID_DATA error for a pipeline field with an invalid data type

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

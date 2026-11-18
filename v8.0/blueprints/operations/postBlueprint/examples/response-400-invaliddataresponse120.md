INVALID_DATA error for an invalid module field type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].transitions[*].module"
      },
      "status": "error"
    }
  ]
}
```

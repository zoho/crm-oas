INVALID_DATA error when the continuous value has an incorrect data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "continuous",
        "expected_data_type": "boolean",
        "json_path": "$.blueprints[*].continuous"
      },
      "status": "error"
    }
  ]
}
```

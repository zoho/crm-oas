INVALID_DATA error for an invalid data type in the api_name field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].transitions[*].layout.api_name"
      },
      "status": "error"
    }
  ]
}
```

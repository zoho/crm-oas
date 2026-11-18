INVALID_DATA error for a layout api_name value with an incorrect data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].layout.api_name"
      },
      "status": "error"
    }
  ]
}
```

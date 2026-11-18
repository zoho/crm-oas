INVALID_DATA error for an invalid field API name value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```

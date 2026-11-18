INVALID_DATA error for an api_name value exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].criteria.field.api_name"
      },
      "status": "error"
    }
  ]
}
```

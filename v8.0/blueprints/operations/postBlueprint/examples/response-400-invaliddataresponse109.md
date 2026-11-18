INVALID_DATA error for an invalid value in the api_name property

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].transitions[*].criteria.field.api_name"
      },
      "status": "error"
    }
  ]
}
```

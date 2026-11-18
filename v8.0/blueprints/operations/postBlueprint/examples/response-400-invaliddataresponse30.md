INVALID_DATA error for a criteria type value exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].criteria.type"
      },
      "status": "error"
    }
  ]
}
```

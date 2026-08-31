Validation error during single role update

```json
{
  "roles": [
    {
      "status": "error",
      "code": "INVALID_DATA",
      "message": "Invalid role name",
      "details": {
        "maximum_length": 200,
        "api_name": "name",
        "json_path": "$.roles[0].name"
      }
    }
  ]
}
```

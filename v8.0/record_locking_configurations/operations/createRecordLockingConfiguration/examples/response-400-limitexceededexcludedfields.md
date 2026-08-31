Exceeded maximum number of excluded fields

```json
{
  "record_locking_configurations": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 15,
        "available_limit": 2,
        "api_name": "excluded_fields",
        "json_path": "$.record_locking_configurations[0].excluded_fields"
      },
      "message": "Maximum limit for excluded fields exceeded",
      "status": "error"
    }
  ]
}
```

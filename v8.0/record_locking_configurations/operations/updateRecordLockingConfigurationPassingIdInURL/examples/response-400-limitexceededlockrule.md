Exceeded maximum number of locking rules

```json
{
  "record_locking_configurations": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 5,
        "available_limit": 2,
        "api_name": "locking_rules",
        "json_path": "$.record_locking_configurations[0].locking_rules"
      },
      "message": "Maximum limit for locking rules exceeded",
      "status": "error"
    }
  ]
}
```

Exceeded maximum number of excluded profiles

```json
{
  "record_locking_configurations": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 15,
        "available_limit": 2,
        "api_name": "lock_excluded_profiles",
        "json_path": "$.record_locking_configurations[0].lock_excluded_profiles"
      },
      "message": "Maximum limit for excluded profiles exceeded",
      "status": "error"
    }
  ]
}
```

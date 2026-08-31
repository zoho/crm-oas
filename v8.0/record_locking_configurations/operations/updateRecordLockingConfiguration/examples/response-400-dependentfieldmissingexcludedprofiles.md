Missing `lock_excluded_profiles` when `locked_for` is `all_profiles_except_excluded_profiles`

```json
{
  "record_locking_configurations": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "locked_for",
          "json_path": "$.record_locking_configurations[0].locked_for"
        },
        "api_name": "lock_excluded_profiles",
        "json_path": "$.record_locking_configurations[0].lock_excluded_profiles"
      },
      "message": "lock_excluded_profiles should have been given when locked_for is given as all_profiles_except_excluded_profiles ",
      "status": "error"
    }
  ]
}
```

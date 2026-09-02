Missing `locking_rules` when `lock_type` is `automatic` or `both`

```json
{
  "record_locking_configurations": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "lock_type",
          "json_path": "$.record_locking_configurations[0].lock_type"
        },
        "api_name": "locking_rules",
        "json_path": "$.record_locking_configurations[0].locking_rules"
      },
      "message": "locking_rules should have been given when lock_type is given as automatic or both",
      "status": "error"
    }
  ]
}
```

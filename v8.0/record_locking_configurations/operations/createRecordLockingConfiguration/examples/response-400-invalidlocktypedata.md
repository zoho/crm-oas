Invalid lock type value

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "supported_values": [
          "manual",
          "automatic",
          "both"
        ],
        "api_name": "lock_type",
        "json_path": "$.record_locking_configurations[0].lock_type"
      },
      "message": "lock_type not found",
      "status": "error"
    }
  ]
}
```

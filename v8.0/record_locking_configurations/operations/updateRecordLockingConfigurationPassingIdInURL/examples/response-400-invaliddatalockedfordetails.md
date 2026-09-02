Invalid `locked_for` value

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "supported_values": [
          "all_profiles",
          "all_profiles_except_excluded_profiles"
        ],
        "api_name": "locked_for",
        "json_path": "$.record_locking_configurations[0].locked_for"
      },
      "message": "locked_for not found",
      "status": "error"
    }
  ]
}
```

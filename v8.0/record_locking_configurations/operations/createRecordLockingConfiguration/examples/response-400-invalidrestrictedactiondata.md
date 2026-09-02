Invalid restricted action value

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "supported_values": [
          "convert",
          "update",
          "delete",
          "change_owner",
          "tags"
        ],
        "api_name": "restricted_actions",
        "json_path": "$.record_locking_configurations[0].restricted_actions[1]"
      },
      "message": "action not found",
      "status": "error"
    }
  ]
}
```

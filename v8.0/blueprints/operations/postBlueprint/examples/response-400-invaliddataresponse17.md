INVALID_DATA error for an unsupported Blueprint owner type value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "users",
          "role",
          "group",
          "record_owner",
          "portal_user_type"
        ],
        "json_path": "$.blueprints[*].owners[*].type"
      },
      "status": "error"
    }
  ]
}
```

INVALID_DATA error for invalid data in the type field

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
        "json_path": "$.blueprints[*].transitions[*].owners[*].type"
      },
      "status": "error"
    }
  ]
}
```

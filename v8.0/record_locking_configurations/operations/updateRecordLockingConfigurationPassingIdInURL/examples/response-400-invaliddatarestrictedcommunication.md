Invalid restricted communication value

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "supported_values": [
          "send_mail",
          "send_survey",
          "send_portal_invitation"
        ],
        "api_name": "restricted_communications",
        "json_path": "$.record_locking_configurations[0].restricted_communications[1]"
      },
      "message": "communications not found",
      "status": "error"
    }
  ]
}
```

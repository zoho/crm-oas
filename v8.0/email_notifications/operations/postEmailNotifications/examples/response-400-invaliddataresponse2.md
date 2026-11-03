INVALID_DATA error — unsupported value passed for associated_to field

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "associated_to",
        "json_path": "$.email_notifications[0].recipients.to[0].associated_to",
        "supported_values": [
          "team_module"
        ]
      },
      "message": "invalid associated_to passed",
      "status": "error"
    }
  ]
}
```

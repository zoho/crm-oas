INVALID_DATA error response for invalid associated_to field value

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

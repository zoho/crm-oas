INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "supported_values": [
          "${CURRENTUSER}"
        ],
        "json_path": "$.assignment_rules[*].default_assignee.api_name"
      },
      "status": "error"
    }
  ]
}
```

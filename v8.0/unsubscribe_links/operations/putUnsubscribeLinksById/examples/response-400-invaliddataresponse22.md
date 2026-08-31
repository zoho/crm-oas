INVALID_DATA error: unsupported submission_action_type value

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "submission_action_type",
        "supported_values": [
          "display_message",
          "redirect"
        ],
        "json_path": "$.unsubscribe_links[*].submission_action_type"
      },
      "status": "error"
    }
  ]
}
```

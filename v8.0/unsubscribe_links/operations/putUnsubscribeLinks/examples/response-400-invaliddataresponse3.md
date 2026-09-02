INVALID_DATA error: unsupported submission_action_type value - variant 1

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "submission_action_type",
        "json_path": "$.unsubscribe_links[0].submission_action_type",
        "supported_values": [
          "display_message",
          "redirect"
        ]
      },
      "message": "the given module is not supported in create or update",
      "status": "error"
    }
  ]
}
```

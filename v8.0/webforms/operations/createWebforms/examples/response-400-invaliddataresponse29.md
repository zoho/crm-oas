INVALID_DATA error for an unsupported module in create or update

```json
{
  "webforms": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "action_on_submit",
        "json_path": "$.webforms[0].action_on_submit",
        "supported_values": [
          "splash_message",
          "thank_you_message",
          "redirect_url"
        ]
      },
      "message": "the given module is not supported in create or update",
      "status": "error"
    }
  ]
}
```

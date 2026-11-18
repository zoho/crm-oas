Message configured on non-save button.

```json
{
  "wizards": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.wizards[0].containers[0].screens[0].segments[2].buttons[0].type"
        },
        "api_name": "message",
        "json_path": "$.wizards[0].containers[0].screens[0].segments[2].buttons[0].message"
      },
      "message": "Only save buttons can have acknowledgement message",
      "status": "error"
    }
  ]
}
```

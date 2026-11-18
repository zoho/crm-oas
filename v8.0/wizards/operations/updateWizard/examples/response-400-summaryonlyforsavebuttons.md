Summary configured on non-save button.

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
        "api_name": "show_summary_on",
        "json_path": "$.wizards[0].containers[0].screens[0].segments[2].buttons[0].show_summary_on"
      },
      "message": "Only save buttons can show summary",
      "status": "error"
    }
  ]
}
```

DEPENDENT_MISMATCH error when double opt-in conflicts with splash message action on submit

```json
{
  "webforms": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "action_on_submit",
          "json_path": "$.webforms[0].action_on_submit"
        },
        "api_name": "double_optin_enabled",
        "json_path": "$.webforms[0].double_optin_enabled"
      },
      "message": "double opt-in cannot be enabled when splash message is chosen as action on submit",
      "status": "error"
    }
  ]
}
```

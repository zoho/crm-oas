DEPENDENT_MISMATCH error for invalid dependent field data

```json
{
  "webforms": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "action_value",
          "json_path": "$.webforms[0].action_value"
        },
        "api_name": "action_on_submit",
        "json_path": "$.webforms[0].action_on_submit"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

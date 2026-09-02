Next shift specified without an effective-from date

```json
{
  "users": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "$next_shift",
          "json_path": "$.users[0].$next_shift"
        },
        "api_name": "$shift_effective_from",
        "json_path": "$.users[0].$shift_effective_from"
      },
      "message": "Dependent Field value should not be null",
      "status": "error"
    }
  ]
}
```

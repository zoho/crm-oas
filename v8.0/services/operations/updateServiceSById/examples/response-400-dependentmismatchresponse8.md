DEPENDENT_MISMATCH on Available_Till where To value must exceed Available_From.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Available_From",
          "json_path": "$.data[0].Available_From"
        },
        "api_name": "Available_Till",
        "json_path": "$.data[0].Available_Till"
      },
      "message": "To value must be Greater than From value",
      "status": "error"
    }
  ]
}
```

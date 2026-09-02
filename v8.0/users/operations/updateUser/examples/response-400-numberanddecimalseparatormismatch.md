Number and decimal separator cannot be the same

```json
{
  "users": [
    {
      "code": "MAPPING_MISMATCH",
      "details": {
        "mapped_field": {
          "api_name": "number_separator",
          "json_path": "$.users[0].number_separator"
        },
        "api_name": "decimal_separator",
        "json_path": "$.users[0].decimal_separator"
      },
      "message": "the number separator and decimal separator values should not be same",
      "status": "error"
    }
  ]
}
```

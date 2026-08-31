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
  ],
  "description": "Shows the error returned when the number separator and decimal separator values submitted in the request are identical.",
  "summary": "Number separator and decimal separator values are identical"
}
```

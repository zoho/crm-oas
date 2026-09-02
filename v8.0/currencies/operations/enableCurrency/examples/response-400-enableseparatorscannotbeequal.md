Thousand and decimal separator cannot be equal

```json
{
  "base_currency": {
    "code": "NOT_ALLOWED",
    "message": "Thousand separator and Decimal separator should not be equal",
    "status": "error",
    "details": {
      "api_name": "decimal_places",
      "json_path": "$.base_currency.format.decimal_places"
    }
  }
}
```

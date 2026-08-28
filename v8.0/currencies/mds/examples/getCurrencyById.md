# Examples: getCurrencyById

**GET /org/currencies/{currency}**

## Response examples

### Status `200` — `application/json` — GetByIdSample

Single currency response

```json
{
  "currencies": [
    {
      "prefix_symbol": true,
      "format": {
        "numeral_system": "International",
        "decimal_places": "2",
        "decimal_separator": "Period",
        "thousand_separator": "Comma"
      },
      "exchange_rate": "85.000000000",
      "is_active": true,
      "exchange_rate_auto_update": true,
      "iso_code": "INR",
      "symbol": "₹",
      "name": "Indian Rupee - INR",
      "is_base": false,
      "id": "3652397000007472080",
      "created_by": {
        "name": "Admin",
        "id": "11111300000001"
      },
      "modified_by": {
        "name": "Admin",
        "id": "11111300000001"
      },
      "modified_time": "2025-01-01T00:00:00Z",
      "created_time": "2025-01-01T00:00:00Z",
      "exchange_rate_updated_time": "2019-05-31T15:10:33+05:30"
    }
  ]
}
```

### Status `403` — `application/json` — CurrenciesNotEnabled

Multi-currency is not enabled

```json
{
  "code": "CURRENCIES_NOT_ENABLED",
  "details": {},
  "message": "Multi currency is not enabled",
  "status": "error"
}
```

# Examples: getCurrencies

**GET /org/currencies**

## Response examples

### Status `200` — `application/json` — Sample

Sample list response

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
      "exchange_rate": "1.000000000",
      "is_active": true,
      "exchange_rate_auto_update": true,
      "iso_code": "USD",
      "symbol": "$",
      "name": "US Dollar - USD",
      "is_base": true,
      "id": "111113000000038990",
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

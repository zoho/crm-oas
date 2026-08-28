# Examples: updateCurrencies

**PUT /org/currencies**

## Request examples

### `application/json` — UpdateSample

Update one currency

```json
{
  "currencies": [
    {
      "id": "3652397000007472080",
      "symbol": "$",
      "is_active": false,
      "exchange_rate": "85.000000000",
      "exchange_rate_auto_update": true
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — UpdateSuccess

Update success example

```json
{
  "currencies": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000129300"
      },
      "message": "The currency updated successfully.",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — MultiStatusExample

Mixed update results

```json
{
  "currencies": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000129300"
      },
      "message": "The currency updated successfully.",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "exchange_rate",
        "json_path": "$.currencies[1].exchange_rate"
      },
      "message": "Exchange rate given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NoPermission

User lacks required permissions

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Currencies"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```

### Status `400` — `application/json` — ActiveCurrencyLimitExceeded

Maximum allowed active currencies reached

```json
{
  "currencies": [
    {
      "code": "ACTIVE_STATE_LIMIT_EXCEEDED",
      "details": {
        "limit": 5
      },
      "message": "Allowed active currency limit reached. Please deactivate any one of the existing active currencies to create this currency.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidISO

Invalid ISO code

```json
{
  "currencies": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "iso_code",
        "json_path": "$.currencies[0].iso_code"
      },
      "message": "Currency isocode given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidSymbol

Invalid currency symbol

```json
{
  "currencies": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "symbol",
        "json_path": "$.currencies[0].symbol"
      },
      "message": "Currency symbol given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SymbolAlreadyUsed

Symbol already assigned

```json
{
  "currencies": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "symbol",
        "json_path": "$.currencies[0].symbol"
      },
      "message": "Currency symbol is already used",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidThousandSeparator

Wrong thousand separator

```json
{
  "currencies": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "thousand_separator",
        "json_path": "$.currencies[0].format.thousand_separator"
      },
      "message": "Thousand separator given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDecimalSeparator

Wrong decimal separator

```json
{
  "currencies": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "decimal_separator",
        "json_path": "$.currencies[0].format.decimal_separator"
      },
      "message": "Decimal separator given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDecimalPlaces

Wrong decimal places

```json
{
  "currencies": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "decimal_places",
        "json_path": "$.currencies[0].format.decimal_places"
      },
      "message": "Decimal places given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidNumeralSystem

Invalid numeral system

```json
{
  "currencies": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "numeral_system",
        "json_path": "$.currencies[0].format.numeral_system"
      },
      "message": "Numeral system given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedSameSeparators

Thousand and decimal separator conflict

```json
{
  "currencies": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "decimal_places",
        "json_path": "$.currencies[0].format.decimal_places"
      },
      "message": "Thousand separator and Decimal separator should not be equal",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — IndianFormatSeparatorRules

Indian numeral system separator restrictions

```json
{
  "currencies": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "numeral_system",
        "json_path": "$.currencies[0].format.numeral_system"
      },
      "message": "The only supported thousand and decimal separators in the Indian numeral system are the comma and the period",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidExchangeRateType

Exchange rate invalid datatype

```json
{
  "currencies": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "string",
        "api_name": "exchange_rate",
        "json_path": "$.currencies[0].exchange_rate"
      },
      "message": "Exchange rate given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidExchangeRateAutoUpdate

Invalid exchange rate auto update

```json
{
  "currencies": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "boolean",
        "api_name": "exchange_rate_auto_update",
        "json_path": "$.currencies[0].exchange_rate_auto_update"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

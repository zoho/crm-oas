# Examples: enableCurrency

**POST /org/currencies/actions/enable**

## Request examples

### `application/json` — EnableSample

Enable multi-currency sample

```json
{
  "base_currency": {
    "format": {
      "decimal_separator": "Period",
      "thousand_separator": "Comma",
      "decimal_places": "2",
      "numeral_system": "International"
    },
    "name": "Algerian Dinar - DZD",
    "iso_code": "DZD",
    "symbol": "DA",
    "exchange_rate": "1.000000000"
  }
}
```

## Response examples

### Status `200` — `application/json` — EnableSuccess

Enable success example

```json
{
  "base_currency": {
    "code": "SUCCESS",
    "details": {
      "id": "111113000000038990"
    },
    "message": "The multi-currency feature is enabled and given currency is created as the base currency.",
    "status": "success"
  }
}
```

### Status `400` — `application/json` — EnableAlreadyEnabled

Multi-currency already enabled

```json
{
  "base_currency": {
    "code": "ALREADY_ENABLED",
    "message": "The base currency is already added",
    "status": "error",
    "details": {}
  }
}
```

### Status `400` — `application/json` — EnableNoPermission

No permission to enable multi-currency

```json
{
  "code": "NO_PERMISSION",
  "message": "Permission denied",
  "status": "error",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Currencies"
    ]
  }
}
```

### Status `400` — `application/json` — EnableInvalidISOCode

Invalid currency iso code

```json
{
  "base_currency": {
    "code": "INVALID_DATA",
    "message": "Currency isocode given seems to be invalid",
    "status": "error",
    "details": {
      "api_name": "iso_code",
      "json_path": "$.base_currency.iso_code"
    }
  }
}
```

### Status `400` — `application/json` — EnableInvalidExchangeRate

Invalid exchange rate

```json
{
  "base_currency": {
    "code": "INVALID_DATA",
    "message": "Exchange rate given seems to be invalid",
    "status": "error",
    "details": {
      "api_name": "exchange_rate",
      "json_path": "$.base_currency.exchange_rate",
      "maximum_decimal_place": 9
    }
  }
}
```

### Status `400` — `application/json` — EnableInvalidSymbol

Invalid currency symbol

```json
{
  "base_currency": {
    "code": "INVALID_DATA",
    "message": "Currency symbol given seems to be invalid",
    "status": "error",
    "details": {
      "api_name": "symbol",
      "json_path": "$.base_currency.symbol"
    }
  }
}
```

### Status `400` — `application/json` — EnableInvalidName

Invalid currency name

```json
{
  "base_currency": {
    "code": "INVALID_DATA",
    "message": "Currency name given seems to be invalid",
    "status": "error",
    "details": {
      "api_name": "name",
      "json_path": "$.base_currency.name"
    }
  }
}
```

### Status `400` — `application/json` — EnableInvalidThousandSeparator

Invalid thousand separator

```json
{
  "base_currency": {
    "code": "INVALID_DATA",
    "message": "Thousand separator given seems to be invalid",
    "status": "error",
    "details": {
      "api_name": "thousand_separator",
      "json_path": "$.base_currency.format.thousand_separator"
    }
  }
}
```

### Status `400` — `application/json` — EnableInvalidDecimalSeparator

Invalid decimal separator

```json
{
  "base_currency": {
    "code": "INVALID_DATA",
    "message": "Decimal separator given seems to be invalid",
    "status": "error",
    "details": {
      "api_name": "decimal_separator",
      "json_path": "$.base_currency.format.decimal_separator"
    }
  }
}
```

### Status `400` — `application/json` — EnableInvalidDecimalPlaces

Invalid decimal places

```json
{
  "base_currency": {
    "code": "INVALID_DATA",
    "message": "Decimal places given seems to be invalid",
    "status": "error",
    "details": {
      "api_name": "decimal_places",
      "json_path": "$.base_currency.format.decimal_places"
    }
  }
}
```

### Status `400` — `application/json` — EnableInvalidNumeralSystem

Invalid numeral system

```json
{
  "base_currency": {
    "code": "INVALID_DATA",
    "message": "Numeral system given seems to be invalid",
    "status": "error",
    "details": {
      "api_name": "numeral_system",
      "json_path": "$.base_currency.format.numeral_system"
    }
  }
}
```

### Status `400` — `application/json` — EnableIndianNumberFormatViolation

Indian numeral system separator rule violation

```json
{
  "base_currency": {
    "code": "INVALID_DATA",
    "message": "The only supported thousand and decimal separators in the Indian numeral system are the comma and the period",
    "status": "error",
    "details": {
      "api_name": "numeral_system",
      "json_path": "$.base_currency.format.numeral_system"
    }
  }
}
```

### Status `400` — `application/json` — EnableSeparatorsCannotBeEqual

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

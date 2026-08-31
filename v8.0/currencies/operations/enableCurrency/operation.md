# POST /org/currencies/actions/enable
**Operation:** `enableCurrency` — Enable multi-currency
> Enable multi-currency for the organization and set the base currency.

**Request Body** (required) — application/json
> Specifies the request payload structure for this operation.
  > Payload for creating and enabling base currency.
  - `base_currency` (object) **REQ** — Represents the base currency information required for initializing multi-currency settings in the CRM.
    - `prefix_symbol` (boolean) — Represents the position of the currency symbol.
**Possible Values:**
**true** - Display the currency symbol before the currency value. This is the default value.
**false** - Display the currency symbol after the currency value.
    - `iso_code` (string) **REQ** [maxLen=3] — Represents the ISO code of the currency. You can get the currency code from the CRM UI at **Setup > General > Company Settings > Currencies.**
    - `symbol` (string) [maxLen=50] — Represents the symbol of the currency.
    - `exchange_rate` (string) **REQ** [maxLen=50, pattern=^[0-9]{1,9}(\.[0-9]{1,9})?$] — Represents the rate at which the currency has to be exchanged with home currency. Accepts positive decimal numbers up to **nine** digits and nine decimal places. Example: 123456789.123456789.
    - `format` (object) — Represents the format of the base currency with details like decimal_separator, thousand_separator, and decimal_places.
      - `numeral_system` (string) [enum=['Indian', 'International'], default=International] — Indicates whether the currency should use the Indian or International numbering format.
      - `decimal_places` (string) [enum=['0', '2', '3', '4', '5', '6']] — Represents the number of decimal places allowed for the currency. It can be **0, 2, and 3.**
      - `decimal_separator` (string) [enum=['Comma', 'Period']] — The decimal separator separates the integer part of the currency from its fractional part. It can be a Period or Comma, depending on the currency.
      - `thousand_separator` (string) [enum=['Comma', 'Period', 'Space']] — The thousand separator separates groups of thousands in a currency. It can be a Period, Comma, or Space, depending on the currency.
    - `name` (string) [maxLen=255] — Full name of the currency (for example, US Dollar - USD).

**Responses:**

- **200**: Successfully enabled and created base currency. [application/json]
    > Successful enable response
    - `base_currency` (object) **REQ** — Success response object.
      - `code` (string) **REQ** [maxLen=50] — Result code, for example, SUCCESS.
      - `details` (object) **REQ** — Additional response details.
        - `id` (string/int64) [maxLen=255] — ID of the created base currency.
      - `message` (string) **REQ** [maxLen=255] — Success message for the operation result.
      - `status` (string) **REQ** [maxLen=50] — Operation status, for example, success.

- **400**: Invalid request or validation errors. [application/json]
    > Possible error responses for multi-currency enablement.
    oneOf:
        - `code` (string) **REQ** [maxLen=100, enum=['NO_PERMISSION']] — Error code indicating no permission.
        - `message` (string) **REQ** [maxLen=255] — Descriptive error message.
        - `status` (string) **REQ** [maxLen=20, enum=['error']] — Indicates error status.
        - `details` (object) **REQ** — Permission error details.
          - `permissions` (array of string) [maxItems=100] — List of missing permissions.
            items: [maxLen=100]
        - `base_currency` (object) **REQ** — base_currency-level error object for currency-specific validation errors.
          - `code` (string) **REQ** [maxLen=100, enum=['ALREADY_ENABLED', 'INVALID_DATA', 'MANDATORY_NOT_FOUND', 'NOT_ALLOWED']] — Error code for base_currency validation.
          - `message` (string) **REQ** [maxLen=255] — Error message for the base currency validation result.
          - `status` (string) **REQ** [maxLen=20, enum=['error']] — Status for the base_currency error.
          - `details` (object) **REQ** — Additional details for base_currency error (field name, JSON path).
            - `api_name` (string) [maxLen=255] — Field or API parameter related to the error.
            - `json_path` (string) [maxLen=255] — JSON path pointing to the error field.
            - `maximum_decimal_place` (integer/int32) [max=9] — Maximum allowed decimal places for the field, returned when the value exceeds the limit.

**Scopes:** ZohoCRM.settings.currencies.CREATE

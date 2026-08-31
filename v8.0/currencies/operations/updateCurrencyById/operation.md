# PUT /org/currencies/{currency}
**Operation:** `updateCurrencyById` — Currency
> Update a specific currency by its unique ID.

**Parameters:**
- `currency` (path, string, required) [maxLen=255]: Path parameter identifying the currency ID.

**Request Body** (required) — application/json
> Specifies the request payload structure for this operation.
  > Payload for updating a specific currency by ID.
  - `currencies` (array of object) [maxItems=100] **REQ** — List of currencies to update (single-element array expected).
    - `format` (object) — Configuration for currency formatting rules.
      - `numeral_system` (string) [enum=['Indian', 'International'], default=International] — Defines the numbering system used for digit grouping.
      - `decimal_places` (string) [enum=['0', '2', '3', '4', '5', '6']] — 
Represents the number of decimal places allowed for the currency. It can be **0, 2, and 3.**
      - `decimal_separator` (string) [enum=['Comma', 'Period']] — The decimal separator separates the integer part of the currency from its fractional part. It can be a **Period or Comma,** depending on the currency.
      - `thousand_separator` (string) [enum=['Comma', 'Period', 'Space']] — The thousand separator separates groups of thousands in a currency. It can be a **Period**, **Comma**, or **Space**, depending on the currency.
    - `exchange_rate` (string) [maxLen=18, pattern=^[0-9]{1,9}(\.[0-9]{1,9})?$] — Represents the rate at which the currency has to be exchanged with home currency. Accepts positive decimal numbers up to **nine** digits and nine decimal places. Example: 123456789.123456789.
    - `is_active` (boolean) — Indicates whether the currency is active and available for use.
    - `exchange_rate_auto_update` (boolean) — Indicates whether the currency has the automated exchange rate option enabled or not.

**Responses:**

- **200**: Successfully updated the specified currency record(s). [application/json]
    > Response object containing updated currency data.
    - `currencies` (array of object) [maxItems=100] **REQ** — List of updated currency responses.
      - `code` (string) **REQ** [maxLen=255] — Specifies the response code
      - `message` (string) **REQ** [maxLen=255] — Indicates the response message.
      - `details` (object) **REQ** — Detailed information about the currency update
        - `id` (string/int64) **REQ** [maxLen=50] — The unique identifier of the currency.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the response.

- **400**: Bad request. The input contains malformed or invalid values. [application/json]
    > Possible error responses for currency update operation.
    oneOf:
        - `code` (string) **REQ** [maxLen=100, enum=['NO_PERMISSION', 'INVALID_DATA']] — Error identifier representing the failure type.
        - `message` (string) **REQ** [maxLen=255] — Specify the error message describing the error condition.
        - `details` (object) **REQ** — Specifies the additional information about the error.
          - `permissions` (array of string) [maxItems=100] — List of required permissions missing for the current user.
            items: [maxLen=100]
          additionalProperties: any
        - `status` (string) **REQ** [maxLen=20, enum=['error']] — Indicates that the response represents an error condition.
        - `currencies` (array of object) [maxItems=100] **REQ** — Array of currency error objects representing individual validation or permission errors.
          - `code` (string) **REQ** [maxLen=100, enum=['INVALID_DATA', 'ACTIVE_STATE_LIMIT_EXCEEDED', 'NOT_ALLOWED']] — Error identifier representing the validation failure type.
          - `message` (string) **REQ** [maxLen=255] — Specify the error message describing the error condition.
          - `details` (object) **REQ** — Additional debugging metadata for the error. Provides field-level or permission-level details.
            - `api_name` (string) [maxLen=255] — The field name, API parameter, or array index related to the error.
            - `json_path` (string) [maxLen=255] — JSON path pointing to the field that caused the error.
            - `limit` (integer/int32) — Maximum allowed limit relevant to the error, for example, max active currencies.
            - `expected_data_type` (string) [maxLen=50] — Expected data type for the invalid field.
            additionalProperties: any
          - `status` (string) **REQ** [maxLen=20, enum=['error']] — Indicates that the response represents an error condition.

- **404**: Not Found. The URL pattern is invalid, typically when a non-numeric identifier is used where a numeric ID is expected. [application/json]
    > Error response when the URL pattern does not match expected format.
    - `code` (string) **REQ** [maxLen=255, enum=['INVALID_URL_PATTERN']] — Error code identifying the type of error.
    - `details` (object) **REQ** — Additional error details.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `status` (string) **REQ** [maxLen=255, enum=['error']] — Error status.

**Scopes:** ZohoCRM.settings.currencies.UPDATE

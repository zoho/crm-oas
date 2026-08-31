# PUT /org/currencies
**Operation:** `updateCurrencies` — Update currencies
> Updates one or more currencies other than the base currency.

**Request Body** (required) — application/json
> Specifies the request payload structure for this operation.
  > Request body to update currency values in the organization.
  - `currencies` (array of object) [maxItems=100] **REQ** — List of currencies to be updated.
    - `id` (string/int64) **REQ** [maxLen=255] — Unique ID of the currency to update. Obtainable from GET /org/currencies.
    - `format` (object) — Currency formatting properties.
      - `numeral_system` (string) [enum=['Indian', 'International'], default=International] — Specifies whether the currency uses the Indian numbering format (1,00,000) or International format (100,000).
      - `decimal_places` (string) [enum=['0', '2', '3', '4', '5', '6']] — Represents the number of decimal places allowed for the currency. It can be **0, 2, and 3.**
      - `decimal_separator` (string) [enum=['Comma', 'Period']] — The decimal separator separates the integer part of the currency from its fractional part. It can be a **Period or Comma,** depending on the currency.
      - `thousand_separator` (string) [maxLen=255, enum=['Comma', 'Period', 'Space']] — The thousand separator separates groups of thousands in a currency. It can be a **Period**, **Comma**, or **Space**, depending on the currency.
    - `exchange_rate` (string) [maxLen=18, pattern=^[0-9]{1,9}(\.[0-9]{1,9})?$] — Represents the rate at which the currency has to be exchanged with home currency. Accepts positive decimal numbers up to **nine** digits and nine decimal places. Example: 123456789.123456789.
    - `is_active` (boolean) — Indicates whether the currency is active in the organization.
    - `exchange_rate_auto_update` (boolean) — Indicates whether the currency has the automated exchange rate option enabled or not.
    - `iso_code` (string) [maxLen=3] — ISO code of the currency. NOTE: During update, ISO code cannot be modified.
    - `symbol` (string) [maxLen=50] — Symbol used to display the currency
    - `name` (string) [maxLen=255] — Name of the currency. NOTE: During update, currency name cannot be modified.

**Responses:**

- **200**: Successfully updated the currency properties. [application/json]
    > Response returned for a successful update operation.
    - `currencies` (array of object) [maxItems=100] **REQ** — List of updated currency responses.
      - `code` (string) **REQ** [maxLen=50] — Specifies the response code.
      - `message` (string) **REQ** [maxLen=255] — Indicates the response message
      - `details` (object) **REQ** — Additional response details
        - `id` (string/int64) **REQ** [maxLen=50] — The unique identifier of the currency.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation.

- **207**: Multi-status. Returned when bulk currency update has a mix of successes and failures. [application/json]
    > Bulk update response containing mixed success and error results.
    - `currencies` (array of object) [maxItems=100] **REQ** — List of per-item results; each entry reflects one submitted currency.
      oneOf:
          - `code` (string) **REQ** [enum=['SUCCESS']] — SUCCESS code for this item.
          - `message` (string) **REQ** [maxLen=255] — Result message for this item.
          - `details` (object) **REQ** — Contains the updated currency identifier.
            - `id` (string/int64) **REQ** [maxLen=50] — Unique identifier of the updated currency.
          - `status` (string) **REQ** [enum=['success']] — Outcome of this item.
          - `code` (string) **REQ** [maxLen=100] — Error code for this item.
          - `message` (string) **REQ** [maxLen=255] — Result message for this item.
          - `details` (object) **REQ** — Additional details for this error item.
            - `api_name` (string) [maxLen=255] — Field or API parameter related to the error.
            - `json_path` (string) [maxLen=255] — JSON path pointing to the error field.
            - `expected_data_type` (string) [maxLen=50] — Expected data type for the invalid field.
            - `limit` (number) — Maximum allowed count relevant to the error.
          - `status` (string) **REQ** [enum=['error']] — Outcome of this item.

- **400**: Bad request. Input validation errors or disallowed update field. [application/json]
    > Possible error responses for currency update operation.
    oneOf:
        - `code` (string) **REQ** [maxLen=100, enum=['NO_PERMISSION']] — Error identifier representing the failure type.
        - `message` (string) **REQ** [maxLen=255] — Message describing the error condition.
        - `details` (object) **REQ** — Additional information about the error.
          - `permissions` (array of string) [maxItems=100] — List of required permissions missing for the current user.
            items: [maxLen=100]
        - `status` (string) **REQ** [maxLen=20, enum=['error']] — Indicates that the response represents an error condition.
        - `currencies` (array of object) [maxItems=100] **REQ** — Array of currency error objects representing individual validation or permission errors.
          - `code` (string) **REQ** [maxLen=100, enum=[4 values]] — Error identifier representing the validation failure type.
          - `message` (string) **REQ** [maxLen=255] — Message describing the error condition.
          - `details` (object) **REQ** — Additional debugging metadata for the error. Provides field-level or permission-level details.
            - `api_name` (string) [maxLen=255] — The field name, API parameter, or array index related to the error.
            - `json_path` (string) [maxLen=255] — JSON path pointing to the field that caused the error.
            - `limit` (integer/int32) — Maximum allowed limit relevant to the error, for example, max active currencies.
            - `expected_data_type` (string) [maxLen=50] — Expected data type for the invalid field.
            - `maximum_decimal_place` (number/int32) — Maximum allowed decimal places for currency values.
          - `status` (string) **REQ** [enum=['error']] — Indicates that the response represents an error condition.

**Scopes:** ZohoCRM.settings.currencies.UPDATE

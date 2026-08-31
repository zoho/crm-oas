# PUT /org/currencies/actions/enable
**Operation:** `updateBaseCurrency` — Update base currency
> Update existing base currency details.

**Request Body** (required) — application/json
> Specifies the request payload structure for this operation.
  > Payload for modifying existing base currency.
  - `base_currency` (object) **REQ** — JSON object containing the updated base currency values.
    - `iso_code` (string) [maxLen=3] — Represents the ISO code of the currency. You can get the currency code from the CRM UI at **Setup > General > Company Settings > Currencies.**
    - `symbol` (string) [maxLen=50] — Represents the symbol of the currency.
    - `exchange_rate` (string) [maxLen=50, pattern=^[0-9]{1,9}(\.[0-9]{1,9})?$] — Represents the rate at which the currency has to be exchanged with home currency. Accepts positive decimal numbers up to nine digits and nine decimal places. Example: 123456789.123456789.
    - `format` (object) — Represents the format of the base currency with details like decimal_separator, thousand_separator, and decimal_places.
      - `numeral_system` (string) [enum=['Indian', 'International'], default=International] — Numbering system used for grouping digits.
      - `decimal_places` (string) [enum=['0', '2', '3', '4', '5', '6']] — Represents the number of decimal places allowed for the currency. It can be **0, 2, and 3**.
      - `decimal_separator` (string) [enum=['Comma', 'Period']] — The decimal separator separates the integer part of the currency from its fractional part. It can be a **Period or Comma,** depending on the currency.
      - `thousand_separator` (string) [maxLen=255, enum=['Comma', 'Period', 'Space']] — The thousand separator separates groups of thousands in a currency. It can be a **Period**, **Comma**, or **Space**, depending on the currency.
    - `name` (string) [maxLen=255] — Represents the name of the currency. You can get the available currencies from the CRM UI at **Setup > General > Company Settings > Currencies.**
    - `id` (string/int64) **REQ** [maxLen=255] — The unique identifier of the currency.

**Responses:**

- **200**: Currency updated successfully. [application/json]
    > Successful update response
    - `base_currency` (object) **REQ** — Result of base currency update
      - `code` (string) **REQ** [maxLen=50] — Indicating the code of the result.
      - `message` (string) **REQ** [maxLen=255] — Message describing the operation result.
      - `status` (string) **REQ** [maxLen=50] — Represents the status of the operation.
      - `details` (object) **REQ** — Additional details of the response.
        - `id` (string/int64) [maxLen=255] — The unique identifier of the base currency created.

- **400**: Invalid request or validation errors. [application/json]
    > Possible error responses for update base currency operation.
    oneOf:
        - `code` (string) **REQ** [maxLen=100, enum=['NO_PERMISSION']] — Error code indicating no permission.
        - `message` (string) **REQ** [maxLen=255] — Descriptive error message.
        - `status` (string) **REQ** [maxLen=20, enum=['error']] — Indicates error status.
        - `details` (object) **REQ** — Permission error details.
          - `permissions` (array of string) [maxItems=100] — List of missing permissions.
            items: [maxLen=100]
        - `base_currency` (object) **REQ** — base_currency-level error object for currency-specific validation errors.
          - `code` (string) **REQ** [maxLen=100, enum=[5 values]] — Error code for base_currency validation.
          - `message` (string) **REQ** [maxLen=255] — Error message for the base currency validation result.
          - `status` (string) **REQ** [maxLen=20, enum=['error']] — Status for the base_currency error.
          - `details` (object) **REQ** — Specifies the additional details for base_currency error (field name, JSON path, or ambiguity details).
            - `api_name` (string) [maxLen=255] — Field or API parameter related to the error.
            - `json_path` (string) [maxLen=255] — A JSON pointer specifying the exact path to the property that failed validation.
            - `ambiguity_due_to` (array of object) [maxItems=100] — List of conflicting identifiers when both id and rid are provided but refer to different currencies.
              - `api_name` (string) [maxLen=255] — The conflicting field name.
              - `json_path` (string) [maxLen=255] — JSON path to the conflicting field.

**Scopes:** ZohoCRM.settings.currencies.UPDATE

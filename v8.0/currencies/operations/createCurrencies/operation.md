# POST /org/currencies
**Operation:** `createCurrencies` — Create currencies
> Creates one or more new currencies for the organization.

**Request Body** (required) — application/json
> Specifies the request payload structure for this operation.
  > Request object containing a list of currencies to create.
  - `currencies` (array of object) [maxItems=180] **REQ** — List of currencies to add to the organization. Supports up to 180 currencies per request.
    - `format` (object) — Represents the format of the base currency with details like decimal_separator, thousand_separator, and decimal_places.
      - `numeral_system` (string) [enum=['Indian', 'International'], default=International] — Numbering system used for grouping digits.
      - `decimal_places` (string) [enum=['0', '2', '3', '4', '5', '6']] — 
Represents the number of decimal places allowed for the currency. It can be **0, 2, and 3.**
      - `decimal_separator` (string) [enum=['Comma', 'Period']] — The decimal separator separates the integer part of the currency from its fractional part. It can be a **Period** or **Comma**, depending on the currency.
      - `thousand_separator` (string) [enum=['Comma', 'Period', 'Space']] — The thousand separator separates groups of thousands in a currency. It can be a **Period**, **Comma**, or **Space**, depending on the currency.
    - `exchange_rate` (string) **REQ** [maxLen=18, pattern=^[0-9]{1,9}(\.[0-9]{1,9})?$] — Represents the rate at which the currency has to be exchanged with home currency. Accepts positive decimal numbers up to **nine** digits and nine decimal places. Example: 123456789.123456789.
    - `is_active` (boolean) — Indicates whether the currency is active.
**Possible Values:**
**true** - The currency is active. This is the default value.
**false** - The currency is inactive.
    - `exchange_rate_auto_update` (boolean) — Indicates whether the currency has the automated exchange rate option enabled or not.
    - `iso_code` (string) **REQ** [maxLen=3] — Represents the ISO code of the currency. You can get the currency code from the CRM UI at **Setup > General > Company Settings > Currencies.**
    - `symbol` (string) [maxLen=50] — Indicates the currency symbol used for display.
    - `name` (string) [maxLen=255] — Represents the name of the currency. You can get the available currencies from the CRM UI at **Setup > General > Company Settings > Currencies.**

**Responses:**

- **200**: Currencies successfully created. [application/json]
    > Successful creation response wrapper.
    - `currencies` (array of object) [maxItems=180] **REQ** — List of results for each currency creation attempt. Returns one entry per submitted currency.
      - `code` (string) **REQ** [enum=['SUCCESS']] — The code representing success
      - `message` (string) **REQ** [maxLen=255] — Success message for the operation result.
      - `details` (object) **REQ** — Contains currency identifier.
        - `id` (string/int64) **REQ** [maxLen=50] — The unique identifier for currency.
      - `status` (string) **REQ** [enum=['success']] — Indicates the status of the operation.

- **207**: Multi-status. Returned when bulk currency creation has a mix of successes and failures. Each entry in the response array carries its own code and status. [application/json]
    > Bulk create response containing mixed success and error results.
    - `currencies` (array of object) [maxItems=180] **REQ** — List of per-item results; each entry reflects one submitted currency.
      oneOf:
          - `code` (string) **REQ** [enum=['SUCCESS']] — SUCCESS code for this item.
          - `message` (string) **REQ** [maxLen=255] — Result message for this item.
          - `details` (object) **REQ** — Contains the created currency identifier.
            - `id` (string/int64) **REQ** [maxLen=50] — Unique identifier of the newly created currency.
          - `status` (string) **REQ** [enum=['success']] — Outcome of this item.
          - `code` (string) **REQ** [maxLen=100] — Error code for this item.
          - `message` (string) **REQ** [maxLen=255] — Result message for this item.
          - `details` (object) **REQ** — Additional details for this error item.
            - `api_name` (string) [maxLen=255] — Field or API parameter related to the error.
            - `json_path` (string) [maxLen=255] — JSON path pointing to the error field.
            - `expected_data_type` (string) [maxLen=50] — Expected data type for the invalid field.
            - `limit` (number) — Maximum allowed count relevant to the error.
          - `status` (string) **REQ** [enum=['error']] — Outcome of this item.

- **400**: Bad request. The input data is invalid or missing required values. [application/json]
    > Possible error responses for currency creation operation.
    oneOf:
        - `code` (string) **REQ** [maxLen=100, enum=['NO_PERMISSION']] — Indicates the error code which implies the type of error.
        - `message` (string) **REQ** [maxLen=255] — Error message describing the failure.
        - `details` (object) **REQ** — Additional information related to permission error.
          - `permissions` (array of string) [maxItems=100] — List of required permissions that were missing.
            items: [maxLen=255]
        - `status` (string) **REQ** [maxLen=20, enum=['error']] — Represents the status of the response.
**Possible values:**
**error**
        - `currencies` (array of object) [maxItems=100] **REQ** — An array of currency errors returned when bulk operations fail, including details of each failure.
          - `code` (string) **REQ** [maxLen=100] — An error code representing the category or type of error returned.
          - `message` (string) **REQ** [maxLen=255] — Error message describing the failure.
          - `details` (object) **REQ** — Additional information related to validation error.
            - `api_name` (string) [maxLen=255] — Indicates the name of the parameter causing validation error.
            - `json_path` (string) [maxLen=255] — A JSON pointer specifying the exact path to the property that failed validation.
            - `expected_data_type` (string) [maxLen=50] — Required datatype for the field when applicable.
            - `limit` (number) — Specifies the maximum allowed count of active currencies.
            additionalProperties: any
          - `status` (string) **REQ** [maxLen=20, enum=['error']] — Indicate the status of the response.

**Scopes:** ZohoCRM.settings.currencies.CREATE

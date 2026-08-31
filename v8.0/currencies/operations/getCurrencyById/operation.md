# GET /org/currencies/{currency}
**Operation:** `getCurrencyById` — Specific Currency
> Retrieves details of a specific currency via its unique currency ID.

**Parameters:**
- `currency` (path, string, required) [maxLen=255]: Unique identifier of the currency to retrieve.

**Responses:**

- **200**: Successfully retrieved the currency details. [application/json]
    > Currency response object.
    - `currencies` (array of object) [maxItems=1] **REQ** — JSON array containing the requested currency object.
      - `prefix_symbol` (boolean) **REQ** — Represents the position of the currency symbol.
**Possible Values:**
**true** - Display the currency symbol before the currency value. This is the default value.
**false** - Display the currency symbol after the currency value.
      - `format` (object) **REQ** — Represents the format of the base currency with details like decimal_separator, thousand_separator, and decimal_places.
        - `numeral_system` (string) **REQ** [enum=['Indian', 'International'], default=International] — Numeral grouping system used for formatting.
        - `decimal_places` (string) **REQ** [enum=['0', '2', '3', '4', '5', '6']] — Represents the number of decimal places allowed for the currency. It can be **0, 2, and 3.**
        - `decimal_separator` (string) **REQ** [enum=['Comma', 'Period']] — The decimal separator separates the integer part of the currency from its fractional part. It can be a **Period or Comma,** depending on the currency.
        - `thousand_separator` (string) **REQ** [enum=['Comma', 'Period', 'Space']] — The thousand separator separates groups of thousands in a currency. It can be a **Period**, **Comma**, or **Space**, depending on the currency.
      - `exchange_rate` (string) **REQ** [maxLen=18, pattern=^[0-9]{1,9}(\.[0-9]{1,9})?$] — Represents the rate at which the currency has to be exchanged with home currency. Accepts positive decimal numbers up to nine digits and nine decimal places. Example: 123456789.123456789.
      - `is_active` (boolean) **REQ** — Indicates whether the currency is active and available for use.
      - `exchange_rate_auto_update` (boolean) — Indicates whether the currency has the automated exchange rate option enabled or not.
      - `iso_code` (string) **REQ** [maxLen=3] — Represents the ISO code of the currency. You can get the currency code from the CRM UI at **Setup > General > Company Settings > Currencies.**
      - `symbol` (string) **REQ** [maxLen=50] — Indicates the currency symbol used for display.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the currency. You can get the available currencies from the CRM UI at **Setup > General > Company Settings > Currencies.**
      - `is_base` (boolean) **REQ** — Indicates whether this is the base currency of the organization.
      - `id` (string/int64) **REQ** [maxLen=255] — Unique ID associated with this currency.
      - `created_by` (object) **REQ** — User who created the currency record.
        - `name` (string) **REQ** [maxLen=255] — Name of the user who created this currency.
        - `id` (string/int64) **REQ** [maxLen=255] — The unique identifier of the user who created the currency record.
      - `modified_by` (object) **REQ** — User who last modified the currency record.
        - `name` (string) **REQ** [maxLen=255] — Name of the user who last updated this currency.
        - `id` (string/int64) **REQ** [maxLen=255] — The unique identifier of the user who last modified the currency record.
      - `modified_time` (string/date-time) **REQ** — Timestamp when the currency was last modified.
      - `created_time` (string/date-time) **REQ** — Timestamp when the currency was initially created.
      - `exchange_rate_updated_time` (string/date-time) — Timestamp when the exchange rate was last modified.

- **204**: No content - currency not found or nothing to return.

- **403**: Forbidden. Multi-currency feature is not enabled for the organization. [application/json]
    > Error response when multi-currency is not enabled.
    - `code` (string) **REQ** [maxLen=100, enum=['CURRENCIES_NOT_ENABLED']] — Error code indicating the type of error.
    - `details` (object) **REQ** — Additional details about the error.
    - `message` (string) **REQ** [maxLen=255] — Human-readable message indicating that the multi-currency feature is not enabled for the organization.
    - `status` (string) **REQ** [maxLen=20, enum=['error']] — Response status indicator.

**Scopes:** ZohoCRM.settings.currencies.READ

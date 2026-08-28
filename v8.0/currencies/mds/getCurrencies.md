# GET /org/currencies
**Operation:** `getCurrencies` — List currencies
> Retrieves all added currencies in the organization.

**Responses:**

- **200**: Successfully retrieved currency data. [application/json]
    > Response object containing a list of currencies.
    - `currencies` (array of object) [maxItems=180] **REQ** — JSON array indicating the list of currencies configured for the organization.
      - `prefix_symbol` (boolean) **REQ** — Represents the position of the currency symbol.
**Possible Values:**
**true** - Display the currency symbol before the currency value. This is the default value.
**false** - Display the currency symbol after the currency value.
      - `format` (object) **REQ** — Currency formatting rules including numeral style, decimals and separators.
        - `numeral_system` (string) **REQ** [enum=['Indian', 'International'], default=International] — Number formatting style: Indian (1,00,000) vs International (100,000).
        - `decimal_places` (string) **REQ** [enum=['0', '2', '3', '4', '5', '6']] — Represents the number of decimal places allowed for the currency. It can be **0, 2, and 3.**
        - `decimal_separator` (string) **REQ** [enum=['Comma', 'Period']] — The decimal separator separates the integer part of the currency from its fractional part. It can be a **Period or Comma,** depending on the currency.
        - `thousand_separator` (string) **REQ** [enum=['Comma', 'Period', 'Space']] — The thousand separator separates groups of thousands in a currency. It can be a **Period, Comma, or Space**, depending on the currency.
      - `exchange_rate` (string) **REQ** [maxLen=18, pattern=^[0-9]{1,9}(\.[0-9]{1,9})?$] — Exchange rate relative to the base currency (supports up to 9 digits and 9 decimal places).
      - `is_active` (boolean) **REQ** — Represents the status of the currency.
**Possible Values:**
**true** - The currency is active. This is the default value.
**false** - The currency is inactive.
      - `exchange_rate_auto_update` (boolean) — Indicates whether the currency has the automated exchange rate option enabled or not.
      - `iso_code` (string) **REQ** [maxLen=3] — Represents the ISO code of the currency. You can get the currency code from the CRM UI at **Setup > General > Company Settings > Currencies.**
      - `symbol` (string) **REQ** [maxLen=50] — Symbol used to represent the currency.
      - `name` (string) **REQ** [maxLen=255] — Name of the currency. Example: Indian Rupee.
      - `is_base` (boolean) **REQ** — Indicates whether this currency is the organization's base currency.
      - `id` (string/int64) **REQ** [maxLen=255] — Unique identifier of the currency.
      - `created_by` (object) **REQ** — Indicates the user who created the currency record.
        - `name` (string) **REQ** [maxLen=255] — Name of the user who created the record.
        - `id` (string/int64) **REQ** [maxLen=255] — The unique identifier of the record creator.
      - `modified_by` (object) **REQ** — Indicates the user who last updated the currency record.
        - `name` (string) **REQ** [maxLen=255] — Name of the user who modified the record.
        - `id` (string/int64) **REQ** [maxLen=255] — The unique identifier of the user who modified the record. 
      - `modified_time` (string/date-time) **REQ** — Timestamp when the currency was last modified.
      - `created_time` (string/date-time) **REQ** — Timestamp when the currency was first created.
      - `exchange_rate_updated_time` (string/date-time) — Timestamp when the exchange rate was last modified.

- **204**: No content - occurs if no currencies are available.

- **403**: Forbidden. Multi-currency feature is not enabled for the organization. [application/json]
    > Error response when multi-currency is not enabled.
    - `code` (string) **REQ** [maxLen=100, enum=['CURRENCIES_NOT_ENABLED']] — Error code indicating the type of error.
    - `details` (object) **REQ** — Additional details about the error.
    - `message` (string) **REQ** [maxLen=255] — Human-readable message indicating that the multi-currency feature is not enabled for the organization.
    - `status` (string) **REQ** [maxLen=20, enum=['error']] — Response status indicator.

**Scopes:** ZohoCRM.settings.currencies.READ

# GET /settings/fiscal_year
**Operation:** `getFiscalYear` — Get Fiscal Year Settings
> To retrieve the fiscal year settings configured for your Zoho CRM organization.

**Responses:**

- **200**: Returns the fiscal year settings configured for the Zoho CRM organization. — Schema: `GetfiscalyearResponse200` [application/json]
    > Represents the response body containing the fiscal year settings configured for the organization.
    schema: `GetfiscalyearResponse200`
    - `fiscal_year` (object `GETFiscalYearNested`) **REQ** — Represents the fiscal year settings configured for the organization, including the calendar type, start month, structure, and surplus week information.
      schema: `GETFiscalYearNested`
      - `calendar_type` (string) **REQ** [maxLen=255] — Represents the calendar type configured for the fiscal year.
      - `display_based_on` (string) **REQ** [maxLen=255] — Represents whether the fiscal year label is based on the start month or end month of the fiscal period.
      - `surplus_week` (object `GETSurplusWeekNested`) **REQ** — Represents the surplus week configuration, including the quarter, period, and year in which the surplus week is placed.
        schema: `GETSurplusWeekNested`
        - `period` (integer/int32) **REQ** — Represents the period within the quarter in which the surplus week falls.
        - `year` (integer/int32) **REQ** — Represents the year for which the surplus week is configured.
        - `quarter` (integer/int32) **REQ** — Represents the quarter in which the surplus week falls.
      - `start_month` (string) **REQ** [maxLen=255] — Represents the start month of the fiscal year.
      - `interval_display_option` (string) **REQ** [maxLen=255, nullable] — Represents the display format configured for fiscal periods.
      - `id` (string/int64) **REQ** [maxLen=255] — Represents the unique identifier of the fiscal year configuration.
      - `structure` (string) **REQ** [maxLen=255, nullable] — Represents the week distribution structure configured for the custom fiscal year.
      - `past_surplus_weeks` (null) **REQ** — Represents the surplus week configurations from past fiscal years.
      - `start_date` (string) **REQ** [maxLen=255, nullable] — Represents the start date of the custom fiscal year.

- **401**: The request failed because the OAuth access token is missing, invalid, or does not include the required scope. [application/json]
    > Contains one of the possible authentication error responses returned when the fiscal year settings cannot be retrieved.
    oneOf:
      - `OAuthScopeMismatchError` — Represents the error returned when the OAuth access token does not include the required scope to access this endpoint.
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code. Possible values: `OAUTH_SCOPE_MISMATCH`.
        - `details` (object) **REQ** — Represents an empty details object returned with the error.
        - `message` (string) **REQ** [enum=['invalid oauth scope to access this URL']] — Represents the error message. Possible values: `invalid oauth scope to access this URL`.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.
      - `AuthenticationFailureError` — Represents the error returned when the OAuth access token is missing or invalid.
        - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code. Possible values: `AUTHENTICATION_FAILURE`.
        - `details` (object) **REQ** — Represents an empty details object returned with the error.
        - `message` (string) **REQ** [enum=['Authentication failed']] — Represents the error message. Possible values: `Authentication failed`.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: `error`.

**Scopes:** ZohoCRM.settings.fiscal_year.READ

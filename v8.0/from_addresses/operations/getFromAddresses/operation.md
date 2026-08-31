# GET /settings/emails/actions/from_addresses
**Operation:** `getFromAddresses` — Get from addresses
> To retrieve the list of email addresses configured as sender addresses for a user in your Zoho CRM organization.

**Responses:**

- **200**: Returns the list of from-address entries configured for the requested user. [application/json]
    > Represents the successful response body, containing the list of configured from-address entries.
    - `from_addresses` (array of object) [maxItems=200] **REQ** — Represents the list of from-address entries configured for the user.
      - `email` (string) **REQ** [maxLen=254, pattern=[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}] — Represents the email address of the from-address entry.
      - `type` (string) **REQ** [maxLen=32] — Represents the type of the from-address entry.
      - `user_name` (string) **REQ** [maxLen=256] — Represents the display name of the user associated with the from-address entry.
      - `id` (string/int64) [nullable] — Represents the unique identifier of the from-address entry.
      - `default` (boolean) — Indicates whether this is the user's default from address.
Possible values:
**true** - This is the default sender address.
**false** - This is not the default sender address.

**Scopes:** ZohoCRM.settings.emails.READ

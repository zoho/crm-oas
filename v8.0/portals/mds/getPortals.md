# GET /settings/portals
**Operation:** `getPortals` — Portals
> To retrieve the list of all portals configured for the Zoho CRM organization. A 204 response indicates no portal has been created yet.

**Responses:**

- **200**: Returns the list of portals configured for the organization with their summary details. [application/json]
    > Represents the 200 response schema for listing portals, containing the array of portal summary objects.
    - `portals` (array of object) [maxItems=100] **REQ** — Represents the list of portals configured for the organization.
      - `created_time` (string/date-time) **REQ** — Represents the timestamp when the portal was first added.
      - `modified_time` (string/date-time) **REQ** — Represents the timestamp when the portal configuration was last modified.
      - `modified_by` (object) **REQ** — Represents the Zoho CRM user who last modified this portal.
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who last modified this portal.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the user who last modified this portal.
      - `created_by` (object) **REQ** — Represents the Zoho CRM user who created this portal.
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who created this portal.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the user who created this portal.
      - `zaid` (string) **REQ** [maxLen=255] — Represents the Zoho account ID (`zaid`) associated with the portal.
      - `name` (string) **REQ** [maxLen=60] — Represents the unique name of the portal.
      - `active` (boolean) **REQ** — Indicates whether the portal is active.
      - `login_url` (string) [maxLen=2048] — Represents the login URL for the portal.

- **204**: No portal has been created for this organization. The response body is empty.

- **400**: The API is not supported in the current environment. Resolution: Retry the request in a production environment. [application/json]
    > Represents the API_NOT_SUPPORTED error returned when the Get Portals API is called in a sandbox environment.
    - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code for this response.
Possible values: **API_NOT_SUPPORTED** - the API is not supported in the current environment. 
    - `details` (object) **REQ** — Represents additional error context.
      - `unsupported_environment` (string) [maxLen=255] — Represents the environment type that does not support this API.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the failure.
    - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. 

- **403**: The authenticated user does not have the required `ZohoCRM.settings.clientportal.READ` permission. Resolution: Ensure the access token includes the correct scope. [application/json]
    > Represents the NO_PERMISSION error returned when the authenticated user lacks the required portal read permission.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response.
Possible values: **NO_PERMISSION** - the authenticated user lacks the required permission. 
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing permission.
    - `details` (object) **REQ** — Represents additional context about the missing permission.
      - `permissions` (array of string) [maxItems=100] — Represents the list of required permission identifiers that the user lacks.
        items: [maxLen=255]
    - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. 

**Scopes:** ZohoCRM.settings.clientportal.READ

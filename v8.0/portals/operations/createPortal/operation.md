# POST /settings/portals
**Operation:** `createPortal` — Portal
> To create a Client Portal for the Zoho CRM organization. Only one portal can be created per organization. The portal name must be unique across Zoho, between 6 and 30 characters.

**Request Body** (required) — application/json
> The request body must contain a **portals** array with exactly one portal object specifying the portal name. The name must be unique, between 6 and 30 characters.
  > Represents the request body schema for creating a portal, containing the portal name.
  - `portals` (array of object) [maxItems=100] **REQ** — Specify the list of portals to create. Only one portal is allowed per request.
    - `name` (string) **REQ** [maxLen=30, minLen=6] — Specify the display name for the portal. The name must be between 6 and 30 characters.

**Responses:**

- **200**: Returns the result of the portal creation, including the portal name and a SUCCESS status code. [application/json]
    > Represents the 200 response schema for a successful portal creation, including the portal name and result code.
    - `portals` (array of object) [maxItems=100] **REQ** — Represents the list of created portals.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the portal creation.
Possible values: **SUCCESS** - the portal creation completed successfully. 
      - `message` (string) **REQ** [maxLen=255] — Represents the confirmation message for the portal creation.
      - `details` (object) **REQ** — Represents the details of the created portal.
        - `name` (string) **REQ** [maxLen=30] — Represents the name of the created portal.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall status of the portal creation.
Possible values: **success** - the operation completed successfully. 

- **400**: The request is invalid. Possible causes include an invalid portal name format, a portal name that is already in use, a missing required field, or a sandbox restriction. Resolution: Review the error details and correct the request before retrying. [application/json]
    > Represents the 400 error response schema for portal creation, covering per-portal validation errors and sandbox restrictions.
    oneOf:
        - `portals` (array of object) [maxItems=100] — Represents the list of per-portal validation errors returned when the request is invalid.
          - `code` (string) **REQ** [enum=[5 values]] — Represents the error code identifying the type of validation failure.
Possible values: **INVALID_DATA** - a field value is invalid or out of range. **ALREADY_USED** - the portal name is already in use. **MANDATORY_NOT_FOUND** - a required field is missing. 
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the validation failure.
          - `details` (object) **REQ** — Represents additional context about the validation error.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the validation error.
            - `json_path` (string) [maxLen=255] — Represents the JSON Path location of the field that caused the validation error.
            - `minimum_length` (integer/int32) — Represents the minimum required character length for the field.
            - `maximum_length` (integer/int32) — Represents the maximum allowed character length for the field.
            - `expected_data_type` (string) [maxLen=255] — Represents the expected data type for the field that failed validation.
            - `regex` (string) [maxLen=255] — Represents the regular expression pattern the field value must match.
            - `resource_path_index` (integer/int32) — Represents the index of the array item associated with the validation error.
          - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request encountered a validation error. 
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code for this response.
Possible values: **API_NOT_SUPPORTED** - the API is not supported in the current environment. 
        - `details` (object) **REQ** — Represents additional error context.
          - `unsupported_environment` (string) [maxLen=255] — Represents the environment type that does not support this API.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. 

- **403**: The authenticated user does not have the required `ZohoCRM.settings.clientportal.CREATE` permission. Resolution: Ensure the access token includes the correct scope. [application/json]
    > Represents the NO_PERMISSION error returned when the authenticated user lacks the required portal creation permission.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response.
Possible values: **NO_PERMISSION** - the authenticated user lacks the required permission. 
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing permission.
    - `details` (object) **REQ** — Represents additional context about the missing permission.
      - `permissions` (array of string) [maxItems=100] — Represents the list of required permission identifiers that the user lacks.
        items: [maxLen=255]
    - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. 

**Scopes:** ZohoCRM.settings.clientportal.CREATE

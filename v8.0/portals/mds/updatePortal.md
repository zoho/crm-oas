# PUT /settings/portals/{portal}
**Operation:** `updatePortal` — Portal
> To update the configuration of an existing portal in the Zoho CRM organization, including the portal name and SAML single sign-on settings.

**Parameters:**
- `portal` (path, string, required) [maxLen=60]: Specify the API name of the portal to retrieve or update. Use the Get Portals operation to retrieve the list of available portals and their names.

**Request Body** (required) — application/json
> The request body must contain a **portals** array with exactly one portal update object. You can update the portal name and SAML configuration. All SAML fields - `login_url`, `logout_url`, and `public_key` - are required when updating SAML settings.
  > Represents the request body schema for updating a portal, supporting name and SAML configuration updates.
  - `portals` (array of object) [maxItems=100] **REQ** — Specify the list of portal update objects. Only one portal is allowed per request.
    - `name` (string) [maxLen=30, minLen=6] — Specify the updated display name for the portal. The name must be between 6 and 30 characters.
    - `saml_configuration` (object) — Specify the SAML configuration to apply to the portal.
      - `login_url` (string) **REQ** [maxLen=2048, pattern=http[s]://www[.][a-z]{7}[.]com] — Specify the SAML SSO login URL for the portal. Must begin with `https://www.`. Required when updating SAML configuration.
      - `logout_url` (string) **REQ** [maxLen=2048, pattern=http[s]://www[.][a-z]{7}[.]com] — Specify the SAML SSO logout URL for the portal. Must begin with `https://www.`. Required when updating SAML configuration.
      - `public_key` (string) **REQ** [maxLen=5000] — Specify the SAML X.509 public key certificate. Required when updating SAML configuration.
      - `active` (boolean) [enum=[True]] — Specify **true** to activate the SAML configuration for the portal. Possible values: **true**.

**Responses:**

- **200**: Returns the result of the portal update, including the updated portal name and a SUCCESS status code. [application/json]
    > Represents the 200 response schema for a successful portal update, including the portal name and result code.
    - `portals` (array of object) [maxItems=100] **REQ** — Represents the list of updated portal results.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the portal update.
Possible values: **SUCCESS** - the portal update completed successfully. 
      - `message` (string) **REQ** [maxLen=255] — Represents the confirmation message for the portal update.
      - `details` (object) **REQ** — Represents the details of the updated portal.
        - `name` (string) **REQ** [maxLen=30] — Represents the name of the updated portal.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall status of the portal update.
Possible values: **success** - the operation completed successfully. 

- **400**: The request is invalid. Possible causes include an invalid portal name, a name already in use, a missing required SAML field, a null value for a required field, or a sandbox restriction. Resolution: Review the error details and correct the request before retrying. [application/json]
    > Represents the 400 error response schema for portal updates, covering per-portal validation errors and sandbox restrictions.
    oneOf:
        - `portals` (array of object) [maxItems=100] **REQ** — Represents the list of per-portal validation errors returned when the update request is invalid.
          - `code` (string) **REQ** [enum=[6 values]] — Represents the error code identifying the type of validation failure.
Possible values: **INVALID_DATA** - a field value is invalid or out of range. **ALREADY_USED** - the portal name is already in use. **MANDATORY_NOT_FOUND** - a required field is missing. **NOT_ALLOWED** - the operation is not permitted. 
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
        - `code` (string) **REQ** [enum=[6 values]] — Represents the error code for the top-level error.
Possible values: **INVALID_DATA** - a field value is invalid. **ALREADY_USED** - the portal name is already in use. **MANDATORY_NOT_FOUND** - a required field is missing. **NOT_ALLOWED** - the operation is not permitted. 
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

- **403**: The authenticated user does not have the required `ZohoCRM.settings.clientportal.UPDATE` permission. Resolution: Ensure the access token includes the correct scope. [application/json]
    > Represents the NO_PERMISSION error returned when the authenticated user lacks the required portal update permission.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response.
Possible values: **NO_PERMISSION** - the authenticated user lacks the required permission. 
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing permission.
    - `details` (object) **REQ** — Represents additional context about the missing permission.
      - `permissions` (array of string) [maxItems=100] — Represents the list of required permission identifiers that the user lacks.
        items: [maxLen=255]
    - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. 

**Scopes:** ZohoCRM.settings.clientportal.UPDATE

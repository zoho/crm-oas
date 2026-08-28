# DELETE /settings/duplicate_check_preference
**Operation:** `deleteDuplicateCheckPreference` — Delete Duplicate Check Preference
> To delete the duplicate check preference configured for the Leads module in your Zoho CRM organization.

**Parameters:**
- `module` (query, string, required) [enum=['Leads']]: Represents the module whose Duplicate Check Preference details you want to retrieve.  Supported module: Leads.

**Responses:**

- **200**: Returns a success response confirming that the API deleted the duplicate check preference. [application/json]
    > Represents the success response returned after the API deletes the duplicate check preference.
    - `duplicate_check_preference` (object) **REQ** — Details of the deleted duplicate check preference
      - `code` (string) [enum=['SUCCESS']] — Response code indicating the result of the deletion
      - `status` (string) [enum=['success']] — Status of the deletion operation
      - `message` (string) [maxLen=1000] — Represents the message confirming the deletion.
      - `details` (object) — Additional details about the deletion operation

- **400**: Bad Request - Invalid or missing parameters [application/json]
    oneOf:
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code
        - `details` (object) **REQ** — Additional error context
          - `param_name` (string) [maxLen=50] — Missing parameter name
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code
        - `details` (object) **REQ** — Additional error context
          - `param_name` (string) [maxLen=50] — Invalid parameter name
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Error code
        - `details` (object) **REQ** — Additional error context
          - `param_name` (string) [maxLen=50] — Name of the unsupported parameter
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Error status indicator

- **403**: No permission or feature not enabled [application/json]
    oneOf:
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating permission denied
        - `details` (object) **REQ** — Additional error details
          - `permissions` (array of string) [maxItems=25] — List of required permissions
            items: [maxLen=255]
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Status indicator for error
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Error code indicating feature is not enabled
        - `details` (object) **REQ** — Additional error details (typically empty)
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Status indicator for error

**Scopes:** ZohoCRM.settings.duplicate_check_preference.DELETE

# DELETE /Contacts/roles
**Operation:** `deleteContactRoles` — Delete Contact Roles
> Deletes one or more contact roles by their unique identifiers in your Zoho CRM organization.

**Parameters:**
- `ids` (query, string, required) [maxLen=255]: Specify a comma-separated list of contact role IDs to delete. Use the [List Contact Roles](contact_roles.yaml#$.paths./contacts/roles.get) resource to retrieve contact role IDs.


**Responses:**

- **200**: Returns the deletion results for all contact roles in the request. [application/json]
    > Contains the results of the contact role deletion operation.
    - `contact_roles` (array of object) [maxItems=100] **REQ** — Contains the deletion results for each contact role in the request.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code of the deletion operation.

**Possible values:**
- **SUCCESS** - The contact role deletion completed successfully.

      - `details` (object) **REQ** — Represents the details of the deleted contact role.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the deleted contact role.
      - `message` (string) **REQ** [maxLen=255] — Represents the message describing the result of the deletion operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall status of the deletion operation.

**Possible values:**
- **success** - The contact role deletion completed successfully.


- **400**: The contact roles could not be deleted due to invalid IDs or a missing required parameter.

**Resolution:** The **ids** query parameter must be provided and all specified contact role IDs must exist in the CRM organization.
 [application/json]
    > Contains the error details for the contact role deletion request.
    oneOf:
        - `contact_roles` (array of object) [maxItems=100] **REQ** — Represents the list of error results for each contact role that failed during deletion.
          oneOf:
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.

**Possible values:**
- **INVALID_DATA** - The contact role data is invalid.

              - `message` (string) **REQ** [maxLen=255] — Represents the error message.
              - `details` (object) **REQ** — Represents the error details for the invalid data.
                - `id` (string) **REQ** [maxLen=19] — Represents the ID of the contact role that triggered the invalid data error.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.

**Possible values:**
- **error** - The contact role deletion failed.

              - `status` (string) **REQ** [enum=['error']] — Represents the error status.

**Possible values:**
- **error** - The contact role deletion failed.

              - `code` (string) **REQ** [enum=['LOWER_LIMIT_REACHED']] — Represents the error code.

**Possible values:**
- **LOWER_LIMIT_REACHED** - Deleting the contact role would reduce the total below the minimum required.

              - `message` (string) **REQ** [maxLen=255] — Represents the error message.
              - `details` (object) **REQ** — Represents the error details for the limit violation.
                - `limit` (integer/int32) **REQ** — Represents the minimum number of contact roles required in the CRM organization.
                - `id` (string) **REQ** [maxLen=19] — Represents the ID of the contact role that triggered the limit error.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code.

**Possible values:**
- **REQUIRED_PARAM_MISSING** - The required **ids** query parameter is missing from the request.

        - `message` (string) **REQ** [maxLen=255] — Represents the error message.
        - `details` (object) **REQ** — Represents the error details for the missing parameter.
          - `param_name` (string) **REQ** [maxLen=100] — Represents the API name of the missing required parameter.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.

**Possible values:**
- **error** - The contact role deletion failed.


**Scopes:** ZohoCRM.modules.contacts.DELETE

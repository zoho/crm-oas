# DELETE /Contacts/roles/{role}
**Operation:** `deleteContactRole` — Delete a Contact Role
> Deletes a specific contact role by its unique identifier in your Zoho CRM organization.

**Parameters:**
- `role` (path, string, required) [maxLen=255]: Specify the unique identifier of the contact role. Use the [List Contact Roles](contact_roles.yaml#$.paths./contacts/roles.get) resource to retrieve contact role IDs.


**Responses:**

- **200**: Returns the result of the contact role deletion when the operation completes successfully. [application/json]
    > Contains the result of the contact role deletion operation.
    - `contact_roles` (array of object) [maxItems=100] **REQ** — Contains the deletion results for the contact role.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code of the deletion operation.

**Possible values:**
- **SUCCESS** - The contact role deletion completed successfully.

      - `details` (object) **REQ** — Represents the details of the deleted contact role.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the deleted contact role.
      - `message` (string) **REQ** [maxLen=255] — Represents the message describing the result of the deletion operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall status of the deletion operation.

**Possible values:**
- **success** - The contact role deletion completed successfully.


- **400**: The contact role could not be deleted due to an invalid ID or a limit violation.

**Resolution:** The contact role ID must be valid and deleting it must not reduce the total number of contact roles below the minimum required.
 [application/json]
    > Contains the error details for the contact role deletion request.
    oneOf:
        - `contact_roles` (array of object) [maxItems=100] **REQ** — Represents the list of error results for the contact role deletion operation.
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

**Scopes:** ZohoCRM.modules.contacts.DELETE

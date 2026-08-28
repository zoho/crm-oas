# PUT /Contacts/roles/{role}
**Operation:** `updateContactRole` — Update a Contact Role
> Updates a specific contact role by its unique identifier in your Zoho CRM organization.

**Parameters:**
- `role` (path, string, required) [maxLen=255]: Specify the unique identifier of the contact role. Use the [List Contact Roles](contact_roles.yaml#$.paths./contacts/roles.get) resource to retrieve contact role IDs.


**Request Body** (required) — application/json
> The request body must contain a `contact_roles` array with one object.
  > Specify the contact role details to update.
  - `contact_roles` (array of object) [maxItems=100] **REQ** — Specify the list of contact roles to update.
    - `name` (string) **REQ** [maxLen=50, pattern=[A-Za-z0-9 ]] — Specify the name of the contact role.
    - `sequence_number` (integer/int32) — Specify the display position of the contact role in the CRM UI picklist.

**Responses:**

- **200**: Returns the result of the contact role update when the operation completes successfully. [application/json]
    > Contains the result of the contact role update operation.
    - `contact_roles` (array of object) [maxItems=100] **REQ** — Contains the update result for the specified contact role.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code of the update operation.

**Possible values:**
- **SUCCESS** - The contact role update completed successfully.

      - `details` (object) **REQ** — Represents the details of the updated contact role.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the updated contact role.
      - `message` (string) **REQ** [maxLen=255] — Represents the message describing the result of the update operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall status of the update operation.

**Possible values:**
- **success** - The contact role update completed successfully.


- **400**: The contact role could not be updated due to a validation error.

**Resolution:** Review the error details, correct any invalid fields, and retry the request.
 [application/json]
    > Contains the error details for the contact role update request.
    oneOf:
        - `contact_roles` (array of object) [maxItems=100] **REQ** — Represents the list of error results for the contact role update operation.
          oneOf:
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code.

**Possible values:**
- **MANDATORY_NOT_FOUND** - A required field is missing from the request.

              - `message` (string) **REQ** [maxLen=255] — Represents the error message.
              - `details` (object) **REQ** — Represents the error details for the missing field.
                - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the missing required field.
                - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the missing required field.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.

**Possible values:**
- **error** - The contact role update failed.

              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.

**Possible values:**
- **INVALID_DATA** - The contact role data is invalid.

              - `message` (string) **REQ** [maxLen=255] — Represents the error message.
              - `details` (object) **REQ** — Represents the error details for the invalid data.
                - `id` (string) **REQ** [maxLen=19] — Represents the ID of the contact role that triggered the invalid data error.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.

**Possible values:**
- **error** - The contact role update failed.


**Scopes:** ZohoCRM.modules.contacts.UPDATE

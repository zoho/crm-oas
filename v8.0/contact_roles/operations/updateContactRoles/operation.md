# PUT /Contacts/roles
**Operation:** `updateContactRoles` — Update Contact Roles
> Updates the properties of one or more existing contact roles in your Zoho CRM organization.

**Schemas:**
`ArrayOfDuplicateSchema`:
  type: array of object [maxItems=100]
    - `status` (string) **REQ** [enum=['error']] — Represents the error status.

**Possible values:**
- **error** - The request failed.

    - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code.

**Possible values:**
- **DUPLICATE_DATA** - A contact role with the same name already exists.

    - `message` (string) **REQ** [maxLen=255] — Represents the error message.
    - `details` (object) **REQ** — Represents the error details for the duplicate data.
      oneOf:
          - `id` (string) **REQ** [maxLen=19] — Represents the ID of the existing contact role that conflicts with the duplicate name.
          - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contains a duplicate value.
          - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the field that contains a duplicate value.
          - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contains a duplicate value.
          - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the field that contains a duplicate value.
`ContactRoleSuccessSchema`:
  > Represents the result of a successful contact role operation.
  - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code of the operation.

**Possible values:**
- **SUCCESS** - The contact role operation completed successfully.

  - `details` (object) **REQ** — Represents the details of the contact role for the create or update operation.
    - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the contact role.
  - `message` (string) **REQ** [maxLen=255] — Represents the message describing the result of the operation.
  - `status` (string) **REQ** [enum=['success']] — Represents the overall status of the operation.

**Possible values:**
- **success** - The contact role operation completed successfully.

`DuplicateDataErrorSchemaPUT`:
  > Represents an error when a contact role with the same name already exists in the CRM organization.
  - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code.

**Possible values:**
- **DUPLICATE_DATA** - A contact role with the same name already exists.

  - `message` (string) **REQ** [maxLen=255] — Represents the error message.
  - `details` (object) **REQ** — Represents the error details for the duplicate data.
    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contains a duplicate value.
    - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the field that contains a duplicate value.
    - `id` (string) [maxLen=19] — Represents the ID of the contact role that has the duplicate name.
  - `status` (string) **REQ** [enum=['error']] — Represents the error status.

**Possible values:**
- **error** - The request failed.

`InvalidDataErrorSchemaPut`:
  > Represents an invalid data error for a contact role field in an update operation.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.

**Possible values:**
- **INVALID_DATA** - The contact role data is invalid.

  - `message` (string) **REQ** [maxLen=255] — Represents the error message.
  - `details` (object) **REQ** — Represents the error details for the invalid data.
    - `id` (string) [maxLen=19] — Represents the ID of the contact role that triggered the invalid data error.
    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contains invalid data.
    - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the field that contains invalid data.
  - `status` (string) **REQ** [enum=['error']] — Represents the error status.

**Possible values:**
- **error** - The request failed.

`MandatoryFieldNotFoundErrorSchema`:
  > Represents an error when a required field is missing from the request.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code.

**Possible values:**
- **MANDATORY_NOT_FOUND** - A required field is missing from the request.

  - `message` (string) **REQ** [maxLen=255] — Represents the error message.
  - `details` (object) **REQ** — Represents the error details for the missing field.
    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the missing required field.
    - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the missing required field.
  - `status` (string) **REQ** [enum=['error']] — Represents the error status.

**Possible values:**
- **error** - The request failed.


**Request Body** (required) — application/json
> The request body must contain a `contact_roles` array. You can include a maximum of 100 objects per request.
  > Specify the contact role details to update in the CRM organization.
  - `contact_roles` (array of object) [maxItems=100] **REQ** — Specify the list of contact roles to update.
    - `name` (string) **REQ** [maxLen=50, pattern=[A-Za-z0-9 ]{1,50}] — Specify the name of the contact role.
    - `id` (string) **REQ** [maxLen=19] — Specify the unique ID of the contact role to update. Use the [List Contact Roles](contact_roles.yaml#$.paths./contacts/roles.get) resource to retrieve contact role IDs.
    - `sequence_number` (number) — Specify the display position of the contact role in the CRM UI picklist.

**Responses:**

- **200**: Returns the results after the CRM updates all contact roles in the request successfully. [application/json]
    > Contains the results of the contact role update operation.
    - `contact_roles` (array of object) [maxItems=100] **REQ** — Contains the update results for each contact role in the request.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code of the update operation.

**Possible values:**
- **SUCCESS** - The contact role update completed successfully.

      - `details` (object) **REQ** — Represents the details of the updated contact role.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the updated contact role.
      - `message` (string) **REQ** [maxLen=255] — Represents the message describing the result of the update operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall status of the update operation.

**Possible values:**
- **success** - The contact role update completed successfully.


- **207**: Returns a mixed response when the CRM updates some contact roles successfully and others fail validation. [application/json]
    > Contains mixed success and error results for bulk contact role update.
    - `contact_roles` (array of object) [maxItems=100] **REQ** — Contains the mixed results for each contact role in the request.
      oneOf:
        - `MandatoryFieldNotFoundErrorSchema` — Represents an error when a required field is missing from the request.
        - `InvalidDataErrorSchemaPut` — Represents an invalid data error for a contact role field in an update operation.
        - `DuplicateDataErrorSchemaPUT` — Represents an error when a contact role with the same name already exists in the CRM organization.
        - `ArrayOfDuplicateSchema` — Contains the list of duplicate data errors for contact role operations.
        - `ContactRoleSuccessSchema` — Represents the result of a successful contact role operation.

- **400**: The contact roles could not be updated due to validation errors.

**Resolution:** Review the error details for each contact role in the response, correct any invalid fields, and retry the request.
 [application/json]
    > Contains the error details for the contact role update request.
    oneOf:
        - `contact_roles` (array of object) [maxItems=100] **REQ** — Contains the error details for each contact role that failed during the update operation.
          oneOf:
            - `MandatoryFieldNotFoundErrorSchema` — Represents an error when a required field is missing from the request.
            - `InvalidDataErrorSchemaPut` — Represents an invalid data error for a contact role field in an update operation.
            - `DuplicateDataErrorSchemaPUT` — Represents an error when a contact role with the same name already exists in the CRM organization.
            - `ArrayOfDuplicateSchema` — Contains the list of duplicate data errors for contact role operations.

**Scopes:** ZohoCRM.modules.contacts.UPDATE

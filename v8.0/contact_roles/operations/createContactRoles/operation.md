# POST /Contacts/roles
**Operation:** `createContactRoles` — Create Contact Roles
> Creates one or more contact roles in your Zoho CRM organization.

**Schemas:**
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

`DuplicateDataErrorSchemaPOST`:
  > Represents an error when a contact role with the same name already exists in the CRM organization.
  - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code.

**Possible values:**
- **DUPLICATE_DATA** - A contact role with the same name already exists.

  - `message` (string) **REQ** [maxLen=255] — Represents the error message.
  - `details` (object) **REQ** — Represents the error details for the duplicate data.
    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contains a duplicate value.
    - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the field that contains a duplicate value.
  - `status` (string) **REQ** [enum=['error']] — Represents the error status.

**Possible values:**
- **error** - The request failed.

`InvalidDataErrorSchemaPOST`:
  > Represents an invalid data error for a contact role field in a create operation.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.

**Possible values:**
- **INVALID_DATA** - The contact role data is invalid.

  - `message` (string) **REQ** [maxLen=255] — Represents the error message.
  - `details` (object) **REQ** — Represents the error details for the invalid data.
    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contains invalid data.
    - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the field that contains invalid data.
    - `expected_data_type` (string) **REQ** [maxLen=100] — Represents the expected data type for the field.
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
  > Specify the contact role details to create in the CRM organization.
  - `contact_roles` (array of object) [maxItems=100] **REQ** — Specify the list of contact roles to create.
    - `name` (string) **REQ** [maxLen=50, pattern=[A-Za-z0-9 ]{1,50}] — Specify the name of the contact role.
    - `sequence_number` (number) **REQ** — Specify the display position of the contact role in the CRM UI picklist.

**Responses:**

- **200**: Returns the contact role creation results when all contact roles in the request succeed. [application/json]
    > Contains the results of the contact role creation, with a status entry for each contact role in the request.
    - `contact_roles` (array of object `ContactRoleSuccessSchema`) [maxItems=100] **REQ** — Contains the results for each contact role in the request.

- **207**: Returns a mixed response when the CRM creates some contact roles successfully and others fail validation. [application/json]
    > Contains mixed success and error results for bulk contact role creation.
    - `contact_roles` (array of object) [minItems=2, maxItems=100] **REQ** — Contains the mixed results for each contact role in the request.
      oneOf:
        - `MandatoryFieldNotFoundErrorSchema` — Represents an error when a required field is missing from the request.
        - `InvalidDataErrorSchemaPOST` — Represents an invalid data error for a contact role field in a create operation.
        - `DuplicateDataErrorSchemaPOST` — Represents an error when a contact role with the same name already exists in the CRM organization.
        - `ContactRoleSuccessSchema` — Represents the result of a successful contact role operation.

- **400**: The contact roles could not be created due to validation errors.

**Resolution:** Review the error details for each contact role in the response, correct any invalid fields, and retry the request.
 [application/json]
    > Contains the validation errors for the contact role creation request.
    - `contact_roles` (array of object) [maxItems=100] **REQ** — Contains the validation errors for each contact role that failed.
      oneOf:
        - `MandatoryFieldNotFoundErrorSchema` — Represents an error when a required field is missing from the request.
        - `InvalidDataErrorSchemaPOST` — Represents an invalid data error for a contact role field in a create operation.
        - `DuplicateDataErrorSchemaPOST` — Represents an error when a contact role with the same name already exists in the CRM organization.

**Scopes:** ZohoCRM.modules.contacts.WRITE

# GET /{module}/{dealId}/Contact_Roles
**Operation:** `getAssociatedContactRoles` — Deal Contact Roles
> Retrieve contact roles associated with a deal.

**Parameters:**
- `module` (path, string, required) [enum=['Deals']]: Represents the module name for the deal record. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get the required module API name.
- `dealId` (path, string/int64, required): Represents the unique identifier of the deal record. Use the [Get Records API](record.yaml#$.paths./{module}.get) and get the unique ID of the Deal.
- `fields` (query, string, required) [maxLen=1000, minLen=1, pattern=^[A-Za-z_][A-Za-z0-9_]*(?:,[A-Za-z_][A-Za-z0-9_]*)*$]: Comma-separated list of field names to include in the response. Field names must follow API naming conventions. Use the [Get Fields API](fields.yaml#$.paths./settings/fields.get) to get the valide field API names.

**Responses:**

- **200**: Successfully retrieved contact roles associated with the deal. [application/json]
    > Response containing contact roles data and pagination details.
    - `data` (array of object) [maxItems=100] **REQ** — Array of contact role records with fields specified in the query parameter
      - `Owner` (object) — Owner information for the contact role
        - `name` (string) [maxLen=255] — Owner's display name
        - `id` (string/int64) — Owner's unique identifier
        - `email` (string/email) — Owner's email address
      - `Department` (string) [nullable] — Department of the contact
      - `Contact_Role` (object) — Contact role information
        - `name` (string) **REQ** [maxLen=255] — Role name (e.g., Developer/Evaluator)
        - `id` (string/int64) **REQ** — Role's unique identifier
      additionalProperties: any
    - `info` (object) **REQ** — Pagination and response metadata
      - `per_page` (integer/int32) **REQ** — Number of records per page
      - `next_page_token` (string) [maxLen=1024, nullable] — Token for retrieving the next page of results
      - `count` (integer/int32) **REQ** — Number of records in the current response
      - `page` (integer/int32) **REQ** — Current page number
      - `previous_page_token` (string) [maxLen=1024, nullable] — Token for retrieving the previous page of results
      - `page_token_expiry` (string) [maxLen=1024, nullable] — Expiry timestamp for page tokens
      - `more_records` (boolean) **REQ** — Indicates if more records are available

- **204**: No contact roles found for the specified deal.

- **400**: The response body of errors such as Invalid data, invalid module, field limit exceeded, or required parameter missing. [application/json]
    > Represents the error response, which can be one of several specific following error types.
    oneOf:
      - `InvalidDataError` — Error response of an invalid related ID provided in the request.
        - `code` (string) **REQ** [const=INVALID_DATA] — Error code indicating invalid deal ID
        - `details` (object) **REQ** — Error details containing the path index
          - `resource_path_index` (integer/int64) **REQ** [const=1] — Index of the path parameter that is invalid (1 for deal ID)
        - `message` (string) **REQ** [const=the related id given seems to be invalid] — Error message indicating the deal ID is invalid
        - `status` (string) **REQ** [const=error] — Response status
      - `InvalidModuleError` — Error response of an invalid module name provided in the request.
        - `code` (string) **REQ** [const=INVALID_MODULE] — Error code indicating invalid module name
        - `details` (object) **REQ** — Error details containing the path index
          - `resource_path_index` (integer/int32) **REQ** [const=0] — Index of the path parameter that is invalid (0 for module)
        - `message` (string) **REQ** [const=the module name given seems to be invalid] — Error message indicating the module name is invalid
        - `status` (string) **REQ** [const=error] — Response status
      - `RequiredParamMissingError` — Error response of a missing required parameter.
        - `code` (string) **REQ** [const=REQUIRED_PARAM_MISSING] — Error code indicating a required parameter is missing
        - `details` (object) **REQ** — Error details containing the missing parameter name
          - `param_name` (string) **REQ** [const=fields] — Name of the missing required parameter
        - `message` (string) **REQ** [const=One of the expected parameter is missing] — Error message indicating a parameter is missing
        - `status` (string) **REQ** [const=error] — Response status
      - `InvalidRelationNameError` — Error response when the user provided an invalid relation name in the request.
        - `code` (string) **REQ** [const=INVALID_DATA] — Error code indicating invalid relation name
        - `details` (object) **REQ** — Error details containing the path index
          - `resource_path_index` (integer/int32) **REQ** [const=2] — Index of the path parameter that is invalid (2 for relation name)
        - `message` (string) **REQ** [const=the relation name given seems to be invalid] — Error message indicating the relation name is invalid
        - `status` (string) **REQ** [const=error] — Response status

- **403**: Error response when the user does not have enough permission to access deals or contacts. [application/json]
    > Represents the error response body when the user lacks permission to access deals or contacts.
    oneOf:
      - `NoPermissionDealsError` — Represents the error response when the user does not have permission to view deals.
        - `code` (string) **REQ** [const=NO_PERMISSION] — Error code indicating lack of permission
        - `details` (object) **REQ** — Details about the missing permissions
          - `permissions` (array of string) [maxItems=1] **REQ** — List of required permissions that are missing
            items: [const=Crm_Implied_View_Potentials]
        - `message` (string) **REQ** [const=permission denied] — Error message indicating permission denial
        - `status` (string) **REQ** [const=error] — Response status
      - `NoPermissionContactsError` — Represents the error response when the user does not have permission to view contacts.
        - `code` (string) **REQ** [const=NO_PERMISSION] — Error code indicating lack of permission
        - `details` (object) **REQ** — Details about the missing permissions
          - `permissions` (array of string) [maxItems=1] **REQ** — List of required permissions that are missing
            items: [const=Crm_Implied_View_Contacts]
        - `message` (string) **REQ** [const=permission denied] — Error message indicating permission denial
        - `status` (string) **REQ** [const=error] — Response status

- **500**: Response body of an Internal Server Error. [application/json]
    > Provides the internal server error response object containing code, message, details, and status.
    - `code` (string) **REQ** [maxLen=50] — Provides the error code indicating the type of error.
    - `message` (string) **REQ** [maxLen=255] — Provides the details of the error.
    - `details` (object) **REQ** — Specifies the additional details about the error.
    - `status` (string) **REQ** [enum=['error']] — Provides the status of the error response.

**Scopes:** ZohoCRM.modules.CONTACTS.READ, ZohoCRM.modules.DEALS.READ

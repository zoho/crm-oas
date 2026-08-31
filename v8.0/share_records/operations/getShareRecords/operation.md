# GET /{moduleApiName}/{recordId}/actions/share
**Operation:** `getShareRecords` — Share Records
> To retrieve the share details of a specific record in a module of your Zoho CRM organization. The response lists each entry with the recipient, the access level, and the sharing metadata.

**Parameters:**
- `moduleApiName` (path, string, required) [maxLen=50]: Specify the API name of the module that owns the record. Refer to the [Get Modules API](modules.yaml#$.paths./settings/modules.get) for valid values.
- `recordId` (path, string/int64, required): Specify the unique ID of the record. Refer to the [Get Records API](record.yaml#$.paths./{module}.get) for valid values.
- `sharedTo` (query, string, optional) [maxLen=19]: Specify the unique ID of the user whose share entries you want to retrieve. When set, the response returns only the share entries for that user. Use the [Get Users API](users.yaml#$paths./users.get) to get the valid IDs for the users. 
- `view` (query, string, optional) [enum=['manage', 'summary']]: Specify the level of detail to include in the response. 
**Possible values**:  summary, manage.

- `approved` (query, string, optional) [enum=['true', 'false', 'both']]: Filters sharing records by approval status.
- `true`  - return only approved sharing entries
- `false`  - return only unapproved (pending) sharing entries
- `both`  - return all sharing entries regardless of approval status
- `current_user` (query, boolean, optional): Specify whether to return only the share entries for the current user. When set to **true**, the response returns only the share entries for the user making the API call.

**Responses:**

- **200**: Returns the list of share entries currently active on the record, with the recipient, the access level, and the sharing metadata for each entry. [application/json]
    > Represents the success response.
    - `share` (array of object) [maxItems=2147483647] — Represents the list of share records.
      - `shared_with` (object) **REQ** — Represents the details of the entity (user, role, or group) with which the record is shared.
        - `name` (string) **REQ** [maxLen=100] — Represents the name of the entity with whom the record is shared.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the entity with whom the record is shared.
        - `type` (string) **REQ** [enum=['users', 'roles', 'groups']] — Represents the type of sharing applied to the
record. 

**Possible values**: 

- users

- roles

- groups

      - `share_related_records` (boolean) **REQ** — Indicates whether the related records of the shared record are also shared with the entity.
      - `shared_through` (object) **REQ** — Represents the details of the record through which sharing is granted, including its module.
        - `module` (object) **REQ** — Represents the module details of the record through which sharing is granted.
          - `name` (string) **REQ** [maxLen=100] — Represents the name of the module.
          - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the module.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the record through which sharing is enabled.
      - `shared_time` (string/date-time) — Represents the date and time at which the record was shared, in ISO 8601 format.
      - `permission` (string) **REQ** [enum=['read_only', 'read_write', 'full_access']] — Represents the level of access granted to the entity
for the shared record. **Possible values**: 

- read_only

- read_write

- full_access

      - `shared_by` (object) — Represents the details of the user who shared the record.
        - `name` (string) **REQ** [maxLen=100] — Represents the name of the entity.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the entity.
        - `zuid` (string) **REQ** [maxLen=19] — Represents the ZUID of the user who shared the record.
      - `type` (string) **REQ** [enum=['private', 'public']] — Represents the type of sharing applied to the
record. 

**Possible values**: 

- private

- public


- **204**: Returns an empty response when the record has no active share entries.

- **400**: Returns an error response when the request URL, path parameters, or share entries fail validation. [application/json]
    > Represents the error responses for the API request.
    oneOf:
      - `ViewAndApprovedParamValueErrorResponse` — Represents the error response returned when the `view` query parameter is set to an unsupported value.
        - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Represents the response code returned by the API.
        - `details` (object) **REQ** — Represents the additional information about the response.
          - `api_name` (string) **REQ** [enum=['view', 'approved']] — Represents the API name of the parameter that caused the error.
        - `message` (string) **REQ** [enum=['Please check whether the input values are correct']] — Represents the response message returned by the API.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.
      - `InvalidRecordIdErrorResponse` — Represents the error response returned when the record ID in the request URL is invalid or does not belong to the specified module.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code returned by the API.
        - `details` (object) **REQ** — Represents the additional information about the response.
          - `resource_path_index` (integer/int32) **REQ** [default=1] — Represents the index of the URL path segment that caused the
error. Default value: **1**.

        - `message` (string) **REQ** [enum=['ENTITY_ID_INVALID']] — Represents the response message returned by the API. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.
      - `InvalidModuleNameErrorResponse` — Represents the error response returned when the module API name in the request URL is invalid or not supported.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the response code returned by the API.
        - `details` (object) **REQ** — Represents the additional information about the response.
          - `resource_path_index` (integer/int32) **REQ** [default=0] — Represents the index of the URL path segment that caused the
error. Default value: **0**.

        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the response message returned by the API.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.

- **403**: Returns an error response when the user does not have permission to perform the share details retrieval or when the share operation is blocked by an org-level restriction. [application/json]
    > Represents the error responses for the API request.
    oneOf:
      - `CommonForbiddenErrorResponse` — Represents the forbidden error response returned when the user does not have permission to access the API.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the response code returned by the API.
        - `details` (object) **REQ** — Represents the additional information about the response.
        - `message` (string) **REQ** [enum=['permission denied - access the api', 'permission denied']] — Represents the response message returned by the API. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.
      - `RecordForbiddenErrorResponse` — Represents the forbidden error response returned when the user does not have the required record-level permissions in the specified module.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the response code returned by the API.
        - `details` (object) **REQ** — Represents the additional information about the response.
          - `permissions` (array of string) [maxItems=1] **REQ** — Represents the list of permissions that the user is missing.
            items: [maxLen=200]
        - `message` (string) **REQ** [enum=['permission denied']] — Represents the response message returned by the API.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.

**Scopes:** ZohoCRM.share.leads.READ, ZohoCRM.share.contacts.READ, ZohoCRM.share.accounts.READ, ZohoCRM.share.deals.READ, ZohoCRM.share.products.READ, ZohoCRM.share.tasks.READ, ZohoCRM.share.events.READ, ZohoCRM.share.calls.READ, ZohoCRM.share.quotes.READ, ZohoCRM.share.invoices.READ, ZohoCRM.share.campaigns.READ, ZohoCRM.share.vendors.READ, ZohoCRM.share.pricebooks.READ, ZohoCRM.share.salesorders.READ, ZohoCRM.share.purchaseorders.READ, ZohoCRM.share.solutions.READ, ZohoCRM.share.cases.READ, ZohoCRM.share.bundles.READ, ZohoCRM.share.custom.READ

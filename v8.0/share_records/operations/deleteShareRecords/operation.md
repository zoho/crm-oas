# DELETE /{moduleApiName}/{recordId}/actions/share
**Operation:** `deleteShareRecords` — Revoke sharing on a record
> To revoke all sharing on a specific record in a module of your Zoho CRM organization. Use this operation to remove access that was previously granted to users, roles, or groups through record-level sharing.

**Parameters:**
- `moduleApiName` (path, string, required) [maxLen=50]: Specify the API name of the module that owns the record. Refer to the [Get Modules API](modules.yaml#$.paths./settings/modules.get) for valid values.
- `recordId` (path, string/int64, required): Specify the unique ID of the record. Refer to the [Get Records API](record.yaml#$.paths./{module}.get) for valid values.

**Responses:**

- **200**: Returns a confirmation that sharing on the record has been revoked successfully. [application/json]
    > Represents the revoke sharing success response.
    - `share` (object) — Represents the share record revoke response details.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code returned by the API.
      - `details` (object) **REQ** — Represents the additional information about the response.
        - `id` (string) [maxLen=19] — Represents the unique ID of the details.
      - `message` (string) **REQ** [enum=['Sharing Revoked']] — Represents the response message returned by the API.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the API call. 

- **400**: Returns an error response when the request URL, path parameters, or share entries fail validation. [application/json]
    > Represents the revoke sharing bad request response.
    oneOf:
      - `NoSharingAvailableToRevokeErrorResponse` — Represents the error response returned when no sharing exists for the record through which the revoke operation can be performed.
        - `code` (string) **REQ** [enum=['CANNOT_PROCESS']] — Represents the response code returned by the API.
        - `details` (object) **REQ** — Represents the additional information about the response.
        - `message` (string) **REQ** [enum=['No sharing through this record is available to revoke']] — Represents the response message returned by the API.
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

- **403**: Returns an error response when the user does not have permission to perform the sharing revoke or when the share operation is blocked by an org-level restriction. — Schema: `CommonForbiddenErrorResponse` [application/json]
    > Represents the forbidden error response returned when the user does not have permission to access the API.
    schema: `CommonForbiddenErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the response code returned by the API.
    - `details` (object) **REQ** — Represents the additional information about the response.
    - `message` (string) **REQ** [enum=['permission denied - access the api', 'permission denied']] — Represents the response message returned by the API. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.

**Scopes:** ZohoCRM.share.leads.DELETE, ZohoCRM.share.contacts.DELETE, ZohoCRM.share.accounts.DELETE, ZohoCRM.share.deals.DELETE, ZohoCRM.share.products.DELETE, ZohoCRM.share.tasks.DELETE, ZohoCRM.share.events.DELETE, ZohoCRM.share.calls.DELETE, ZohoCRM.share.quotes.DELETE, ZohoCRM.share.invoices.DELETE, ZohoCRM.share.campaigns.DELETE, ZohoCRM.share.vendors.DELETE, ZohoCRM.share.pricebooks.DELETE, ZohoCRM.share.salesorders.DELETE, ZohoCRM.share.purchaseorders.DELETE, ZohoCRM.share.solutions.DELETE, ZohoCRM.share.cases.DELETE, ZohoCRM.share.bundles.DELETE, ZohoCRM.share.custom.DELETE

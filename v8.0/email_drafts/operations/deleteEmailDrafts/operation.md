# DELETE /{module}/{record}/__email_drafts/{draft}
**Operation:** `deleteEmailDrafts` — Delete an Email Draft
> Deletes the specified email draft for the given record.

**Parameters:**
- `module` (path, string, required) [maxLen=100]: Specifies the module of the record. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the API names of modules.

- `record` (path, string, required) [maxLen=100, pattern=^[0-9]+$]: Specifies the unique identifier of the record. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve record IDs.

- `draft` (path, string, required) [maxLen=256]: Specifies the unique encrypted draft identifier. Use the [Get Email Drafts](email_drafts.yaml#$.paths./{module}/{record}/__email_drafts.get) resource to retrieve draft IDs.


**Responses:**

- **200**: Returns the deletion result when the email draft is deleted successfully. [application/json]
    > Response object containing the result of deleting email drafts.
    - `__email_drafts` (array of object) [maxItems=1] **REQ** — List of deleted email draft results.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Status code for the operation.
      - `message` (string) **REQ** [maxLen=512] — Operation message.
      - `status` (string) **REQ** [enum=['success']] — Status of the operation.
      - `details` (object) **REQ** — Details of the deleted draft.
        - `id` (string) **REQ** [maxLen=256] — Encrypted identifier of the deleted draft.

- **400**: Bad Request - The request could not be processed due to invalid input.

**Resolution:** Verify that the module name is valid, the record ID exists, and the draft ID is correct.
 [application/json]
    > Generic error response for an invalid DELETE request.
    - `code` (string) [maxLen=100, enum=['INVALID_MODULE', 'INVALID_DATA']] — Machine-readable error code.

**Possible values:**
- **INVALID_MODULE** - The specified module is invalid.
- **INVALID_DATA** - The specified record ID or draft ID is invalid.

    - `message` (string) [maxLen=512] — Human-readable error message.
    - `status` (string) [enum=['error']] — Always "error".
    - `details` (object) — Additional context (varies by code).
      - `resource_path_index` (integer/int32) — Index of the invalid path parameter.
      - `id` (string) [maxLen=256] — Encrypted identifier of the draft that could not be deleted.
      additionalProperties: any
    additionalProperties: any

- **403**: Forbidden - the user does not have permission to perform the operation. [application/json]
    > Permission error response returned when the caller lacks required permissions.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code identifying the permission error.
    - `message` (string) **REQ** [maxLen=512] — Human-readable message describing the permission error.
    - `status` (string) **REQ** [enum=['error']] — High-level status of the response.
    - `details` (object) **REQ** — Optional object containing additional details about the error.

**Scopes:** ZohoCRM.modules.leads.DELETE, ZohoCRM.modules.accounts.DELETE, ZohoCRM.modules.contacts.DELETE, ZohoCRM.modules.deals.DELETE, ZohoCRM.modules.quotes.DELETE, ZohoCRM.modules.salesorders.DELETE, ZohoCRM.modules.purchaseorders.DELETE, ZohoCRM.modules.invoices.DELETE, ZohoCRM.modules.vendors.DELETE, ZohoCRM.modules.custom.DELETE, ZohoCRM.modules.cases.DELETE

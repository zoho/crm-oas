# GET /{module}/{record}/__email_drafts
**Operation:** `getEmailDrafts` — List Email Drafts for a Record
> Retrieves the list of email drafts associated with the specified record in the given module.

**Parameters:**
- `module` (path, string, required) [maxLen=100]: Specifies the module of the record. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the API names of modules.

- `record` (path, string, required) [maxLen=100, pattern=^[0-9]+$]: Specifies the unique identifier of the record. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve record IDs.

- `page` (query, integer/int32, optional) [min=1, default=1]: Specifies the page number for pagination. Default:1.
- `per_page` (query, integer/int32, optional) [min=1, max=200, default=200]: Specifies the number of records per page. Default:200.
- `sort_by` (query, string, optional) [enum=['created_time', 'modified_time'], default=created_time]: Field to sort the email drafts by. Default:created_time.
- `sort_order` (query, string, optional) [enum=['asc', 'desc'], default=asc]: Sort direction. Default:asc.

**Responses:**

- **200**: Returns the list of email drafts associated with the specified record. [application/json]
    > Response containing the list of email drafts and pagination info.
    - `__email_drafts` (array of object) [maxItems=100] **REQ** — List of email draft objects.
      - `id` (string) **REQ** [maxLen=256] — Represents the unique encrypted draft identifier. Use this ID to update or delete the draft.

      - `modified_time` (string/date-time) **REQ** — Timestamp when the draft was last modified (ISO 8601 format).
      - `created_time` (string/date-time) **REQ** — Timestamp when the draft was created (ISO 8601 format).
      - `from` (string) **REQ** [maxLen=256] — Sender email address.
      - `to` (array of object) [maxItems=100, nullable] **REQ** — Primary recipients for the draft; null if none.
        - `user_name` (string) **REQ** [maxLen=256, nullable] — Recipient display name; null if not available.
        - `email` (string) **REQ** [maxLen=256] — Recipient email address.
      - `reply_to` (string) **REQ** [maxLen=256, nullable] — Reply-to email address; null if not set.
      - `cc` (array of object) [maxItems=100, nullable] **REQ** — CC recipients for the draft; null if none.
        - `user_name` (string) **REQ** [maxLen=256, nullable] — CC recipient display name; null if not available.
        - `email` (string) **REQ** [maxLen=256] — CC recipient email address.
      - `bcc` (array of object) [maxItems=100, nullable] **REQ** — BCC recipients for the draft; null if none.
        - `user_name` (string) **REQ** [maxLen=256, nullable] — BCC recipient display name; null if not available.
        - `email` (string) **REQ** [maxLen=256] — BCC recipient email address.
      - `schedule_details` (object) — Scheduling information; null if not scheduled.
        - `time` (string/date-time) **REQ** — Scheduled send time in the requesting user's timezone (ISO 8601 format).
        - `timezone` (string) [maxLen=100, nullable] — Timezone identifier (Java TimeZone ID) or null.
        - `source` (string) [enum=[5 values]] — Source of the schedule decision.
      - `subject` (string) **REQ** [maxLen=512, nullable] — Email subject; null if not set.
      - `summary` (string) **REQ** [maxLen=500, nullable] — Plain text preview of the draft body (up to 250 characters); null if empty.
      - `$sharing_permission` (string) [maxLen=64] — Sharing permission level for the requesting user.
      - `rich_text` (boolean) — true when HTML editor was used; false for plain text.
      - `source` (string) [maxLen=256] — Source identifier string stored at draft creation time.
      - `inventory_details` (object) — Inventory email details; null if not an inventory draft.
        - `inventory_template` (object) **REQ** — Inventory template details.
          - `name` (string) **REQ** [maxLen=256] — Inventory template name.
          - `id` (string) **REQ** [maxLen=64] — Inventory template identifier.
        - `paper_type` (string) **REQ** [enum=['A4', 'USLetter']] — Paper type for rendered inventory.
        - `view_type` (string) **REQ** [enum=['portrait', 'landscape']] — Layout/view type for the inventory.
        - `record` (object) — CRM record associated with this inventory draft.
          - `id` (string) **REQ** [maxLen=64] — CRM record identifier.
          - `name` (string) **REQ** [maxLen=256] — CRM record display name.
      - `attachments` (array of object) [maxItems=50, nullable] — Attachments included with the draft; null if none.
        - `id` (string) **REQ** [maxLen=256] — Encrypted attachment/file identifier.
        - `file_name` (string) **REQ** [maxLen=512] — Original file name.
        - `file_size` (string) **REQ** [maxLen=20] — File size in bytes as a numeric string.
        - `service_name` (string) **REQ** [maxLen=100] — Storage service name.
      - `content` (string) [maxLen=200000, nullable] — Email HTML body content; null if not set.
      - `linked_record` (object) — CRM record linked to this draft; null if not linked.
        - `id` (string) **REQ** [maxLen=64] — Linked CRM record identifier.
        - `module` (object) **REQ** — Module of the linked record.
          - `api_name` (string) **REQ** [maxLen=100] — Module API name.
          - `id` (string) [maxLen=64] — Module tab identifier.
      - `owner` (object) **REQ** — Owner who created the draft.
        - `id` (string) **REQ** [maxLen=64] — Owner user identifier. Use the [Users API](users.yaml#$.paths./users/bulk.get) to retrieve user IDs.

        - `name` (string) **REQ** [maxLen=256] — Owner display name.
    - `info` (object) **REQ** — Pagination info for the list response.
      - `page` (integer/int32) **REQ** — Current page number.
      - `per_page` (integer/int32) **REQ** — Number of records per page.
      - `count` (integer/int32) **REQ** — Number of records returned in this page.
      - `more_records` (boolean) **REQ** — true if additional pages exist.

- **204**: Indicates that no email drafts exist for the specified record.

- **400**: Bad Request - The request could not be processed due to invalid input.

**Resolution:** Verify that the module name is valid and the record ID exists in the CRM organization.
 [application/json]
    > Error response for invalid module or record path parameters.
    - `code` (string) [maxLen=100, enum=['INVALID_MODULE', 'INVALID_DATA', 'PATTERN_NOT_MATCHED']] — Machine-readable error code.

**Possible values:**
- **INVALID_MODULE** - The specified module is invalid.
- **INVALID_DATA** - The specified record ID is invalid.
- **PATTERN_NOT_MATCHED** - A query parameter's value does not match its required pattern (e.g. `sort_by`, `sort_order`).

    - `message` (string) [maxLen=512] — Human-readable error message.
    - `status` (string) [enum=['error']] — Always "error".
    - `details` (object) — Additional context about the error.
      - `resource_path_index` (integer/int32) — Index of the invalid path parameter.
      - `param_name` (string) [maxLen=255] — Name of the query parameter whose value failed pattern validation.
      additionalProperties: any
    additionalProperties: any

- **403**: Forbidden - the user does not have permission to perform the operation. [application/json]
    > Permission error response returned when the caller lacks required permissions.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code identifying the permission error.
    - `message` (string) **REQ** [maxLen=512] — Human-readable message describing the permission error.
    - `status` (string) **REQ** [enum=['error']] — High-level status of the response.
    - `details` (object) **REQ** — Optional object containing additional details about the error.

**Scopes:** ZohoCRM.modules.leads.READ, ZohoCRM.modules.accounts.READ, ZohoCRM.modules.contacts.READ, ZohoCRM.modules.deals.READ, ZohoCRM.modules.quotes.READ, ZohoCRM.modules.salesorders.READ, ZohoCRM.modules.purchaseorders.READ, ZohoCRM.modules.invoices.READ, ZohoCRM.modules.vendors.READ, ZohoCRM.modules.custom.READ, ZohoCRM.modules.cases.READ

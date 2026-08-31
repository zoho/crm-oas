# GET /{module}/{record}/__email_drafts/{draft}
**Operation:** `getEmailDraft` — Get an Email Draft
> Retrieves the specified email draft for the given record in the module.

**Parameters:**
- `module` (path, string, required) [maxLen=100]: Specifies the module of the record. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the API names of modules.

- `record` (path, string, required) [maxLen=100, pattern=^[0-9]+$]: Specifies the unique identifier of the record. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve record IDs.

- `draft` (path, string, required) [maxLen=256]: Specifies the unique encrypted draft identifier. Use the [Get Email Drafts](email_drafts.yaml#$.paths./{module}/{record}/__email_drafts.get) resource to retrieve draft IDs.


**Responses:**

- **200**: Returns the details of the specified email draft. [application/json]
    > Response containing a single email draft.
    - `__email_drafts` (array of object) [maxItems=1] **REQ** — Array containing exactly one email draft object.
      - `id` (string) **REQ** [maxLen=256] — Unique encrypted draft identifier.
      - `modified_time` (string/date-time) **REQ** — Timestamp when the draft was last modified (ISO 8601 format).
      - `created_time` (string/date-time) **REQ** — Timestamp when the draft was created (ISO 8601 format).
      - `from` (string) **REQ** [maxLen=256] — Sender email address.
      - `to` (array of object) [maxItems=100, nullable] **REQ** — Primary recipients; null if none.
        - `user_name` (string) **REQ** [maxLen=256, nullable] — Recipient display name; null if not available.
        - `email` (string) **REQ** [maxLen=256] — Recipient email address.
      - `reply_to` (string) **REQ** [maxLen=256, nullable] — Reply-to email address; null if not set.
      - `cc` (array of object) [maxItems=100, nullable] **REQ** — CC recipients; null if none.
        - `user_name` (string) **REQ** [maxLen=256, nullable] — CC recipient display name; null if not available.
        - `email` (string) **REQ** [maxLen=256] — CC recipient email address.
      - `bcc` (array of object) [maxItems=100, nullable] **REQ** — BCC recipients; null if none.
        - `user_name` (string) **REQ** [maxLen=256, nullable] — BCC recipient display name; null if not available.
        - `email` (string) **REQ** [maxLen=256] — BCC recipient email address.
      - `$sharing_permission` (string) [maxLen=64] — Sharing permission level for the requesting user.
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
      - `schedule_details` (object) — Scheduling information; null if not scheduled.
        - `time` (string/date-time) **REQ** — Scheduled send time (ISO 8601 format).
        - `timezone` (string) [maxLen=100, nullable] — Timezone identifier or null.
        - `source` (string) [enum=[5 values]] — Source of the schedule decision.
      - `rich_text` (boolean) **REQ** — true when HTML editor was used; false for plain text.
      - `subject` (string) **REQ** [maxLen=512, nullable] — Email subject; null if not set.
      - `content` (string) **REQ** [maxLen=200000, nullable] — Email HTML body content; null if not set.
      - `summary` (string) **REQ** [maxLen=500, nullable] — Plain text preview of the draft body; null if empty.
      - `owner` (object) **REQ** — Owner who created the draft.
        - `id` (string) **REQ** [maxLen=64] — Owner user identifier. Use the [Users API](users.yaml#$.paths./users/bulk.get) to retrieve user IDs.

        - `name` (string) **REQ** [maxLen=256] — Owner display name.
      - `source` (string) [maxLen=256] — Source identifier string stored at draft creation time.
      - `linked_record` (object) — CRM record linked to this draft; null if not linked.
        - `id` (string) **REQ** [maxLen=64] — Linked CRM record identifier.
        - `module` (object) **REQ** — Module of the linked record.
          - `api_name` (string) **REQ** [maxLen=100] — Module API name.
          - `id` (string) [maxLen=64] — Module tab identifier.

- **204**: Indicates that the specified email draft does not exist, or that the draft ID could not be resolved (e.g. malformed or undecryptable).

- **400**: Bad Request - The request could not be processed due to invalid input.

**Resolution:** Verify that the module name is valid and the record ID exists. A malformed or non-existent draft ID does not return this error — see the `204` response instead.
 [application/json]
    > Generic error response for an invalid GET single-draft request.
    - `code` (string) [maxLen=100, enum=['INVALID_MODULE', 'INVALID_DATA']] — Machine-readable error code.

**Possible values:**
- **INVALID_MODULE** - The specified module is invalid.
- **INVALID_DATA** - The specified record ID is invalid.

    - `message` (string) [maxLen=512] — Human-readable error message.
    - `status` (string) [enum=['error']] — Always "error".
    - `details` (object) — Additional context (varies by code).
      - `resource_path_index` (integer/int32) — Index of the invalid path parameter.
      additionalProperties: any
    additionalProperties: any

- **403**: Forbidden - the user does not have permission to perform the operation. [application/json]
    > Permission error response returned when the caller lacks required permissions.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code identifying the permission error.
    - `message` (string) **REQ** [maxLen=512] — Human-readable message describing the permission error.
    - `status` (string) **REQ** [enum=['error']] — High-level status of the response.
    - `details` (object) **REQ** — Optional object containing additional details about the error.

**Scopes:** ZohoCRM.modules.leads.READ, ZohoCRM.modules.accounts.READ, ZohoCRM.modules.contacts.READ, ZohoCRM.modules.deals.READ, ZohoCRM.modules.quotes.READ, ZohoCRM.modules.salesorders.READ, ZohoCRM.modules.purchaseorders.READ, ZohoCRM.modules.invoices.READ, ZohoCRM.modules.vendors.READ, ZohoCRM.modules.custom.READ, ZohoCRM.modules.cases.READ

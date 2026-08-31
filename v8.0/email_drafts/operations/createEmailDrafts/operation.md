# POST /{module}/{record}/__email_drafts
**Operation:** `createEmailDrafts` — Create Email Drafts for a Record
> Creates one or more email drafts associated with the specified record in the given module.

**Parameters:**
- `module` (path, string, required) [maxLen=100]: Specifies the module of the record. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the API names of modules.

- `record` (path, string, required) [maxLen=100, pattern=^[0-9]+$]: Specifies the unique identifier of the record. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve record IDs.


**Request Body** (required) — application/json
  > Request body for creating email drafts.
  - `__email_drafts` (array of object) [maxItems=100] **REQ** — List of email drafts to create.
    - `from` (string) **REQ** [maxLen=254, pattern=[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}] — Specifies the sender email address. Must be a configured outgoing address for the user. Use the [From Addresses API](from_addresses.yaml#$.paths./settings/emails/actions/from_addresses.get) to retrieve valid from addresses.

    - `to` (array of object) [maxItems=100] — List of primary recipients.
      - `user_name` (string) [maxLen=256, nullable] — Recipient display name; null if not available.
      - `email` (string) **REQ** [maxLen=256] — Recipient email address.
    - `reply_to` (string) [maxLen=256, nullable] — Reply-to email address; null to clear.
    - `cc` (array of object) [maxItems=100] — List of CC recipients.
      - `user_name` (string) [maxLen=256, nullable] — CC recipient display name; null if not available.
      - `email` (string) **REQ** [maxLen=256] — CC recipient email address.
    - `bcc` (array of object) [maxItems=100] — List of BCC recipients.
      - `user_name` (string) [maxLen=256, nullable] — BCC recipient display name; null if not available.
      - `email` (string) **REQ** [maxLen=256] — BCC recipient email address.
    - `inventory_details` (object) — Inventory email details; null if not an inventory draft.
      - `inventory_template` (object) **REQ** — Inventory template to use.
        - `id` (string) **REQ** [maxLen=64] — Inventory template identifier.
      - `paper_type` (string) **REQ** [enum=['A4', 'USLetter']] — Paper type.
      - `view_type` (string) **REQ** [enum=['portrait', 'landscape']] — View type.
    - `schedule_details` (object) — Scheduling details; null to remove schedule.
      - `time` (string/date-time) **REQ** — Scheduled send time (ISO 8601 format).
      - `timezone` (string) [maxLen=100, nullable] — Java TimeZone ID string; null uses organization default.
      - `source` (string) [enum=[5 values]] — Source of the schedule decision.
    - `rich_text` (boolean) **REQ** — true for HTML editor mode; false for plain text mode.
    - `subject` (string) [maxLen=512, nullable] — Email subject; null to clear.
    - `content` (string) [maxLen=200000, nullable] — HTML body when rich_text is true; null to clear.
    - `plainTextContent` (string) [maxLen=200000, nullable] — Plain text body when rich_text is false; null to clear.
    - `source` (string) [maxLen=256] — Source identifier string stored at draft creation time (e.g., campaign name or integration identifier).
    - `linked_record` (object) — CRM record to link this draft to (Contacts module only); null to clear.
      - `id` (string) **REQ** [maxLen=64] — CRM record identifier to link.
      - `module` (object) **REQ** — Module to which the record belongs. Specify at least one of api_name" or "id". If both are specified, they must refer to the same module.
        - `api_name` (string) [maxLen=100] — API name of the module.
        - `id` (string) [maxLen=20] — Tab identifier of the module.
    - `attachments` (array of object) [maxItems=50] — Attachments to add to the draft.
      - `id` (string) **REQ** [maxLen=256] — Attachment/file identifier. Use the [Files API](files.yaml#$.paths./files.get) to retrieve file IDs.

      - `file_name` (string) [maxLen=512] — File name.
      - `file_size` (string) [maxLen=20] — File size in bytes as a numeric string.
      - `service_name` (string) **REQ** [maxLen=100] — Storage service name (e.g., Desktop, ZFSAttached).

**Responses:**

- **201**: Returns the creation results when all email drafts in the request are created successfully. [application/json]
    > Response object containing the result of created email drafts.
    - `__email_drafts` (array of object) [maxItems=100] **REQ** — List of created email draft results.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Status code for the operation.
      - `message` (string) **REQ** [maxLen=512] — Operation message.
      - `status` (string) **REQ** [enum=['success']] — Status of the operation.
      - `details` (object) **REQ** — Details of the created draft.
        - `id` (string) **REQ** [maxLen=256] — Encrypted identifier of the created draft. Use this ID to update or delete the draft.

- **207**: Multi-status response for batch operations with mixed success and error outcomes. [application/json]
    > Response containing per-draft status for mixed batch processing results.
    - `__email_drafts` (array of object) [maxItems=100] **REQ** — Per-draft status results for the submitted batch.
      oneOf:
          - `code` (string) **REQ** [enum=['SUCCESS']] — Operation result code.
          - `details` (object) **REQ** — Details for successful draft operation.
            - `id` (string) **REQ** [maxLen=64] — Updated or created draft identifier.
          - `message` (string) **REQ** [maxLen=512] — Human-readable result message.
          - `status` (string) **REQ** [enum=['success']] — Per-item outcome status.
          - `code` (string) **REQ** [maxLen=128, enum=[8 values]] — Operation error code.

**Possible values:**
- **MANDATORY_NOT_FOUND** - A required field is missing.
- **INVALID_DATA** - The field contains invalid data.
- **NOT_ALLOWED** - The field is not allowed in this operation.
- **DUPLICATE_DATA** - A duplicate value was found (e.g. a duplicate attachment).
- **EXPECTED_FIELD_MISSING** - At least one of a set of expected fields must be specified.
- **AMBIGUITY_DURING_PROCESSING** - The given field values are ambiguous or conflicting.
- **NOT_SUPPORTED** - The given field or value is not supported for this module.
- **DEPENDENT_MISMATCH** - A field value does not match its dependent field.

          - `details` (object) **REQ** — Details for failed draft operation.
            - `api_name` (string) [maxLen=128] — Field or API name that caused the error.
            - `json_path` (string) [maxLen=256] — JSON path for the invalid or missing field.
            additionalProperties: any
          - `message` (string) **REQ** [maxLen=512] — Human-readable error message.
          - `status` (string) **REQ** [enum=['error']] — Per-item outcome status.

- **400**: Bad Request - The request could not be processed due to invalid input.

**Resolution:** Review the error details, correct any invalid fields, and retry the request.
 [application/json]
    > Error response - either a generic request-level error (has top-level code/message/status/details) or a batch validation error (has __email_drafts array with per-draft errors).
    - `code` (string) [maxLen=100, enum=['INVALID_MODULE', 'INVALID_DATA']] — Machine-readable error code for generic errors.

**Possible values:**
- **INVALID_MODULE** - The specified module is invalid.
- **INVALID_DATA** - The specified record ID is invalid.

    - `message` (string) [maxLen=512] — Human-readable error message for generic errors.
    - `status` (string) [enum=['error']] — Always "error".
    - `details` (object) — Additional context for generic errors.
      - `resource_path_index` (integer/int32) — Index of the invalid path parameter.
      additionalProperties: any
    - `__email_drafts` (array of object) [maxItems=100] — Per-draft validation error array (present for batch validation errors).
      - `code` (string) [maxLen=100, enum=[8 values]] — Error code.

**Possible values:**
- **MANDATORY_NOT_FOUND** - A required field is missing.
- **INVALID_DATA** - The field contains invalid data.
- **NOT_ALLOWED** - The field is not allowed in this operation.
- **DUPLICATE_DATA** - A duplicate value was found (e.g. a duplicate attachment).
- **EXPECTED_FIELD_MISSING** - At least one of a set of expected fields must be specified.
- **AMBIGUITY_DURING_PROCESSING** - The given field values are ambiguous or conflicting.
- **NOT_SUPPORTED** - The given field or value is not supported for this module.
- **DEPENDENT_MISMATCH** - A field value does not match its dependent field.

      - `message` (string) [maxLen=512] — Human-readable error message for this draft.
      - `status` (string) [enum=['error']] — Always "error".
      - `details` (object) — Additional context for this draft's error.
        - `api_name` (string) [maxLen=100] — API field name that caused the error.
        - `json_path` (string) [maxLen=256] — JSON path to the offending field.
        additionalProperties: any
      additionalProperties: any
    additionalProperties: any

- **403**: Forbidden - the user does not have permission to perform the operation. [application/json]
    > Permission error response returned when the caller lacks required permissions.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code identifying the permission error.
    - `message` (string) **REQ** [maxLen=512] — Human-readable message describing the permission error.
    - `status` (string) **REQ** [enum=['error']] — High-level status of the response.
    - `details` (object) **REQ** — Optional object containing additional details about the error.

**Scopes:** ZohoCRM.modules.leads.CREATE, ZohoCRM.modules.accounts.CREATE, ZohoCRM.modules.contacts.CREATE, ZohoCRM.modules.deals.CREATE, ZohoCRM.modules.quotes.CREATE, ZohoCRM.modules.salesorders.CREATE, ZohoCRM.modules.purchaseorders.CREATE, ZohoCRM.modules.invoices.CREATE, ZohoCRM.modules.vendors.CREATE, ZohoCRM.modules.custom.CREATE, ZohoCRM.modules.cases.CREATE

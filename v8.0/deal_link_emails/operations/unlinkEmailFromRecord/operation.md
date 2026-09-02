# DELETE /Contacts/{contactId}/Emails/{messageId}/actions/link_record
**Operation:** `unlinkEmailFromRecord` — Unlink Deal Email
> Unlinks an email from a specified record in CRM.

**Parameters:**
- `contactId` (path, string, required) [maxLen=100, pattern=^[0-9]+$]: The ID of the contact to which the email is to be linked or unlinked
- `messageId` (path, string, required) [maxLen=500, pattern=^[a-zA-Z0-9]+$]: The ID of the email message to be linked or unlinked
- `owner_id` (query, string, required) [maxLen=100, pattern=^[0-9]+$]: The ID of the owner of the contact.

**Responses:**

- **200**: success response [application/json]
    > Response schema for unlinking email from record
    - `Emails` (array of object) [maxItems=1] **REQ** — List of email unlink operation results
      - `status` (string) **REQ** [enum=['success']] — Status of the unlink operation
      - `code` (string) **REQ** [enum=['SUCCESS']] — Result code of the unlink operation
      - `message` (string) **REQ** [maxLen=256] — Detailed message about the unlink operation
      - `details` (object) **REQ** — Additional details about the unlink operation
        - `message_id` (string) **REQ** [maxLen=256] — Unique identifier of the email message

- **400**: Bad Request - Invalid input or missing required parameters [application/json]
    > Error response schema for unlinking email from record
    oneOf:
        - `Emails` (array of object) [maxItems=1] **REQ** —  Unique identifier of the module
          oneOf:
              type: array of object [maxItems=1]
                - `status` (string) **REQ** [enum=['error']] — Status of the error
                - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
                - `message` (string) **REQ** [maxLen=256] —  Unique identifier of the message
                - `details` (object) **REQ** —  Unique identifier of the module
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the missing field
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path to the missing field
              type: array of object [maxItems=1]
                - `status` (string) **REQ** [enum=['error']] — Status of the error
                - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
                - `message` (string) **REQ** [maxLen=256, enum=['invalid data']] —  Unique identifier of the message
                - `details` (object) **REQ** —  Unique identifier of the module
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the field with invalid data
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path to the field with invalid data
        - `Emails` (array of object) [maxItems=1] **REQ** —  Unique identifier of the module
          oneOf:
              type: array of object [maxItems=1]
                - `status` (string) **REQ** [enum=['error']] — Status of the error
                - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
                - `message` (string) **REQ** [maxLen=256] —  Unique identifier of the message
                - `details` (object) **REQ** —  Unique identifier of the module
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the missing field
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path to the missing field
              type: array of object [maxItems=1]
                - `status` (string) **REQ** [enum=['error']] — Status of the error
                - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
                - `message` (string) **REQ** [maxLen=256, enum=['invalid data']] —  Unique identifier of the message
                - `details` (object) **REQ** —  Unique identifier of the module
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the field with invalid data
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path to the field with invalid data

**Scopes:** ZohoCRM.modules.contacts.CREATE, ZohoCRM.modules.emails.CREATE, ZohoCRM.modules.deals.CREATE

# POST /Contacts/{contactId}/Emails/{messageId}/actions/link_record
**Operation:** `linkEmailToRecord` — Link Deal Email
> Links an email to a specified record in CRM.

**Parameters:**
- `contactId` (path, string, required) [maxLen=100, pattern=^[0-9]+$]: The ID of the contact to which the email is to be linked or unlinked
- `messageId` (path, string, required) [maxLen=500, pattern=^[a-zA-Z0-9]+$]: The ID of the email message to be linked or unlinked

**Request Body** (required) — application/json
  > Request body schema for linking email to record
  - `Emails` (array of object) [maxItems=1] — List of emails to be linked to records
    - `owner` (object) **REQ** — Owner of the email
      - `id` (string) [maxLen=100, pattern=^[0-9]+$] — Unique identifier of the owner
    - `linked_record` (object) **REQ** — Record to which the email is to be linked
      - `module` (object) **REQ** — Module of the record
        - `api_name` (string) [enum=['Deals']] — API name of the module
        - `id` (string) **REQ** [maxLen=100, pattern=^[0-9]+$] — Unique identifier of the module
      - `name` (string) [maxLen=255] — Name of the record
      - `id` (string) **REQ** [maxLen=100, pattern=^[0-9]+$] — Unique identifier of the record

**Responses:**

- **200**: Successful response [application/json]
    > Response schema for linking email to record
    - `Emails` (array of object) [maxItems=1] **REQ** — List of email link operation results
      - `status` (string) **REQ** [enum=['success']] — Status of the link operation
      - `code` (string) **REQ** [enum=['SUCCESS']] — Result code of the link operation
      - `message` (string) **REQ** [maxLen=256] — Detailed message about the link operation
      - `details` (object) **REQ** — Additional details about the link operation
        - `message_id` (string) **REQ** [maxLen=256] — Unique identifier of the email message

- **400**: Bad Request - Invalid input parameters [application/json]
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

- **404**: Not Found - The specified contact or email does not exist [application/json]
    > Details of not found error
    oneOf:
        - `status` (string) **REQ** [enum=['error']] —  Unique identifier of the module
        - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] —  Unique identifier of the module
        - `message` (string) **REQ** [enum=['Please check if the URL trying to access is a correct one']] —  Unique identifier of the module
        - `details` (object) **REQ** —  Unique identifier of the module
        - `status` (string) **REQ** [enum=['error']] —  Unique identifier of the module
        - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] —  Unique identifier of the module
        - `message` (string) **REQ** [enum=['Please check if the URL trying to access is a correct one']] —  Unique identifier of the module
        - `details` (object) **REQ** —  Unique identifier of the module

**Scopes:** ZohoCRM.modules.contacts.CREATE, ZohoCRM.modules.emails.CREATE, ZohoCRM.modules.deals.CREATE

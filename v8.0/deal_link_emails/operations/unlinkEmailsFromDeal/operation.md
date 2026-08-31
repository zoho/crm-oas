# DELETE /Contacts/{contactId}/Emails/actions/link_record
**Operation:** `unlinkEmailsFromDeal` — Unlink Emails from Deals
> To unlink deals from one or more of a contact's emails. An email will only be linked to a single deal at a time.  When you call this API, the specified email(s) will be unlinked from them. The user's profile requires "View" permission for Deals and Contacts modules to use this API.

**Parameters:**
- `contactId` (path, string, required) [maxLen=100, pattern=^[0-9]+$]: The ID of the contact to which the email is to be linked or unlinked
- `message_ids` (query, string, required) [maxLen=2000, pattern=^[a-zA-Z0-9]+(,[a-zA-Z0-9]+)*$]: The IDs of the email messages to be linked
- `owner_id` (query, string, required) [maxLen=100, pattern=^[0-9]+$]: The ID of the owner of the contact.

**Responses:**

- **200**: The emails were unlinked from the deals successfully. [application/json]
    > Response schema
    - `Emails` (array of object) [maxItems=20] **REQ** — List of email unlink operation results
      - `status` (string) **REQ** [enum=['success']] — Status of the unlink operation
      - `code` (string) **REQ** [enum=['SUCCESS']] — Result code of the unlink operation
      - `message` (string) **REQ** [maxLen=256] — Detailed message about the unlink operation
      - `details` (object) **REQ** — Additional details about the unlink operation
        - `message_id` (string) **REQ** [maxLen=256] — Unique identifier of the email message

- **400**: Bad Request [application/json]
    oneOf:
        - `Emails` (array of object) [maxItems=20] **REQ** — Array of error details for each email unlink operation.
          oneOf:
              type: array of object [maxItems=20]
                - `status` (string) **REQ** [enum=['error']] — Status of the error
                - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
                - `message` (string) **REQ** [maxLen=256] — Error message
                - `details` (object) **REQ** — Object containing additional details about the error.
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the missing field
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path to the missing field
              type: array of object [maxItems=20]
                - `status` (string) **REQ** [enum=['error']] — Status of the error
                - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
                - `message` (string) **REQ** [maxLen=256, enum=['invalid data']] — Error message
                - `details` (object) **REQ** — Object containing additional details about the error.
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the field with invalid data
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path to the field with invalid data
        - `status` (string) **REQ** [enum=['error']] — The status of the response.
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — The error code identifying the type of error.
        - `message` (string) **REQ** [maxLen=256] — A message describing the error.
        - `details` (object) **REQ** — Object containing additional details about the error.
          - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
          - `json_path` (string) **REQ** [maxLen=255] — The JSON path to the field that caused the error.

- **404**: Not Found [application/json]
    > Details of not found error
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — The status of the response.
        - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — The error code identifying the type of error.
        - `message` (string) **REQ** [enum=['Please check if the URL trying to access is a correct one']] — A message describing the error.
        - `details` (object) **REQ** — An empty object. No additional details are provided for this error.
        - `status` (string) **REQ** [enum=['error']] — The status of the response.
        - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — The error code identifying the type of error.
        - `message` (string) **REQ** [enum=['Please check if the URL trying to access is a correct one']] —  Unique identifier of the module
        - `details` (object) **REQ** — An empty object. No additional details are provided for this error.

**Scopes:** ZohoCRM.modules.contacts.CREATE, ZohoCRM.modules.emails.CREATE, ZohoCRM.modules.deals.CREATE

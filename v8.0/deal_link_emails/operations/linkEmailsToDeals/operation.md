# POST /Contacts/{contactId}/Emails/actions/link_record
**Operation:** `linkEmailsToDeals` — Link Emails to Deals
> To link a deal with one or more of a contact's emails. An email can only be linked to a single deal at a time. Zoho CRM automatically links a contact's incoming emails to the deals using the [Deal Prediction Mechanism](https://help.zoho.com/portal/en/kb/crm/connect-with-customers/email/user-functions/articles/email-association-with-deal#Auto-link_Emails_by_Deal_Prediction_Mechanism). You can also manage these links using the Link Deal to Emails API and [Unlink Deal from Emails API](deal_link_emails.yaml#$.paths./Contacts/{contactId}/Emails/{messageId}/actions/link_record.delete).

**Parameters:**
- `contactId` (path, string, required) [maxLen=100, pattern=^[0-9]+$]: The ID of the contact to which the email is to be linked or unlinked

**Request Body** (required) — application/json
> The request body to link emails to deals.
  > The request body schema for linking emails to deals.
  - `Emails` (array of object) [maxItems=20] — Array containing the details of the emails to link to deals. Mandatory.
    - `message_id` (string) **REQ** [maxLen=500, pattern=^[a-zA-Z0-9]+$] — The unique message ID of the email to which the deal will be linked. Mandatory when linking multiple emails. You can obtain message ID of a record through [Get Emails of a Record API](emails.yaml#$.paths.{moduleApiName}/{id}/Emails/{messageId}.get).
    - `owner` (object) **REQ** — The details of the user whose email you want to link. Mandatory.
      - `id` (string) [maxLen=100, pattern=^[0-9]+$] — The unique ID of the user whose email you want to link. Mandatory.
    - `linked_record` (object) **REQ** — The details of the deal record to be linked to the email. Mandatory. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module IDs
      - `module` (object) **REQ** — The details of the Deals module. Mandatory.
        - `api_name` (string) [enum=['Deals']] — The API name of the Deals module. Mandatory.
        - `id` (string) **REQ** [maxLen=100, pattern=^[0-9]+$] — The unique ID of the Deals module. Mandatory.
      - `name` (string) [maxLen=255] — The name of the deal record that the email must be linked to. Mandatory.
      - `id` (string) **REQ** [maxLen=100, pattern=^[0-9]+$] — The unique ID of the deal record that the email must be linked to. Mandatory.

**Responses:**

- **200**: The emails were linked to the deals successfully. [application/json]
    > Successful response containing the link operation results.
    - `Emails` (array of object) [maxItems=20] **REQ** — List of email link operation results
      - `status` (string) **REQ** [enum=['success']] — Status of the link operation
      - `code` (string) **REQ** [enum=['SUCCESS']] — Result code of the link operation
      - `message` (string) **REQ** [maxLen=256] — Detailed message about the link operation
      - `details` (object) **REQ** — Additional details about the link operation
        - `message_id` (string) **REQ** [maxLen=255] — Unique identifier of the email message

- **400**: Bad Request [application/json]
    > Error response schema
    oneOf:
        - `Emails` (array of object) [maxItems=20] **REQ** — List of error details for each email link operation
          oneOf:
              type: array of object [maxItems=20]
                - `status` (string) **REQ** [enum=['error']] — Status of the error
                - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
                - `message` (string) **REQ** [maxLen=256] — Error message
                - `details` (object) **REQ** — Additional details about the error
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the missing field
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path to the missing field
              type: array of object [maxItems=20]
                - `status` (string) **REQ** [enum=['error']] — Status of the error
                - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
                - `message` (string) **REQ** [maxLen=256] — Error message
                - `details` (object) **REQ** — Additional details about the error
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the field with invalid data
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path to the field with invalid data
        - `status` (string) **REQ** [enum=['error']] — Status of the error
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
        - `message` (string) **REQ** [maxLen=256] — Error message
        - `details` (object) **REQ** — Additional details about the error
          - `api_name` (string) **REQ** [maxLen=255] — API name of the missing field
          - `json_path` (string) **REQ** [maxLen=255] — JSON path to the missing field

- **404**: Not Found [application/json]
    > Details of not found error
    - `status` (string) **REQ** [enum=['error']] — Status of the error
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Error code
    - `message` (string) **REQ** [enum=['Please check if the URL trying to access is a correct one']] — Error message
    - `details` (object) **REQ** — Additional details about the error

**Scopes:** ZohoCRM.modules.emails.CREATE, ZohoCRM.modules.deals.CREATE, ZohoCRM.modules.contacts.CREATE

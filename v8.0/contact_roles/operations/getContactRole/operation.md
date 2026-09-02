# GET /Contacts/roles/{role}
**Operation:** `getContactRole` — Get a Contact Role
> Retrieves the details of a specific contact role by its unique identifier in your Zoho CRM organization.

**Parameters:**
- `role` (path, string, required) [maxLen=255]: Specify the unique identifier of the contact role. Use the [List Contact Roles](contact_roles.yaml#$.paths./contacts/roles.get) resource to retrieve contact role IDs.


**Responses:**

- **200**: Returns the details of the specified contact role. [application/json]
    > Contains the details of the specified contact role.
    - `contact_roles` (array of object) [maxItems=100] **REQ** — Represents the details of the specified contact role.
      - `name` (string) **REQ** [maxLen=50, pattern=[A-Za-z0-9 ]] — Represents the name of the contact role.
      - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the contact role.
      - `sequence_number` (number) **REQ** — Represents the display position of the contact role in the CRM UI picklist.

- **204**: Indicates that the specified contact role does not exist in the CRM organization.

**Scopes:** ZohoCRM.modules.contacts.READ

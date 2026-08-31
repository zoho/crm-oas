# GET /Contacts/roles
**Operation:** `getContactRoles` — List Contact Roles
> Retrieves the list of contact roles available in your Zoho CRM organization.

**Responses:**

- **200**: Returns the list of contact roles configured in the CRM organization. [application/json]
    > Contains the list of contact roles configured in the CRM organization.
    - `contact_roles` (array of object) [maxItems=100] **REQ** — Represents the list of contact roles configured in the CRM organization.
      - `name` (string) **REQ** [maxLen=50, pattern=[A-Za-z0-9 ]] — Represents the name of the contact role.
      - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the contact role. Use the [List Contact Roles](contact_roles.yaml#$.paths./contacts/roles.get) resource to retrieve contact role IDs.
      - `sequence_number` (number) **REQ** — Represents the display position of the contact role in the CRM UI picklist.

- **204**: Indicates that no contact roles are configured in the CRM organization.

**Scopes:** ZohoCRM.modules.contacts.READ

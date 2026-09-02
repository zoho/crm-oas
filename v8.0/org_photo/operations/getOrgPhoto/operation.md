# GET /org/photo
**Operation:** `getOrgPhoto` — Organization photo
> To retrieve the organization photo for your Zoho CRM organization.

**Responses:**

- **200**: Returns the organization photo as PNG binary image data. [image/png]
    > Represents the organization photo as PNG binary image data.
    type: string/binary — Represents the organization photo as PNG binary image data.

- **204**: No organization photo is available for this organization.

**Scopes:** ZohoCRM.org.READ

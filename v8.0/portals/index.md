# Portals

- [OpenAPI specification](portals.yaml)
- [Portals](mds/getPortals.md)
  - To retrieve the list of all portals configured for the Zoho CRM organization. A 204 response indicates no portal has been created yet.
  - [Examples](mds/examples/getPortals.md)
- [Portal](mds/createPortal.md)
  - To create a Client Portal for the Zoho CRM organization. Only one portal can be created per organization. The portal name must be unique across Zoho, between 6 and 30 characters.
  - [Examples](mds/examples/createPortal.md)
- [Specific Portal](mds/getPortal.md)
  - To retrieve the complete configuration of a specific portal in the Zoho CRM organization, including its SAML authentication settings, active status, and creation metadata.
  - [Examples](mds/examples/getPortal.md)
- [Portal](mds/updatePortal.md)
  - To update the configuration of an existing portal in the Zoho CRM organization, including the portal name and SAML single sign-on settings.
  - [Examples](mds/examples/updatePortal.md)

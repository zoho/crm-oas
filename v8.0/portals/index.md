# Portals

- [OpenAPI specification](portals.yaml)
- [Portals](operations/getPortals/operation.md)
  - To retrieve the list of all portals configured for the Zoho CRM organization. A 204 response indicates no portal has been created yet.
  - [Examples](operations/getPortals/examples/)
- [Portal](operations/createPortal/operation.md)
  - To create a Client Portal for the Zoho CRM organization. Only one portal can be created per organization. The portal name must be unique across Zoho, between 6 and 30 characters.
  - [Examples](operations/createPortal/examples/)
- [Specific Portal](operations/getPortal/operation.md)
  - To retrieve the complete configuration of a specific portal in the Zoho CRM organization, including its SAML authentication settings, active status, and creation metadata.
  - [Examples](operations/getPortal/examples/)
- [Portal](operations/updatePortal/operation.md)
  - To update the configuration of an existing portal in the Zoho CRM organization, including the portal name and SAML single sign-on settings.
  - [Examples](operations/updatePortal/examples/)

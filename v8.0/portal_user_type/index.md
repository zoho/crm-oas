# Portal User Types

- [OpenAPI specification](portal_user_type.yaml)
- [Portal User Types](operations/getPortalUserTypes/operation.md)
  - Retrieves a list of all portal user types configured for the specified portal, with their summary configuration including name, status, user counts, and last modification time.
  - [Examples](operations/getPortalUserTypes/examples/)
- [Portal User Type](operations/createPortalUserType/operation.md)
  - Creates a new portal user type for the specified portal. A portal user type defines the personality module, invitation field, and per-module access permissions for portal users. The portal must already exist in the organization's Zoho CRM account.
  - [Examples](operations/createPortalUserType/examples/)
- [Portal User Type](operations/getPortalUserType/operation.md)
  - Retrieves the full configuration of a single portal user type, including identity fields, active status, user counts, audit metadata, personality module, invitation field, and per-module access permissions.
  - [Examples](operations/getPortalUserType/examples/)
- [Portal User Type](operations/updatePortalUserType/operation.md)
  - Updates the configuration of an existing portal user type. You can modify module-level access settings, including shared type, allowed layouts, filter fields, and field-level permissions.
  - [Examples](operations/updatePortalUserType/examples/)
- [Delete user type](operations/deletePortalUserType/operation.md)
  - Deletes the specified portal user type from the portal. If portal users are assigned to this user type, provide `transfer_To` with the ID of another user type to transfer them before deletion.
  - [Examples](operations/deletePortalUserType/examples/)

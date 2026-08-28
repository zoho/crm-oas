# Portal User Types

- [OpenAPI specification](portal_user_type.yaml)
- [Portal User Types](mds/getPortalUserTypes.md)
  - Retrieves a list of all portal user types configured for the specified portal, with their summary configuration including name, status, user counts, and last modification time.
  - [Examples](mds/examples/getPortalUserTypes.md)
- [Portal User Type](mds/createPortalUserType.md)
  - Creates a new portal user type for the specified portal. A portal user type defines the personality module, invitation field, and per-module access permissions for portal users. The portal must already exist in the organization's Zoho CRM account.
  - [Examples](mds/examples/createPortalUserType.md)
- [Portal User Type](mds/getPortalUserType.md)
  - Retrieves the full configuration of a single portal user type, including identity fields, active status, user counts, audit metadata, personality module, invitation field, and per-module access permissions.
  - [Examples](mds/examples/getPortalUserType.md)
- [Portal User Type](mds/updatePortalUserType.md)
  - Updates the configuration of an existing portal user type. You can modify module-level access settings, including shared type, allowed layouts, filter fields, and field-level permissions.
  - [Examples](mds/examples/updatePortalUserType.md)
- [Delete user type](mds/deletePortalUserType.md)
  - Deletes the specified portal user type from the portal. If portal users are assigned to this user type, provide `transfer_To` with the ID of another user type to transfer them before deletion.
  - [Examples](mds/examples/deletePortalUserType.md)

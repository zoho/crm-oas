# POST /settings/automation/email_notifications
**Operation:** `postEmailNotifications` — Create Email Notifications
> Creates an email notification action in your Zoho CRM organization by defining its name, associated module, email template, sender details, and recipients. The email notification can be linked to automation rules so that emails are automatically triggered when the specified conditions are met. A pre-existing Email Template is required before creating an email notification; the template ID must be referenced in the request payload.

**Schemas:**
`DirectRecipientEmails`:
  > Represents a recipient configuration that uses explicit email addresses to specify notification targets. Provide one or more addresses in the details.emails array.
  - `type` (string) **REQ** [maxLen=255, enum=['emails']] — Represents the recipient type for this configuration.
Possible values:
emails - Indicates that recipients are specified using explicit email addresses.
  - `details` (object) **REQ** — Represents the details object containing the email addresses for this recipient.
    - `emails` (array of string/email `RecipientEmailAddress`) [minItems=1, maxItems=10] **REQ** — Represents the list of explicit email addresses to notify for this recipient.
      items: [maxLen=255, pattern=^[^\s@]+@[^\s@]+\.[^\s@]+$]
  - `resource` (null) — Represents the resource reference for this recipient type. Not applicable for direct email address recipients.
  - `associated_to` (null) — Represents the associated resource for this recipient type. Not applicable for direct email address recipients.
`DirectRecipientGroup`:
  > Represents a recipient resolved from a CRM user group, used when all members of a group should receive an email notification. Group IDs can be retrieved from the GET /settings/groups endpoint. Not supported in the recipients.to field when bulk_email is true.
  - `type` (string) **REQ** [maxLen=255, enum=['group']] — Represents the recipient type for this group recipient.
Possible values:
group - Indicates that the recipient is resolved from a CRM user group.
  - `resource` (object `ResourceIdentifierGroup`) **REQ** — Group resource (name/id) from Zoho CRM Groups API.
  - `details` (null) — Represents additional recipient details. Not applicable for group recipients.
  - `associated_to` (null) — Represents the associated record for this recipient. Not applicable for group recipients.
`DirectRecipientMergeField`:
  > Represents a recipient resolved dynamically from a merge field, where the recipient address depends on the triggering record and is resolved at runtime. Merge field recipients fall into two categories: INTERNAL — fields resolving to CRM users, such as ${!Module.Owner} or ${!Module.Created_By}, for which from_address must not be provided and defaults to the first registered email address; and EXTERNAL — fields resolving to email-type fields (ui_type=25), such as ${!Module.Email} or ${!Module.Lookup.Email}, for which from_address is required. Use module and field metadata APIs to retrieve valid field API names.
  - `type` (string) **REQ** [maxLen=255, enum=['merge_field']] — Represents the recipient type for this entry.
Possible values:
merge_field - Indicates that the recipient address is resolved dynamically from a record field at runtime.
  - `details` (object) **REQ** — Represents the merge-field details used to resolve the recipient address at runtime, including the field API name and an optional identifier.
    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the merge field used to resolve the recipient address. Sample references: ${!{module_API_name}.{field_API_name}} for direct fields, or ${!{module_API_name}.{lookup_APIname}.{field_API_name}} for lookup fields.
    - `id` (string) [maxLen=255] — Represents the identifier of the merge field used to resolve the recipient.
  - `resource` (null) — Represents the resource associated with the recipient. Not applicable for merge_field recipients; this field is always null.
  - `associated_to` (null) — Represents the associated entity for the recipient. Not applicable for merge_field recipients; this field is always null.
`DirectRecipientProfile`:
  > Represents a notification recipient resolved by a CRM profile, used to notify all users sharing a specific profile or permission level. Refer to the GET /settings/profiles endpoint to retrieve valid profile IDs. For private (team) modules, set the `associated_to` field to `team_module`.
  - `type` (string) **REQ** [maxLen=255, enum=['profile']] — Represents the recipient type for this notification recipient definition.
Possible values:
profile - The recipient is resolved by a CRM profile, notifying all users who share that profile.
  - `resource` (object `ResourceIdentifierProfile`) **REQ** — Profile resource (name/id) from Zoho CRM Profiles API.
  - `details` (null) — Represents additional recipient details. This field is not applicable for profile recipients and is always null.
  - `associated_to` (string) [maxLen=255, enum=['team_module', None], nullable] — Indicates whether the notification module is a private (team) module. Set to `team_module` when the notification targets a private module. Leave null for standard modules.
Possible values:
team_module - The notification module is a private (team) module.
`DirectRecipientRole`:
  > Represents a recipient resolved by a CRM role, used to notify all users assigned to a specific role. The role identifier must be retrieved from the GET /settings/roles endpoint. This recipient type is not supported in the recipients.to field when bulk_email is true.
  - `type` (string) **REQ** [maxLen=255, enum=['role']] — Represents the recipient type for this role-based recipient entry.
Possible values:
role - Identifies the recipient as resolved by a CRM role, sending notifications to all users assigned to that role.
  - `resource` (object `ResourceIdentifierRole`) **REQ** — Role resource (name/id) from Zoho CRM Roles API.
  - `details` (null) — Represents additional details about the recipient. Not applicable for role recipients.
  - `associated_to` (null) — Represents the associated record context for the recipient. Not applicable for role recipients.
`DirectRecipientRoleAndSubordinate`:
  > Represents a recipient resolved from a role and all subordinate roles below it in the hierarchy, used when a notification must reach a manager and everyone reporting under that role. The role ID must be retrieved from the GET /settings/roles endpoint. This recipient type is not supported in recipients.to when bulk_email is true.
  - `type` (string) **REQ** [maxLen=255, enum=['role_and_subordinate']] — Represents the recipient type for this notification target.
Possible values:
role_and_subordinate - Resolves the recipient from a role and all subordinate roles below it in the hierarchy.
  - `resource` (object `ResourceIdentifierRole`) **REQ** — Role resource (name/id) from Zoho CRM Roles API.
  - `details` (null) — Represents additional details for the recipient. Not applicable for role_and_subordinate recipients.
  - `associated_to` (null) — Represents the associated record for this recipient. Not applicable for role_and_subordinate recipients.
`DirectRecipientTerritory`:
  > Represents a recipient resolved from a sales territory in Zoho CRM, used to notify all users assigned to a specific territory. The territory resource ID must be retrieved from the GET /settings/territories endpoint. This recipient type is not supported in the recipients.to field when bulk_email is true.
  - `type` (string) **REQ** [maxLen=255, enum=['territory']] — Represents the recipient type for this territory-based recipient entry.
Possible values:
territory - Indicates that the recipient is resolved from a sales territory, notifying all users assigned to that territory.
  - `resource` (object `ResourceIdentifierTerritory`) **REQ** — Territory resource (name/id) from Zoho CRM Territories API.
  - `details` (null) — Represents additional details for this recipient. Not applicable for territory recipients.
  - `associated_to` (null) — Indicates the associated record for this recipient. Not applicable for territory recipients.
`DirectRecipientTerritoryAndSubterritory`:
  > Represents a recipient resolved from a Territory and all its child sub-territories, used when notifying an entire territory hierarchy. The territory identifier can be retrieved from the Territories API. This recipient type is not supported in recipients.to when bulk_email is true.
  - `type` (string) **REQ** [maxLen=255, enum=['territory_and_subterritory']] — Represents the recipient type for this entry.
Possible values:
territory_and_subterritory - Indicates that the recipient is resolved from a Territory and all its child sub-territories.
  - `resource` (object `ResourceIdentifierTerritory`) **REQ** — Territory resource (name/id) from Zoho CRM Territories API.
  - `details` (null) — Represents additional details for this recipient. Not applicable for territory_and_subterritory recipients.
  - `associated_to` (null) — Represents the associated record for this recipient. Not applicable for territory_and_subterritory recipients.
`DirectRecipientUser`:
  > Represents a recipient resolved from a specific CRM user, used when the notification must be sent to a named individual. Retrieve the user ID from the Get Users endpoint. For private modules, set the `associated_to` field to `team_module` to include team-scoped users.
  - `type` (string) **REQ** [maxLen=255, enum=['user']] — Represents the recipient type for the notification target. For direct user recipients, this value is always `user`.
Possible values:
user - The recipient is a specific CRM user identified by their user ID.
  - `resource` (object `ResourceIdentifierUser`) **REQ** — User resource (name/id) from Zoho CRM Users API.
  - `details` (null) — Represents additional details for the recipient. Not applicable for user recipients.
  - `associated_to` (string) [maxLen=255, enum=['team_module', None], nullable] — Indicates the scope context for recipient resolution. Set to `team_module` when the notification module is a private module where record visibility is restricted to team members. When set, only team-scoped users and profiles are included. Leave null for standard modules.
Possible values:
team_module - The notification module is a private (team) module; only team-scoped users and profiles are included as recipients.
null - The notification module is a standard module; all applicable users and profiles are included.
`DirectRecipients`:
  discriminator: `type`
    merge_field → #/components/schemas/DirectRecipientMergeField
    emails → #/components/schemas/DirectRecipientEmails
    user → #/components/schemas/DirectRecipientUser
    profile → #/components/schemas/DirectRecipientProfile
    group → #/components/schemas/DirectRecipientGroup
    role → #/components/schemas/DirectRecipientRole
    role_and_subordinate → #/components/schemas/DirectRecipientRoleAndSubordinate
    territory → #/components/schemas/DirectRecipientTerritory
    territory_and_subterritory → #/components/schemas/DirectRecipientTerritoryAndSubterritory
  oneOf:
    - `DirectRecipientMergeField` — Represents a recipient resolved dynamically from a merge field, where the recipient address depends on the triggering record and is resolved at runtime. Merge field recipients fall into two categories: INTERNAL — fields resolving to CRM users, such as ${!Module.Owner} or ${!Module.Created_By}, for which from_address must not be provided and defaults to the first registered email address; and EXTERNAL — fields resolving to email-type fields (ui_type=25), such as ${!Module.Email} or ${!Module.Lookup.Email}, for which from_address is required. Use module and field metadata APIs to retrieve valid field API names.
    - `DirectRecipientEmails` — Represents a recipient configuration that uses explicit email addresses to specify notification targets. Provide one or more addresses in the details.emails array.
    - `DirectRecipientUser` — Represents a recipient resolved from a specific CRM user, used when the notification must be sent to a named individual. Retrieve the user ID from the Get Users endpoint. For private modules, set the `associated_to` field to `team_module` to include team-scoped users.
    - `DirectRecipientProfile` — Represents a notification recipient resolved by a CRM profile, used to notify all users sharing a specific profile or permission level. Refer to the GET /settings/profiles endpoint to retrieve valid profile IDs. For private (team) modules, set the `associated_to` field to `team_module`.
    - `DirectRecipientGroup` — Represents a recipient resolved from a CRM user group, used when all members of a group should receive an email notification. Group IDs can be retrieved from the GET /settings/groups endpoint. Not supported in the recipients.to field when bulk_email is true.
    - `DirectRecipientRole` — Represents a recipient resolved by a CRM role, used to notify all users assigned to a specific role. The role identifier must be retrieved from the GET /settings/roles endpoint. This recipient type is not supported in the recipients.to field when bulk_email is true.
    - `DirectRecipientRoleAndSubordinate` — Represents a recipient resolved from a role and all subordinate roles below it in the hierarchy, used when a notification must reach a manager and everyone reporting under that role. The role ID must be retrieved from the GET /settings/roles endpoint. This recipient type is not supported in recipients.to when bulk_email is true.
    - `DirectRecipientTerritory` — Represents a recipient resolved from a sales territory in Zoho CRM, used to notify all users assigned to a specific territory. The territory resource ID must be retrieved from the GET /settings/territories endpoint. This recipient type is not supported in the recipients.to field when bulk_email is true.
    - `DirectRecipientTerritoryAndSubterritory` — Represents a recipient resolved from a Territory and all its child sub-territories, used when notifying an entire territory hierarchy. The territory identifier can be retrieved from the Territories API. This recipient type is not supported in recipients.to when bulk_email is true.
`EmailNotificationAddressMergeField`:
  > Represents the address configuration for a merge_field type from or reply-to address in an email notification. Two hardcoded values are always available: ${!Current.User.Email} (the logged-in user's email) and ${!Record.Owner.Email} (the record owner's email). Any user lookup field available in the module can also be used as a from or reply-to address, for example, ${!Deals.Contact_Name.Email}. Use module and field metadata APIs to discover available user lookup fields.
  - `type` (string) **REQ** [maxLen=255, enum=['merge_field']] — Represents the address type for this configuration.
Possible values:
merge_field - Indicates the address is resolved dynamically from a CRM module field or user lookup field.
  - `details` (object) **REQ** — Represents the merge field details used to resolve the sender or reply-to address. The api_name property is required for merge_field address types.
    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the merge field used to resolve the sender or reply-to address. Supported reference formats include ${!{module_API_name}.{field_API_name}} for direct fields and ${!{module_API_name}.{lookup_APIname}.{field_API_name}} for lookup fields.
    - `id` (string) [maxLen=255] — Represents the optional identifier for the merge field.
  - `resource` (null) — Represents the resource field, which is not applicable for merge_field address types and must be set to null.
`EmailNotificationAddressOrganizationEmail`:
  > Represents the address configuration for an organization email sender in an email notification. The resource.id must be an organization email ID retrieved from Zoho CRM Organization APIs.
  - `type` (string) **REQ** [maxLen=255, enum=['organization_email']] — Represents the address type for the email notification sender configuration.
Possible values:
organization_email - Indicates that the sender address is an organization email registered in the Zoho CRM organization.
  - `resource` (object `ResourceIdentifierOrganizationEmail`) **REQ** — Organization email resource. Use resource.id from Zoho CRM Organization APIs.
  - `details` (null) — Represents additional details for the address configuration. This field is not applicable when the type is organization_email.
`EmailNotificationAddressUser`:
  > Represents the address configuration for a Zoho CRM user recipient in an email notification. The resource.id must be a valid CRM user ID from the Zoho CRM Users APIs.
  - `type` (string) **REQ** [maxLen=255, enum=['user']] — Represents the address type for the email notification recipient configuration.
Possible values:
user - Indicates that the recipient address is resolved from a Zoho CRM user.
  - `resource` (object `ResourceIdentifierUser`) **REQ** — User resource. Use resource.id from Zoho CRM Users APIs.
  - `details` (null) — Represents additional address details. This field is not applicable when the type is set to `user` and should be omitted or set to null.
`ResourceIdentifierGroup`:
  > Group resource (name/id) from Zoho CRM Groups API.
  - `name` (string) [maxLen=255] — Represents the display name of the group. This field is informational only and is not used to resolve the record.
  - `id` (string) **REQ** [maxLen=255] — Represents the unique numeric identifier of the group. Refer to the [Get user groups](user_groups.yaml#$.paths./settings/user_groups.get) endpoint for details.
`ResourceIdentifierOrganizationEmail`:
  > Organization email resource. Use resource.id from Zoho CRM Organization APIs.
  - `name` (string) [maxLen=255] — Represents the display name of the organization email. This field is informational only and is not used by the API to resolve the record.
  - `id` (string) **REQ** [maxLen=255] — Represents the unique numeric identifier of the organization email. Refer to the [Organization Email](organization_emails.yaml#$.paths./settings/emails/org_emails.post) endpoint for details.
`ResourceIdentifierProfile`:
  > Profile resource (name/id) from Zoho CRM Profiles API.
  - `name` (string) [maxLen=255] — Represents the display name of the profile. This value is informational only and is not used by the API to resolve the record.
  - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]{1,19}$] — Represents the unique numeric identifier of the profile. Refer to the [Profiles](profiles.yaml#$.paths./settings/profiles.get) endpoint for details.
`ResourceIdentifierRole`:
  > Role resource (name/id) from Zoho CRM Roles API.
  - `name` (string) [maxLen=255] — Represents the display name of the role. This field is informational only and is not used to resolve the record.
  - `id` (string) **REQ** [maxLen=255] — Represents the unique numeric identifier of the role. Refer to the [Get all roles](roles.yaml#$.paths./settings/roles.get) endpoint for details.
`ResourceIdentifierTerritory`:
  > Territory resource (name/id) from Zoho CRM Territories API.
  - `name` (string) [maxLen=255] — Represents the display name of the Territory. This value is informational only; the API uses the id field to resolve the Territory record.
  - `id` (string/int64) **REQ** [maxLen=255] — Represents the unique numeric identifier of the Territory. Refer to the [Get all territories](territories.yaml#$.paths./settings/territories.get) endpoint for details.
`ResourceIdentifierUser`:
  > User resource (name/id) from Zoho CRM Users API.
  - `name` (string) [maxLen=255] — Represents the display name of the user. This value is informational only; the API uses the id field to resolve the user record.
  - `id` (string) **REQ** [maxLen=255] — Represents the unique numeric identifier of the user. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.

**Request Body** — application/json `CreateEmailNotificationsRequest`
> The request body must contain an email_notifications array with one object.
  > Represents the request body wrapper for creating an email notification action. The body must contain an email_notifications array with exactly one object.
  - `email_notifications` (array of object `EmailNotificationCreateInput`) [maxItems=1] **REQ** — Specify the email notification objects to create. The array must contain exactly one object.
    schema: `EmailNotificationCreateInput`
    - `name` (string) **REQ** [maxLen=255] — Specify the display name of the email notification action. The following special characters are not allowed: ~`#%^&*()+={}[]|;"<>\.
    - `module` (object `ModuleDetails`) **REQ** — Primary CRM module whose records trigger this email notification (e.g., Leads, Contacts, Deals). Both api_name and id are required. If they mismatch, returns AMBIGUITY_DURING_PROCESSING. This value cannot be changed after creation. Use GET /settings/modules to discover available modules.
      schema: `ModuleDetails`
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM module whose records trigger the email notification. For example, Leads, Contacts, or Deals. Both api_name and id must refer to the same module.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique numeric identifier of the CRM module. Both id and api_name must refer to the same module.
    - `related_module` (object `RelatedModuleDetails`) — Related module context for this notification configuration (e.g., Notes as related module for a Leads notification). This value cannot be changed after creation. Pass null when not applicable.
      schema: `RelatedModuleDetails`
      - `api_name` (string) [maxLen=255] — Represents the API name of the related CRM module used in the automation configuration, for example, Notes.
      - `id` (string) [maxLen=255] — Represents the unique identifier of the related CRM module that corresponds to the api_name value.
    - `template` (object `EmailTemplate`) **REQ** — Email template to be used for this notification action. Both name and id are required. Fetch available templates from the Email Templates API for the configured module. If no template exists yet for that module, create one first via the createEmailTemplate tool and then associate it here. Templates containing Consent or Survey links are not supported for mass emails; do not use a template containing these links when bulk_email is set to true.
      schema: `EmailTemplate`
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the email template associated with the email notification.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the email template.
    - `recipients` (object `EmailRecipients`) **REQ** — Recipients of the email notification. Provide a JSON object with three arrays: to (required, at least one entry), cc (optional), and bcc (optional). CC and BCC are only allowed when bulk_email is true.
      schema: `EmailRecipients`
      - `to` (array of object `DirectRecipients`) [minItems=1, maxItems=100] **REQ** — Represents the primary recipients of the email notification. At least one recipient entry is required.
      - `cc` (array of object `DirectRecipients`) [maxItems=50] — Represents the CC recipients of the email notification. Supported only when bulk_email is set to true.
      - `bcc` (array of object `DirectRecipients`) [maxItems=50] — Represents the BCC recipients of the email notification. Supported only when bulk_email is set to true.
    - `from_address` (object `FromAddress`) — Sender (From) address. Supported types: merge_field, user, organization_email. When bulk_email is false, the From address defaults to notifications@zohocrm.com for notifications sent to internal CRM users; from_address must not be specified in this case and doing so returns DEPENDENT_MISMATCH. When bulk_email is true, the configured From address is used instead of notifications@zohocrm.com, and the From address is required for mass emails.
      discriminator: `type`
        merge_field → #/components/schemas/EmailNotificationAddressMergeField
        user → #/components/schemas/EmailNotificationAddressUser
        organization_email → #/components/schemas/EmailNotificationAddressOrganizationEmail
        email → #/components/schemas/EmailNotificationAddressEmails
      oneOf:
        - `EmailNotificationAddressMergeField` — Represents the address configuration for a merge_field type from or reply-to address in an email notification. Two hardcoded values are always available: ${!Current.User.Email} (the logged-in user's email) and ${!Record.Owner.Email} (the record owner's email). Any user lookup field available in the module can also be used as a from or reply-to address, for example, ${!Deals.Contact_Name.Email}. Use module and field metadata APIs to discover available user lookup fields.
        - `EmailNotificationAddressUser` — Represents the address configuration for a Zoho CRM user recipient in an email notification. The resource.id must be a valid CRM user ID from the Zoho CRM Users APIs.
        - `EmailNotificationAddressOrganizationEmail` — Represents the address configuration for an organization email sender in an email notification. The resource.id must be an organization email ID retrieved from Zoho CRM Organization APIs.
        - `EmailNotificationAddressEmails` — Represents the sender address configuration for an email notification, used when the server assigns the address automatically or when the address resolves to a plain email address.
          - `type` (string) **REQ** [maxLen=255, enum=['email']] — Represents the type of sender address for the notification.
Possible values:
email - The sender address resolves to a plain email address.
          - `details` (object) **REQ** — Represents the email details for the sender address associated with the notification.
            - `email` (object) **REQ** — Represents the sender email address in the local@domain format.
              schema: `RecipientEmailAddress`
              type: string/email [maxLen=255, pattern=^[^\s@]+@[^\s@]+\.[^\s@]+$] — Represents an email address in local@domain format, used for direct recipient and sender configurations.
          - `resource` (null) — Represents the resource reference for the sender address. This field is not applicable when the address type is email.
    - `reply_to_address` (object `ReplyToAddress`) — Reply-to address. Supported types: merge_field, user, organization_email. When all recipients are internal CRM users, reply_to_address must not be specified and doing so returns DEPENDENT_MISMATCH. Required when any recipient resolves to an external email.
      oneOf:
        - `EmailNotificationAddressMergeField` — Represents the address configuration for a merge_field type from or reply-to address in an email notification. Two hardcoded values are always available: ${!Current.User.Email} (the logged-in user's email) and ${!Record.Owner.Email} (the record owner's email). Any user lookup field available in the module can also be used as a from or reply-to address, for example, ${!Deals.Contact_Name.Email}. Use module and field metadata APIs to discover available user lookup fields.
        - `EmailNotificationAddressUser` — Represents the address configuration for a Zoho CRM user recipient in an email notification. The resource.id must be a valid CRM user ID from the Zoho CRM Users APIs.
        - `EmailNotificationAddressOrganizationEmail` — Represents the address configuration for an organization email sender in an email notification. The resource.id must be an organization email ID retrieved from Zoho CRM Organization APIs.
        - `EmailNotificationAddressNull` (null) — Represents a null address value, indicating that no sender or reply-to address has been configured for the email notification.
    - `bulk_email` (boolean) [default=False] — Indicates whether mass email mode is enabled for this notification. When set to true, CC and BCC recipients are allowed in the recipients object; when omitted or set to false, including CC or BCC recipients returns an AMBIGUITY_DURING_PROCESSING error. When true, role, group, territory, role_and_subordinate, and territory_and_subterritory recipient types cannot be specified in the recipients.to array; use individual users or email addresses instead. This value cannot be changed after creation.
Possible values:
true - Mass email mode is enabled; CC and BCC recipients are permitted.
false - Mass email mode is disabled; CC and BCC recipients are not permitted.
    - `feature_type` (string) [maxLen=255, enum=[13 values]] — Automation feature this email notification belongs to. Defaults to 'workflow' if omitted. All listed values are supported for creation via API.

**Responses:**

- **201**: Returns the unique identifier of the newly created email notification action. — Schema: `CreateEmailNotificationSuccessResponse` [application/json]
    > Represents the response returned when an email notification is successfully created in the Zoho CRM organization.
    schema: `CreateEmailNotificationSuccessResponse`
    - `email_notifications` (array of object `CreateEmailNotificationSuccessItem`) [maxItems=1] **REQ** — Represents the list of email notification objects created in the request. Contains one item representing the successfully created email notification.
      schema: `CreateEmailNotificationSuccessItem`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the email notification creation operation.
Possible values:
SUCCESS - The email notification action was created successfully.
      - `details` (object `CreateEmailNotificationSuccessDetails`) **REQ** — Identifier details returned for the created email notification action.
        schema: `CreateEmailNotificationSuccessDetails`
        - `id` (string) **REQ** [maxLen=20] — Unique identifier of the newly created email notification action.
      - `message` (string) **REQ** [maxLen=255] — Represents the success message returned after the email notification action is created.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the email notification creation operation.
Possible values:
success - The email notification action was created successfully.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request contains invalid or missing data. Resolution: The request must include all mandatory fields with valid values. The module API name and ID must refer to the same module, the email_notifications array must not exceed one object, and recipient details must be complete and correctly formatted. [application/json]
    > Represents the error response returned when the create email notification request fails validation. The structure varies depending on the specific validation error encountered.
    additionalProperties: any
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **401**: Insufficient privileges to perform this operation. Resolution: The user do not have permission to perform this action. Contact your administrator. — Schema: `UnauthorizedError` [application/json]
    > Represents an unauthorized error response returned when the user lacks the required privilege to perform the requested operation.
    schema: `UnauthorizedError`
    - `code` (string) **REQ** [enum=['unauthorized']] — Represents the error code indicating the authorization failure.
Possible values:
unauthorized - The request lacks valid authorization credentials to perform this operation.
    - `details` (object) **REQ** — Represents additional details about the authorization error.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the authorization failure.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response, indicating that an error occurred.
Possible values:
error - The request was not processed due to an authorization failure.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to create an email notification. Resolution: The CRM administrator must grant the manage workflow permission to the user's profile. — Schema: `PermissionDeniedError` [application/json]
    > Represents an error response returned when the requesting user lacks the necessary permissions to perform the operation.
    schema: `PermissionDeniedError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code indicating the reason the request was denied.
Possible values:
NO_PERMISSION - The requesting user does not have the required permission to perform this operation.
    - `details` (object) **REQ** — Represents an object containing additional details about the permission denial, including the specific permissions that were missing.
      - `permissions` (array of string) [maxItems=25] — Represents the list of permissions that the requesting user lacks for the attempted operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the reason the requested operation was denied.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
error - Indicates that the request failed due to insufficient permissions.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.automation_actions.CREATE

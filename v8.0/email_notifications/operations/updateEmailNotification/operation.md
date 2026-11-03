# PUT /settings/automation/email_notifications/{id}
**Operation:** `updateEmailNotification` — Update an Email Notification by ID
> Updates an existing email notification in your Zoho CRM organization.

**Parameters:**
- `id` (path, string, required) [maxLen=20]: Specify the unique ID of the email notification to update.

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

**Request Body** — application/json `UpdateEmailNotificationRequest`
> The request body must contain an email_notifications array with one object.
  > Represents the request body wrapper for updating an email notification action. The body must contain an email_notifications array with exactly one object.
  - `email_notifications` (array of object `EmailNotificationUpdateInput`) [maxItems=1] **REQ** — Specify the email notification object to update. The array must contain exactly one object with the fields to modify.
    schema: `EmailNotificationUpdateInput`
    - `name` (string) **REQ** [maxLen=255] — Specify the display name of the email notification action. Special characters ~`#%^&*()+={}[]|;"<>\ are not allowed.
    - `template` (object `EmailTemplate`) **REQ** — Email template to be used for this notification action. Both name and id are required. Fetch available templates from the Email Templates API. If no template exists yet for that module, create one first via the createEmailTemplate tool and then associate it here.
      schema: `EmailTemplate`
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the email template associated with the email notification.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the email template.
    - `recipients` (object `EmailRecipients`) **REQ** — Recipients of the email notification. Provide a JSON object with three arrays: to (required, at least one entry), cc (optional), and bcc (optional). CC and BCC are only allowed when bulk_email is true (set during creation).
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

**Responses:**

- **200**: Returns the result of the email notification update, including the ID of the updated notification and a success status. — Schema: `UpdateEmailNotificationSuccessResponse` [application/json]
    > Represents the successful response returned after updating an email notification definition in Zoho CRM. Contains the updated email notification details in the email_notifications array.
    schema: `UpdateEmailNotificationSuccessResponse`
    - `email_notifications` (array of object `NewEmailNotificationResponse`) [maxItems=1] — Represents the list of updated email notification definitions. Contains one object with the details of the email notification that was updated.
      schema: `NewEmailNotificationResponse`
      - `code` (string) [maxLen=255] — Represents the status code returned after the email notification is created successfully.
      - `details` (object `ResponseDetails`) — Represents the details of a recipient or sender entry in an email notification definition, including the email address, merge field API name, and merge field identifier.
        schema: `ResponseDetails`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the merge field. Applicable only when the type is merge_field.
        - `email` (string) [maxLen=255] — Represents the email address associated with the recipient or sender in the notification definition.
        - `api_name` (string) [maxLen=100] — Represents the API name of the merge field used to resolve the email address dynamically. For example: ${!Deals.Contact_Name.Email}. Applicable only when the type is merge_field.
      - `message` (string) [maxLen=255] — Represents the message describing the outcome of the email notification creation request.
      - `status` (string) [maxLen=255] — Represents the status of the email notification creation operation, indicating whether the request was successful.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request contains invalid or missing data. Resolution: The request must be corrected by providing valid values for all required fields, including a valid module name, correct recipient details, and a valid email notification name without special characters. [application/json]
    > Represents the error response payload returned when the update email notification request fails due to a validation error.
    additionalProperties: any
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **401**: The email notification cannot be updated because it is locked or associated with a restricted automation. Resolution: The CRM administrator must verify that the email notification is not associated with CommandCenter or a marketplace extension before attempting to update it. [application/json]
    > Represents the error response payload returned when the update email notification request is rejected due to an authorization failure.
    - `email_notifications` (array of object) [maxItems=25] **REQ** — Represents the list of error objects returned for the update email notification request.
      oneOf:
        - `MandatoryFieldMissingError` — Represents an error response returned when a required field is missing from the request.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code indicating that a required field is missing from the request.
Possible values:
MANDATORY_NOT_FOUND - The request is missing a mandatory field.
          - `details` (object) **REQ** — Represents the details of the validation error, including the API name and JSON path of the missing mandatory field.
            - `api_name` (string) [maxLen=255] — Represents the API name of the mandatory field that is missing from the request.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the missing mandatory field within the request body.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing mandatory field.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
error - Indicates that the request failed due to a missing mandatory field.
        - `InvalidModuleError` — Represents the error response returned when the module name provided in the request is not recognized or does not exist in the Zoho CRM organization.
          - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code indicating the nature of the module validation failure.
Possible values:
INVALID_MODULE - The specified module name is not recognized or does not exist in the CRM organization.
          - `details` (object) **REQ** — Represents additional details about the invalid module error, including the API name and JSON path of the parameter that failed validation.
            - `api_name` (string) [maxLen=255] — Represents the API name of the module parameter that triggered the invalid module error.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path of the request parameter that caused the invalid module error.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the module name provided in the request is invalid.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for an invalid module error.
Possible values:
error - Indicates the request failed due to an invalid module name.
        - `AmbiguityInModuleError` — Represents an error response returned when an ambiguity related to a module is detected during processing.
          - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code indicating that an ambiguity was encountered during module processing.
Possible values:
AMBIGUITY_DURING_PROCESSING - An ambiguity was detected while processing the module-related request.
          - `details` (object) **REQ** — Represents the error details containing information about the ambiguities detected during module processing.
            - `ambiguity_due_to` (array of object) [maxItems=25] — Represents the list of items that caused the ambiguity during module processing.
              - `api_name` (string) [maxLen=255] — Represents the API name of the field or module that caused the ambiguity.
              - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field or property that caused the ambiguity during processing.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the ambiguity encountered during module processing.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for this error.
Possible values:
error - Indicates that the request failed due to an ambiguity detected during module processing.
        - `InvalidRecipientsError` — Represents an error response returned when one or more user-specified recipients in the request are not valid, including details about each erroneous entry such as the field API name, JSON path, and individual error codes.
          - `code` (string) **REQ** [enum=['MULTIPLE_OR_MULTI_ERRORS']] — Represents the error code identifying the type of recipient validation failure.
Possible values:
MULTIPLE_OR_MULTI_ERRORS - Indicates that multiple recipient validation errors were encountered in the request.
          - `details` (object) **REQ** — Represents the validation details associated with the recipient error, including the field name, JSON path, and a list of individual error entries.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field associated with the recipient validation error.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request payload that contains the invalid recipient value.
            - `error` (array of object) [maxItems=25] — Represents the list of individual recipient validation errors encountered in the request.
              - `code` (string) [maxLen=255] — Represents the error code identifying the specific type of validation failure for the recipient entry.
              - `details` (object) — Represents the additional details for the individual recipient validation error, including the field API name and JSON path of the erroneous entry.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field for which the recipient validation error occurred.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the specific field in the request payload where the recipient validation error occurred.
              - `message` (string) [maxLen=255] — Represents the error message describing the reason the recipient entry failed validation.
              - `status` (string) [maxLen=255] — Represents the status of the individual recipient validation error.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the specified recipients are invalid.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response.
Possible values:
error - Indicates that the request failed due to invalid recipients.
        - `InvalidAssociatedToError` — Represents the error response returned when an associated_to field value in the request is invalid, including the field API name, JSON path, and the list of supported values.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating the nature of the validation failure.
Possible values:
INVALID_DATA - The associated_to field value in the request is invalid or does not match the expected format.
          - `details` (object) **REQ** — Represents the details of the validation error, including the field API name, JSON path, and the list of supported values for the associated_to field.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field in the request for which the associated_to validation failed.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field in the request body for which the associated_to validation failed.
            - `supported_values` (array of string) [maxItems=25] — Represents the list of valid values supported for the associated_to field that failed validation.
              items: [maxLen=255]
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the associated_to field value in the request is invalid.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response indicating the outcome of the request.
Possible values:
error - The request failed due to an invalid associated_to field value.
        - `DependentMismatchError` — Represents an error response returned when a request parameter's value conflicts with or violates a dependency condition defined by another parameter.
          - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code identifying a dependency mismatch in the request parameters.
Possible values:
DEPENDENT_MISMATCH - The request contains a parameter whose value conflicts with or violates a dependency condition defined by another parameter.
          - `details` (object) **REQ** — Represents the error details describing the dependency mismatch, including the API names and JSON paths of the affected parameters.
            - `dependee` (object) — Represents the details of the dependee parameter — the parameter on which the mismatched parameter depends — including its API name and JSON path.
              - `api_name` (string) [maxLen=255] — Represents the API name of the dependee parameter involved in the dependency mismatch.
              - `json_path` (string) [maxLen=1000] — Represents the JSON path to the dependee parameter within the request payload.
            - `api_name` (string) [maxLen=255] — Represents the API name of the request parameter that caused the dependency mismatch.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the request parameter that caused the dependency mismatch.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the dependency mismatch that occurred.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
error - Indicates that the request failed due to a dependency mismatch in the request parameters.
        - `InvalidTemplateIdError` — Represents the error response returned when a request contains an invalid or unrecognized email template ID, including the error code, status, message, and details about the field that caused the failure.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating the nature of the failure.
Possible values:
INVALID_DATA - The request contains an invalid or unrecognized email template ID.
          - `details` (object) **REQ** — Represents an object containing additional details about the validation error, including the API name and JSON path of the field that caused the failure.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field associated with the invalid template ID error.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request payload that caused the invalid template ID error.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid template ID issue encountered during the request.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for this error.
Possible values:
error - Indicates that the request failed due to an invalid template ID.
        - `InvalidAddressError` — Represents the error response returned when the request contains an invalid email address or configuration, such as an invalid from or to parameter.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating the nature of the failure.
Possible values:
INVALID_DATA - The request contains an invalid email address or configuration value.
          - `details` (object) **REQ** — Represents an object containing additional validation details about the invalid address or configuration field that caused the error.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the invalid email address or configuration value.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the specific field in the request payload that contains the invalid email address or configuration value.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid email address or configuration issue encountered in the request.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for this error.
Possible values:
error - Indicates that the request failed due to an invalid email address or configuration.
        - `InvalidNameError` — Represents an error response returned when a submitted name contains characters that are not allowed in Zoho CRM.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating the type of naming validation failure.
Possible values:
INVALID_DATA - The submitted data contains a name with characters that are not allowed.
          - `details` (object) **REQ** — Represents the details of the naming validation error, including the API name and JSON path of the field that contains the invalid characters.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field for which the invalid name error was raised.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains the invalid name.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the naming validation failure.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for the naming validation error.
Possible values:
error - Indicates that the request failed due to an invalid name.
        - `NameLengthExceededError` — Represents the error response returned when the length of a specified name exceeds the defined character limit.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating the nature of the failure.
Possible values:
INVALID_DATA - The request contains invalid data, such as a name that exceeds the allowed character limit.
          - `details` (object) **REQ** — Represents the details of the validation error, including the field API name, the JSON path of the invalid field, and the maximum character limit that was exceeded.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field for which the name length limit was exceeded.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body for which the name length limit was exceeded.
            - `maximum_limit` (integer/int32) — Represents the maximum number of characters allowed for the field name that was exceeded in the request.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the request failed.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for this error.
Possible values:
error - Indicates that the request failed due to the name length exceeding the allowed limit.
        - `BulkEmailCCError` — Represents the error response returned when bulk email settings incorrectly configure CC or BCC details while the bulk email option is disabled.
          - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code identifying the type of ambiguity encountered during processing.
Possible values:
AMBIGUITY_DURING_PROCESSING - An ambiguity was detected while processing the bulk email CC or BCC configuration.
          - `details` (object) **REQ** — Represents the error details containing information about the fields that caused the ambiguity during bulk email CC or BCC configuration.
            - `ambiguity_due_to` (array of object) [maxItems=25] — Represents the list of fields that caused the ambiguity during bulk email CC or BCC configuration processing.
              - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the ambiguity during bulk email CC or BCC configuration processing.
              - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that caused the ambiguity during bulk email CC or BCC configuration processing.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the ambiguity encountered during bulk email CC or BCC configuration processing.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response, indicating that an error occurred.
Possible values:
error - The request resulted in an error due to ambiguous CC or BCC configuration in bulk email settings.
        - `LockedNotificationEditError` — Represents the error response returned when an attempt is made to edit a locked email notification, indicating an authorization error.
          - `code` (string) **REQ** [enum=['AUTHORIZATION_ERROR']] — Represents the error code indicating the type of error that occurred.
Possible values:
AUTHORIZATION_ERROR - The request was rejected because the email notification is locked and cannot be edited.
          - `details` (object) **REQ** — Represents the additional details associated with the authorization error for the locked email notification.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the email notification could not be edited.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for the locked notification edit attempt.
Possible values:
error - Indicates that the request failed due to an authorization error.
        - `InvalidDataTypeError` — Represents the error response returned when the recipient configuration in the `to` field includes only record-based recipients (such as the record owner, the owner's manager, or the created-by user) and a `from_address` or `reply_to_address` cannot be associated with that configuration.
          - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code identifying the type of dependency conflict.
Possible values:
DEPENDENT_MISMATCH - The specified recipient configuration conflicts with the from_address or reply_to_address settings.
          - `details` (object) **REQ** — Represents the error details identifying the field and its dependent field that caused the configuration conflict.
            - `dependee` (object) — Represents the dependent field whose configuration conflicts with the primary field identified in the error.
              - `api_name` (string) [maxLen=255] — Represents the API name of the dependent field that conflicts with the primary field configuration.
              - `json_path` (string) [maxLen=1000] — Represents the JSON path to the dependent field within the request payload.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the dependency conflict.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field within the request payload that caused the dependency conflict.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the dependency conflict between the recipient configuration and the sender or reply-to address settings.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
error - Indicates that the request failed due to a dependency conflict in the configuration.
        - `DependentFieldMissingError` — Represents the error response returned when a dependent field conflict is detected in the request, such as when bulk email is enabled and a role or group is specified as a recipient in the 'to' field.
          - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code indicating the nature of the dependency mismatch.
Possible values:
DEPENDENT_MISMATCH - The request contains a dependent field conflict, such as associating a role or group as a recipient when bulk email is enabled.
          - `details` (object) **REQ** — Represents the details of the validation error, identifying the fields involved in the dependency conflict.
            - `dependee` (object) — Represents the field whose value is required to be present for the dependent field to be valid.
              - `api_name` (string) [maxLen=255] — Represents the API name of the dependee field involved in the dependency conflict.
              - `json_path` (string) [maxLen=1000] — Represents the JSON path of the dependee field within the request payload where the dependency conflict was detected.
            - `dependent_field` (object) — Represents the field that has a dependency on another field and caused the validation error.
              - `api_name` (string) [maxLen=255] — Represents the API name of the dependent field that triggered the dependency conflict.
              - `json_path` (string) [maxLen=1000] — Represents the JSON path of the dependent field within the request payload where the conflict originated.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the dependency conflict that occurred.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
error - Indicates that the request failed due to a dependency conflict.
        - `InvalidResourceIdentifierError` — Represents the error response returned when the request contains an invalid resource identifier. The response includes an error code, a descriptive message, and a details object with the API name, expected data type, and JSON path of the field that failed validation.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of validation failure.
Possible values:
INVALID_DATA - The request contains invalid data for the specified resource identifier.
          - `details` (object) **REQ** — Represents an object containing additional details about the invalid resource identifier, including the API name, expected data type, and JSON path of the field that failed validation.
            - `expected_data_type` (string) [maxLen=255] — Represents the data type that was expected for the field identified in the error, as determined by the API schema.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field or parameter for which the invalid resource identifier error was triggered.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request payload for which the invalid resource identifier error was triggered.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the resource identifier in the request was considered invalid.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
error - Indicates that the request failed due to an invalid resource identifier.
        - `InvalidApiNameError` — Represents the error response returned when a submitted API name is invalid or does not meet the required format. Contains the error code, status, message, and details including the invalid API name, its JSON path in the request payload, and the maximum allowed length.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating the type of validation failure.
Possible values:
INVALID_DATA - The submitted API name contains invalid data or does not meet the required format.
          - `details` (object) **REQ** — Represents the details of the validation error, including the invalid API name, its location in the request payload, and the maximum allowed length.
            - `maximum_length` (integer/int32) — Represents the maximum character length allowed for the invalid API name field.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field or parameter that failed validation.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field in the request payload that caused the validation error.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid API name validation failure.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
error - Indicates that the request failed due to an invalid API name.
        - `MissingRequiredFieldError` — Represents the error response returned when a required field is missing from the request. The response includes the error code, a message describing the missing field, and details identifying the field's API name and its JSON path in the request body.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code indicating that a required field is missing from the request.
Possible values:
MANDATORY_NOT_FOUND - A required field was not found in the request.
          - `details` (object) **REQ** — Represents an object containing additional details about the missing required field, including the field API name and its JSON path in the request.
            - `api_name` (string) [maxLen=255] — Represents the API name of the required field that is missing from the request.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path within the request body that identifies the location of the missing required field.
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing required field that caused the request to fail.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for this error.
Possible values:
error - Indicates that the request failed due to a missing required field.
        - `ResourceIdentifierLengthExceededError` — Represents the error response returned when a request contains a resource identifier that exceeds the allowed length, resulting in an INVALID_DATA error.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating the type of validation failure.
Possible values:
INVALID_DATA - The request contains invalid data, such as a resource identifier that exceeds the allowed length.
          - `details` (object) **REQ** — Represents additional details about the validation error, including the API name, JSON path, and supported values related to the invalid data.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field or resource for which the identifier length validation failed.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field in the request payload where the identifier length validation error occurred.
            - `supported_values` (array of string) [maxItems=25] — Represents the list of supported values for the field that failed validation.
              items: [maxLen=255]
          - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the reason the request failed due to an invalid data condition.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for this error.
Possible values:
error - Indicates that the request failed due to invalid data.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.automation_actions.UPDATE

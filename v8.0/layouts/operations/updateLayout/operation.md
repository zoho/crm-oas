# PATCH /settings/layouts/{id}
**Operation:** `updateLayout` — Update a custom layout
> To update a custom layout in your Zoho CRM organization, including renaming it, modifying profile permissions, enabling or disabling the business card display, and creating, updating, or deleting sections and fields within sections.

**Tags:** Layouts

**Parameters:**
- `id` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Specify the unique identifier of the layout. Refer to the [Get Layouts](layouts.yaml#$.paths./settings/layouts.get) resource for valid values.
- `module` (query, string, required) [maxLen=50]: Specify the API name of the required module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.

**Schemas:**
`DeleteObject`:
  > Delete configuration for removing the field. Set permanent to false to move to unused section (can be re-added later), true to permanently delete the field and its data.
  - `permanent` (boolean) **REQ** — Indicates whether the resource is removed irrecoverably or placed in the recycle bin for potential recovery. Possible values: `true` — the resource is permanently destroyed and cannot be restored; `false` — the resource is moved to trash and may be recovered before final purge.
`ErrorDetails`:
  > Contains additional context-specific details accompanying an API error response, providing structured diagnostics such as the offending parameter name, expected data type, supported values, or dependency information.
  - `param_name` (string) [maxLen=100] — Identifies the specific request parameter whose value or absence triggered the error, enabling targeted correction of the offending input.
  - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Resource ID related to the error, if applicable.
  - `expected_data_type` (string) [maxLen=50] — Indicates the data type that the API expects for the parameter that failed validation, enabling callers to correct the value format before retrying the request.
  - `supported_values` (array of string) [maxItems=10] — Contains the discrete values accepted for the parameter identified in the error, providing a reference set to correct the offending request.
    items: [maxLen=100]
  - `dependee` (object) — Contains structured information about the controlling parameter whose presence or value is required before the missing dependent parameter becomes valid or applicable.
    - `param_name` (string) [maxLen=100] — Identifies the API parameter name of the dependee — the controlling parameter that must be supplied or satisfied to make the associated dependent parameter applicable in the request.
  - `resource_path_index` (integer/int32) — Indicates the zero-based position within a multi-segment URL path at which the invalid or unrecognised segment was detected, helping to locate the exact portion of the resource path that caused the error.
  - `permissions` (array of string) [maxItems=20] — Contains the set of OAuth permission scopes that must be granted to the authenticating user or application before the requested action can be completed. Returned when the request is denied due to insufficient permissions.
    items: [maxLen=100]
  additionalProperties: any
`ErrorResponse`:
  > Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.
  - `code` (string) **REQ** [enum=[11 values]] — Identifies the category of error returned by the API. Possible values: `REQUIRED_PARAM_MISSING` — a mandatory parameter was absent from the request; `DEPENDENT_PARAM_MISSING` — a parameter required by another supplied parameter was not provided; `INVALID_MODULE` — the specified module does not exist or is not accessible; `INVALID_DATA` — one or more field values failed validation; `NOT_SUPPORTED` — the requested operation is not supported for the target resource; `NOT_ALLOWED` — the operation is not permitted in the current context; `AUTHENTICATION_FAILURE` — the supplied credentials could not be verified; `OAUTH_SCOPE_MISMATCH` — the OAuth token does not carry the scope required for the operation; `INVALID_REQUEST_METHOD` — the HTTP method used is not accepted by the endpoint; `INTERNAL_ERROR` — an unexpected server-side failure occurred; `NO_PERMISSION` — the authenticated user lacks the CRM profile permission needed to perform the action.
  - `details` (object `ErrorDetails`) **REQ** — Contains additional context-specific details accompanying an API error response, providing structured diagnostics such as the offending parameter name, expected data type, supported values, or dependency information.
  - `message` (string) **REQ** [maxLen=1000] — Contains a short, descriptive explanation of the error condition, providing context that supplements the structured error code.
  - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the request. Possible values: `error` — the request did not complete successfully and the response body contains error details.

**Request Body** (required) — application/json `UpdateLayoutRequest`
> The request body must contain a layouts array with one object. You can include a maximum of five sections per request, with no more than five fields in total across all sections.
  > Represents the request body for updating a layout, containing exactly one layout object with the configuration changes to apply.
  - `layouts` (array of object `LayoutUpdateObject`) [minItems=1, maxItems=1] **REQ** — Contains exactly one layout object defining the update operations to be applied, including sections, profiles, and display settings.
    schema: `LayoutUpdateObject`
    - `name` (string) [maxLen=255, minLen=1] — Represents the new display name for the layout. Must be unique within the module's layout configurations.
    - `show_business_card` (boolean) — Specifies whether the business card view is enabled or disabled for this layout as part of the update.
    - `profiles` (array of object `ProfileUpdateObject`) [minItems=1, maxItems=50] — Contains the array of profile objects to be added to or removed from the layout's profile associations in this update operation.
      schema: `ProfileUpdateObject`
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the profile.
      - `_delete` (boolean) — Indicates whether this profile's association with the layout should be removed. Possible values: `true` — the profile is disassociated from the layout; `false` — the profile association is retained or added.
    - `sections` (array of object `SectionUpdateObject`) [minItems=1, maxItems=5] — Contains the array of section objects to be created, modified, or deleted as part of this layout update, defining the field and configuration changes within each section.
      schema: `SectionUpdateObject`
      - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the section. Required for updating or deleting existing sections. Omit when creating a new section.
      - `name` (string) [maxLen=255, minLen=1] — Represents the internal API name of the section. Required when creating a new section through a layout update.
      - `display_label` (string) [maxLen=255, minLen=1] — Represents the heading label of the section as displayed in the CRM interface. Required when creating a new section.
      - `sequence_number` (integer/int32) [min=1, max=100] — Indicates the one-based ordinal position of the section within the layout, controlling the order in which sections are rendered.
      - `tab_traversal` (string) [enum=['left_to_right', 'top_to_bottom']] — Specifies the tab key navigation direction within the section. Defines how focus moves between fields when users press Tab. Possible values: `left_to_right` — focus moves horizontally across columns first. `top_to_bottom` — focus moves vertically down each column first.
      - `column_count` (integer/int32) [min=1, max=2] — Indicates the number of columns in which fields are arranged within this section when the layout is rendered on record forms.
      - `fields` (array of object `FieldUpdateObject`) [minItems=1, maxItems=25] — Contains the array of field operations to perform within this section, including adding, updating, creating, or removing field entries.
        schema: `FieldUpdateObject`
        - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of an existing field. Required when adding, updating position, or removing an existing field. Omit when creating a new custom field.
        - `field_label` (string) [maxLen=255, minLen=1] — Represents the display label shown for the field in the CRM interface. Required when creating a new custom field through a layout update.
        - `data_type` (string) [enum=[28 values]] — Represents the data type of the field. Required when adding a new custom field to the layout. Possible values: `text`, `textarea`, `email`, `phone`, `website`, `integer`, `bigint`, `currency`, `double`, `percent`, `date`, `datetime`, `boolean`, `picklist`, `multiselectpicklist`, `lookup`, `multiselectlookup`, `autonumber`, `fileupload`, `imageupload`, `formula`, `rollup_summary`, `consent_lookup`, `profileimage`, `richtextarea`, `userlookup`, `multiuserlookup`, `event_reminder`.
        - `length` (integer/int32) [min=1, max=32000] — Represents the maximum number of characters permitted for this field's value. Applicable to text and textarea field types.
        - `sequence_number` (integer/int32) [min=1] — Represents the one-based ordinal position of the field within its containing section, controlling the rendering order of fields on record forms.
        - `element_type` (string) [enum=['field', 'mirror_field']] — Represents the element type for special field components in the layout, distinguishing standard data fields from mirror fields. Possible values: `field` — a standard data field. `mirror_field` — a field that mirrors a value from a lookup source.
        - `lookup_field` (object) — Represents the source lookup field from which a mirror field derives its value, establishing the cross-module field reference for mirror field creation.
          - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the source lookup field.
          - `api_name` (string) [maxLen=100] — Represents the API name of the source lookup field on which this mirror field is based.
        - `_delete` (object `DeleteObject`) — Delete configuration for removing the field. Set permanent to false to move to unused section (can be re-added later), true to permanently delete the field and its data.
        - `association_details` (object `PatchAssociationDetails`) — Association details for Field-Of-Lookup (FOL) mapping. Links this field to a related field in another module through a lookup field.
          oneOf:
              - `related_field` (object) **REQ** — Represents the related field on the associated module used to complete the lookup association, identifiable by its ID or API name.
                - `api_name` (string) [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
              - `lookup_field` (object) **REQ** — Represents the lookup field used to establish the association, identifiable by its ID, API name, or a combination of both.
                - `api_name` (string) [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Represents an API identifier string composed of alphanumeric characters and underscores, used as a programmatic reference for fields, modules, and other CRM entities.
                - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents a unique numeric identifier for a CRM entity, expressed as a 64-bit integer serialized as a string to preserve precision in JSON.
                - `reference_id` (string) [maxLen=255, pattern=\{\{[a-zA-Z0-9]+\}\}] — Represents a temporary identifier used to reference a section or element within a layout update request payload, enabling cross-referencing between newly created elements before their permanent IDs are assigned.
            - `TypeNull` (null) — Represents a null value used in `oneOf` schemas where a property may be absent or explicitly set to null.
      - `_delete` (object `DeleteObject`) — Delete configuration for removing the section. When provided, the section identified by id will be deleted.
      additionalProperties: any

**Responses:**

- **200**: Returns a layouts array containing the result of the update operation, including a SUCCESS status code and the ID of the updated layout. — Schema: `UpdateLayoutSuccessResponse` [application/json]
    > Represents the successful response returned when a layout update operation completes, containing the per-layout update results.
    schema: `UpdateLayoutSuccessResponse`
    - `layouts` (array of object `LayoutUpdateSuccessResult`) [minItems=1, maxItems=1] **REQ** — Contains the array of result entries for the layout update operation, each reporting the outcome for an individual layout.
      schema: `LayoutUpdateSuccessResult`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the success code returned when the layout update operation completes without error.
      - `details` (object) **REQ** — Contains the identifying details of the layout that was successfully updated, such as its ID.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the updated layout.
      - `message` (string) **REQ** [maxLen=255] — Contains a confirmation message indicating that the layout update operation completed successfully.
      - `status` (string) **REQ** [enum=['success']] — Indicates the outcome of the layout update operation. Possible values: `success` — the layout update completes successfully.

- **400**: Invalid data or parameters in the request. **Resolution:** The caller must verify that the layout ID, module name, and all required fields and section identifiers in the request body are valid and present. — Schema: `UpdateLayoutErrorResponse` [application/json]
    > Represents the error response returned for layout update operations that fail, containing either a wrapped per-layout error array or a top-level error code and message.
    schema: `UpdateLayoutErrorResponse`
    - `layouts` (array of object `LayoutUpdateErrorResult`) [minItems=1, maxItems=1] — Contains the array of layout-specific error results for batch layout update operations that encountered failures.
      schema: `LayoutUpdateErrorResult`
      - `code` (string) **REQ** [enum=[11 values]] — Represents the error classification code returned for a failed layout update operation. Possible values: `INVALID_DATA` — a field value fails validation. `MANDATORY_NOT_FOUND` — a required field is absent. `NOT_ALLOWED` — the operation is not permitted for this field. `LIMIT_EXCEEDED` — a maximum count or size limit was exceeded. `DUPLICATE_DATA` — a duplicate value was detected. `EXPECTED_FIELD_MISSING` — a conditionally required field is absent. `DEPENDENT_FIELD_MISSING` — a dependent field required by another field is not provided. `DEPENDENT_MISMATCH` — a dependent field's value does not match the expected configuration. `NOT_SUPPORTED` — the operation is not supported for this field type. `FEATURE_NOT_SUPPORTED` — the requested feature is not available. `AMBIGUITY_DURING_PROCESSING` — conflicting references prevent unambiguous processing.
      - `details` (object `LayoutUpdateErrorDetails`) **REQ** — Represents the structured error details for a layout update failure, providing diagnostic information such as the offending field's JSON path and API name, dependency violations, ambiguity sources, limit breaches, and expected field constraints.
        schema: `LayoutUpdateErrorDetails`
        - `api_name` (string) [maxLen=100] — Represents the API name of the field whose value or configuration caused the layout update error.
        - `json_path` (string) [maxLen=500] — Represents the JSON path to the field within the layout update request payload that caused the error, enabling precise identification of the offending input.
        - `expected_data_type` (string) [maxLen=50] — Indicates the data type that the API expected for the field that failed validation during the layout update.
        - `maximum_length` (integer/int32) — Indicates the maximum character length allowed for the field that failed validation during the layout update.
        - `limit` (integer/int32) — Indicates the maximum allowed value or count that was exceeded during the layout update, providing the threshold value for the violated constraint.
        - `dependee` (object) — Contains information about the dependent field that caused a mismatch or dependency violation during the layout update operation.
          - `api_name` (string) [maxLen=100] — Represents the API name of the dependent field involved in the layout update dependency error.
          - `json_path` (string) [maxLen=500] — Represents the JSON path to the dependent field within the layout update request payload.
        - `limit_due_to` (array of object) [maxItems=10] — Contains the list of fields responsible for causing a limit to be exceeded during the layout update, identifying which fields contributed to the constraint violation.
          - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contributed to exceeding the layout update limit.
          - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field within the layout update request payload that contributed to exceeding the limit.
        - `ambiguity_due_to` (array of object) [maxItems=10] — Contains the list of fields that caused an ambiguity error during layout update processing, identifying conflicting or duplicate field references in the request.
          - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contributed to the layout update ambiguity error.
          - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field within the layout update request payload that contributed to the ambiguity error.
        - `expected_fields` (array of object) [maxItems=10] — Contains the list of fields of which at least one must be provided for the layout update to proceed, describing a conditional required field constraint.
          - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the expected field that is missing from the layout update request.
          - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the expected field within the layout update request payload.
        additionalProperties: any
      - `message` (string) **REQ** [maxLen=1000] — Contains a descriptive explanation of the error encountered during the layout update operation.
      - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the layout update operation. Possible values: `error` — the operation did not complete successfully.
    - `code` (string) [maxLen=255] — Represents the error classification code returned for layout update failures that are not wrapped in a layout-specific error array.
    - `details` (object `ErrorDetails`) — Contains additional context-specific details accompanying an API error response, providing structured diagnostics such as the offending parameter name, expected data type, supported values, or dependency information.
    - `message` (string) [maxLen=255] — Contains a descriptive explanation of the layout update error that occurred.
    - `status` (string) [enum=['error']] — Indicates the outcome of the layout update operation. Possible values: `error` — the operation did not complete successfully.

- **401**: Unauthorized response returned when authentication fails or the provided credentials are invalid or missing. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.

- **403**: Permission denied. **Resolution:** The user does not have permission to update the layout. The administrator must grant the required CRM profile permissions. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.

- **405**: The HTTP request method is not valid for this endpoint. **Resolution:** The caller must specify a valid HTTP request method for the API URL. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.

- **500**: Internal server error response returned when an unexpected failure occurs on the server side while processing the request. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.

**Scopes:** ZohoCRM.settings.layouts.UPDATE

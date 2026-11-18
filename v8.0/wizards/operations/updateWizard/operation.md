# PATCH /settings/wizards/{id}
**Operation:** `updateWizard` — Wizard
> Updates the specified wizard including screens, containers, field configurations, and rules - based on the data provided in the request.

**Parameters:**
- `id` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+$]: Specify the unique ID of the wizard to retrieve or delete.

**Request Body** (required) — application/json
> Provide the wizard configuration to update, including containers, screens, segments, buttons, and conditional rules.
  > Request body to update an existing wizard configuration.
  - `wizards` (array of object) [maxItems=1] **REQ** — List of wizard definitions to be updated. Only one wizard can be updated per request.
    - `module` (object) — Module information for which the wizard is configured. Either api_name or id must be provided.
      - `api_name` (string) [maxLen=50] — API name of the module. Any valid module API name is allowed.
      - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the module.
      anyOf:
          additionalProperties: any
          additionalProperties: any
    - `name` (string) [maxLen=30] — Unique name of the wizard used in the API.
    - `portal_user_types` (array of object) [maxItems=500] — Client portal user types that are allowed to access the wizard.
      - `name` (string) [maxLen=255] — Internal name of the portal user type.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the portal user type.
      - `_delete` (boolean) — Specify `true` to remove this existing portal user type from the wizard.
    - `profiles` (array of object) [maxItems=500] — Profiles allowed to access the wizard.
      - `name` (string) [maxLen=255] — Name of the profile.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Numeric unique identifier of the profile.
      - `_delete` (boolean) — Specify `true` to remove this existing profile from the wizard.
    - `active` (boolean) — Indicates whether the wizard is active.
    - `containers` (array of object) [maxItems=7] — Containers that bind a layout to its wizard screens and chart definition.
      - `_delete` (boolean) — Specify `true` to delete this existing container.
      - `layout` (object) **REQ** — Layout from which wizard fields are sourced.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Numeric unique identifier of the layout.
        - `name` (string) [maxLen=50] — Name of the layout. Ignored for resolution, used only for readability.
        - `_delete` (boolean) — Specify `true` to remove this layout binding from the container.
      - `chart_data` (object) — Metadata representing the visual flow between screens in the wizard.
        - `nodes` (array of object) [maxItems=75] **REQ** — Visual nodes representing screens in the wizard flow.
          - `pos_x` (integer/int32) **REQ** — X-coordinate (in pixels) of the node on the canvas.
          - `pos_y` (integer/int32) **REQ** — Y-coordinate (in pixels) of the node on the canvas.
          - `start_node` (boolean) **REQ** — Indicates whether this node is the starting screen in the flow.
          - `screen` (object) **REQ** — Screen represented by this node. Must refer to an existing screen or a new one in the same payload.
            - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the screen.
            - `reference_id` (string) [maxLen=50, pattern=\{\{[a-zA-Z0-9]+\}\}] — Temporary identifier used to reference a screen that is created or updated in the same request.
            - `display_label` (string) [maxLen=255] — Display label of the screen.
            oneOf:
                additionalProperties: any
                additionalProperties: any
        - `connections` (array of object) [maxItems=75] — Connections between source button and target screens in the wizard flow.
          - `source_button` (object) **REQ** — Button from which the connection originates.
            - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the button.
            - `reference_id` (string) [maxLen=50, pattern=\{\{[a-zA-Z0-9]+\}\}] — Temporary identifier used to reference a button created in the same payload.
            - `display_label` (string) [maxLen=255] — Display label of the button.
            oneOf:
                additionalProperties: any
                additionalProperties: any
          - `target_screen` (object) **REQ** — Target screen node in the wizard flow that this connection points to. Either an existing screen (`id`) or a temporary screen (`reference_id`) must be provided.
            - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the target screen.
            - `reference_id` (string) [maxLen=50, pattern=\{\{[a-zA-Z0-9]+\}\}] — Temporary identifier used to reference a target screen that is created or updated in the same request.
            - `display_label` (string) [maxLen=255] — Display label of the target screen.
            oneOf:
                additionalProperties: any
                additionalProperties: any
        - `color_palette` (object) — Color palette used in the wizard canvas.
          - `button_background` (array of string) [maxItems=10] — List of hex color values used for button backgrounds.
            items: [maxLen=7]
      - `screens` (array of object) [maxItems=75] — Screens included in this container for the wizard.
        - `display_label` (string) [maxLen=255] — Display label of the screen.
        - `reference_id` (string) [maxLen=50, pattern=\{\{[a-zA-Z0-9]+\}\}] — Temporary identifier used to reference this screen within this request.
        - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the screen.
        - `_delete` (boolean) — Specify `true` to delete this existing screen. Applicable only when `id` (an existing screen) is provided.
        - `segments` (array of object) [maxItems=75] — Segments that group fields, text, and buttons on the screen.
          - `_delete` (boolean) — Specify `true` to delete this existing segment. Applicable only when referencing an existing segment via `reference_id`.
          - `sequence_number` (integer/int32) **REQ** — Sequence in which the segment appears within the screen.
          - `display_label` (string) [maxLen=255] — Display label of the segment.
          - `type` (string) **REQ** [maxLen=50, enum=['composite', 'fields', 'subforms', 'text_label', 'widget', 'buttons']] — Type of segment, for example 'composite', 'text_label', or 'buttons'.
          - `reference_id` (string) [maxLen=50, pattern=\{\{[a-zA-Z0-9]+\}\}] — Internal reference identifier used to map this segment within the same request.
          - `name` (string) [maxLen=255] — Name of the segment (used for text_label and buttons segments).
          - `content` (string) [maxLen=2000] — Static content, used for text_label segments.
          - `tab_traversal` (string) [enum=['left_to_right', 'top_to_bottom']] — Specify the tab traversal direction for keyboard navigation within this segment (legacy layout only).

Possible values:
- `left_to_right` - Tab moves through elements from left to right.
- `top_to_bottom` - Tab moves through elements from top to bottom.
          - `elements` (array of object) [maxItems=200] — Field elements inside this segment. Present for composite segments.
            - `sequence_number` (integer/int32) — Sequence in which the element appears within the segment.
            - `type` (string) **REQ** [maxLen=50, enum=['field', 'query_component', 'segment']] — Type of the element, for example 'field'.
            - `resource` (object) **REQ** — Resource referenced by this element.
              - `name` (string) [maxLen=255] — API name of the resource.
              - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the resource.
          - `fields` (array of object) [maxItems=75] — Specify the list of fields to include in this segment. For `fields`-type segments, specify `id` directly on the item (only numeric `id` is accepted; `api_name` is not supported for updates). For `subforms`-type segments, specify `id`/`api_name` directly on the item.
            oneOf:
                - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the field.
                - `sequence_number` (integer/int32) — Specify the sequence number that determines the position of this field within the segment. Required when adding this field to the segment for the first time.
                - `_delete` (boolean) — Specify `true` to remove this field from the segment.
                - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the field.
                - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the field.
                - `sequence_number` (integer/int32) — Specify the sequence number that determines the position of this field within the segment.
          - `buttons` (array of object) [maxItems=50] — Buttons displayed inside this segment. Present for buttons segments.
            - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the button.
            - `reference_id` (string) [maxLen=50, pattern=\{\{[a-zA-Z0-9]+\}\}] — Internal reference identifier used to map this button within the same request.
            - `display_label` (string) [maxLen=255] — Display label of the button.
            - `sequence_number` (integer/int32) — Sequence of the button within the segment.
            - `shape` (string) [enum=['square', 'capsule', 'round']] — Shape of the button.
            - `background_color` (string) [maxLen=7] — Background color of the button (hex value).
            - `color` (string) [maxLen=7] — Text color of the button (hex value).
            - `type` (string) [enum=['save', 'transition']] — Type of button action.
            - `category` (string) [enum=['wizard_button', 'custom_button']] — Category of the button.
            - `visibility` (string) [enum=['hide', 'disable', 'show']] — Visibility behavior of the button.
            - `target_screen` (object) — Target screen navigated to when this button is clicked. Must reference an existing screen or a new one in the same request.
            - `profiles` (array) [maxItems=500] — Profiles for which this button is applicable.
            - `resource` (object) [nullable] — Specify the resource associated with the button, if any.
            - `criteria` (object) — Specify the criteria controlling the visibility or behavior of this button.
            - `message` (object) — Specify the message configuration to show when this button performs a save action.
            - `transition` (object) — Specify additional transition configuration for the button, if any.
            - `show_summary_on` (string) [enum=['create', 'create_and_edit', None], nullable] — Specify the event on which a summary screen is shown after this button action.

Possible values:
- `create` - Show the summary when creating a record.
- `edit` - Show the summary when editing a record.
- `create_and_edit` - Show the summary on both create and edit.
            - `_delete` (boolean) — Specify `true` to delete this existing button. Applicable only when `id` (an existing button) is provided.
            oneOf:
                additionalProperties: any
                additionalProperties: any
          - `widget` (object) — Widget resource linked to this segment. Required when type is 'widget'.
            - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the widget.
            - `name` (string) [maxLen=255] — Name of the widget.
        - `conditional_rules` (array of object) [maxItems=50] — Conditional rules evaluated on this screen.
          - `query_id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Specify the unique numeric identifier of an existing conditional rule to update in place. Omit this to add a new conditional rule.
          - `_delete` (boolean) — Specify `true` to delete this existing conditional rule. Applicable only when `query_id` is provided.
          - `execute_on` (string) [maxLen=50] — Event on which the rule executes, for example 'create_edit'.
          - `criteria` (object) — Criteria expression evaluated for this rule.
            - `comparator` (string) **REQ** [maxLen=50] — Comparator used in the criteria, for example 'not_equal'.
            - `field` (object) **REQ** — Field against which the criteria is evaluated.
              - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the field.
              - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the field.
            - `type` (string) **REQ** [maxLen=50] — Type of criteria, for example 'value'.
            - `value` (string) **REQ** [maxLen=255] — Value used in the comparison (for example ${EMPTY}).
          - `actions` (array of object) [maxItems=50] — List of actions executed when the criteria is satisfied.
            - `type` (string) **REQ** [maxLen=50, enum=[6 values]] — Type of action to perform on the field or segment.
            - `field` (object) — Field that this action targets. Either field or segment must be provided.
            - `segment` (object) — Segment that this action targets. Either an existing segment ID or a reference_id must be provided.
            - `value` (string) [maxLen=2000] — Value to set on the field when using the 'set_value' action type; ignored for other action types.
            - `exempted_profiles` (array) [maxItems=500] — Profiles for which this action should not be applied when using lock-type actions.
            - `exempted_portal_user_types` (array) [maxItems=500] — Portal user types for which this action should not be applied when using lock-type actions.
            oneOf:
                additionalProperties: any
                additionalProperties: any
                additionalProperties: any

**Responses:**

- **200**: Wizard updated successfully. [application/json]
    > Response body returned after updating a wizard.
    - `wizards` (array of object) [maxItems=1] **REQ** — List of update results for each wizard.
      - `status` (string) **REQ** [enum=['success']] — Indicates that the wizard was updated successfully.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Response code for successful update.
      - `message` (string) **REQ** [maxLen=255, enum=['wizard updated successfully']] — Message describing the update result.
      - `details` (object) **REQ** — Contains identifiers related to the updated wizard.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the updated wizard.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request is invalid due to one or more validation errors in the wizard definition. [application/json]
    > Error response returned when the wizard update payload fails validation.
    - `wizards` (array of object) [maxItems=100] **REQ** — List of validation errors, one per wizard payload in the request.
      oneOf:
          - `status` (string) **REQ** [enum=['error']] — Indicates that the operation failed.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code for invalid data validation failure.
          - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
          - `details` (object) **REQ** — Additional error details; the exact fields vary depending on the error code.
            - `api_name` (string) **REQ** [maxLen=255] — Name of the field or entity that is invalid or missing.
            - `json_path` (string) **REQ** [maxLen=2000] — JSONPath expression pointing to the invalid or missing value in the request body.
            - `expected_data_type` (string) [maxLen=50] — Expected data type for the offending value (for example 'boolean', 'bigint').
            - `regex` (string) [maxLen=255] — Pattern that the value was expected to match, when applicable.
            - `resource_path_index` (integer/int32) — Index of the resource in the path, when the error refers to a specific resource path index.
            - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric identifier related to the field or element that caused the validation error.
            - `dependee` (object) — Field on which the current field depends in a dependency validation error.
              - `api_name` (string) **REQ** [maxLen=255] — API name of the dependee field.
              - `json_path` (string) **REQ** [maxLen=2000] — JSONPath of the dependee field in the request body.
          - `status` (string) **REQ** [enum=['error']] — Indicates that the operation failed.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code for invalid data validation failure.
          - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
          - `details` (object) **REQ** — Additional details including the list of accepted values for the field.
            - `api_name` (string) **REQ** [maxLen=255] — API name of the field that received an invalid value.
            - `json_path` (string) **REQ** [maxLen=2000] — JSONPath expression pointing to the invalid field in the request body.
            - `supported_values` (array of string) [maxItems=50] **REQ** — List of accepted values for the field.
              items: [maxLen=255]
          - `status` (string) **REQ** [enum=['error']] — Indicates that the operation failed.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code for mandatory not found validation failure.
          - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
          - `details` (object) **REQ** — Additional error details; the exact fields vary depending on the error code.
            - `api_name` (string) **REQ** [maxLen=255] — Name of the field or entity that is invalid or missing.
            - `json_path` (string) **REQ** [maxLen=2000] — JSONPath expression pointing to the invalid or missing value in the request body.
            - `expected_data_type` (string) [maxLen=50] — Expected data type for the offending value (for example 'boolean', 'bigint').
            - `regex` (string) [maxLen=255] — Pattern that the value was expected to match, when applicable.
            - `resource_path_index` (integer/int32) — Index of the resource in the path, when the error refers to a specific resource path index.
            - `dependee` (object) — Field on which the current field depends in a dependency validation error.
              - `api_name` (string) **REQ** [maxLen=255] — API name of the dependee field.
              - `json_path` (string) **REQ** [maxLen=2000] — JSONPath of the dependee field in the request body.
          - `status` (string) **REQ** [enum=['error']] — Indicates that the operation failed.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code for not allowed validation failure.
          - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
          - `details` (object) **REQ** — Additional error details; the exact fields vary depending on the error code.
            - `api_name` (string) **REQ** [maxLen=255] — Name of the field or entity that is invalid or missing.
            - `json_path` (string) **REQ** [maxLen=2000] — JSONPath expression pointing to the invalid or missing value in the request body.
            - `expected_data_type` (string) [maxLen=50] — Expected data type for the offending value (for example 'boolean', 'bigint').
            - `regex` (string) [maxLen=255] — Pattern that the value was expected to match, when applicable.
            - `resource_path_index` (integer/int32) — Index of the resource in the path, when the error refers to a specific resource path index.
            - `dependee` (object) — Field on which the current field depends in a dependency validation error.
              - `api_name` (string) **REQ** [maxLen=255] — API name of the dependee field.
              - `json_path` (string) **REQ** [maxLen=2000] — JSONPath of the dependee field in the request body.
          - `status` (string) **REQ** [enum=['error']] — Indicates that the operation failed.
          - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code for dependent mismatch validation failure.
          - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
          - `details` (object) **REQ** — Additional error details; the exact fields vary depending on the error code.
            - `api_name` (string) **REQ** [maxLen=255] — Name of the field or entity that is invalid or missing.
            - `json_path` (string) **REQ** [maxLen=2000] — JSONPath expression pointing to the invalid or missing value in the request body.
            - `expected_data_type` (string) [maxLen=50] — Expected data type for the offending value (for example 'boolean', 'bigint').
            - `regex` (string) [maxLen=255] — Pattern that the value was expected to match, when applicable.
            - `resource_path_index` (integer/int32) — Index of the resource in the path, when the error refers to a specific resource path index.
            - `dependee` (object) — Field on which the current field depends in a dependency validation error.
              - `api_name` (string) **REQ** [maxLen=255] — API name of the dependee field.
              - `json_path` (string) **REQ** [maxLen=2000] — JSONPath of the dependee field in the request body.
          - `status` (string) **REQ** [enum=['error']] — Indicates that the operation failed.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code for invalid data validation failure.
          - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
          - `details` (object) **REQ** — Additional error details; the exact fields vary depending on the error code. Used when api_name is absent from the error details.
            - `api_name` (string) [maxLen=255] — API name of the field involved in the error. Not present in this error variant.
            - `json_path` (string) **REQ** [maxLen=2000] — JSONPath expression pointing to the invalid or missing value in the request body.
            - `expected_data_type` (string) [maxLen=50] — Expected data type for the offending value (for example 'boolean', 'bigint').
            - `regex` (string) [maxLen=255] — Pattern that the value was expected to match, when applicable.
            - `resource_path_index` (integer/int32) — Index of the resource in the path, when the error refers to a specific resource path index.
            - `dependee` (object) — Field on which the current field depends in a dependency validation error.
              - `api_name` (string) **REQ** [maxLen=255] — API name of the dependee field.
              - `json_path` (string) **REQ** [maxLen=2000] — JSONPath of the dependee field in the request body.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **401**: Authentication credentials are missing or invalid. [application/json]
    > Represents the error response returned when authentication credentials are missing or invalid.
    oneOf:
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Error code indicating OAuth scope mismatch.
        - `details` (object) **REQ** — Empty details object.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [enum=['error']] — Status indicating failure.
        - `code` (string) **REQ** [enum=['INVALID_TOKEN']] — Error code indicating an invalid token.
        - `details` (object) **REQ** — Empty details object.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [enum=['error']] — Status indicating failure.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The authenticated user does not have permission to update wizards. [application/json]
    > Error returned when the user lacks permission to perform the operation.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating insufficient permissions.
    - `details` (object) **REQ** — Details about the required permissions.
      - `permissions` (array of string) [maxItems=50] **REQ** — List of permissions required.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `status` (string) **REQ** [enum=['error']] — Status indicating failure.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **404**: The requested wizard resource could not be found due to an invalid URL pattern. [application/json]
    > Error response body returned when the requested wizard resource cannot be found due to an invalid URL pattern.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
        - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Error code indicating an invalid URL pattern.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message describing the issue.
        - `details` (object) **REQ** — Additional information about the error, if available.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.wizards.UPDATE

# GET /settings/wizards/{id}
**Operation:** `getWizardDetails` — Get wizard details
> To retrieve the complete configuration of a single wizard in your Zoho CRM organization, including its containers, screens, segments, buttons, and conditional rules.

**Parameters:**
- `id` (path, string/int64, required): Specify the unique ID of the wizard to retrieve or delete.
- `layout_id` (query, string/int64, required): Specify the unique ID of the layout associated with the wizard. Refer to the [Get Layouts](layouts.yaml#$.paths./settings/layouts.get) resource for valid values.

**Responses:**

- **200**: Returns the detailed configuration of the specified wizard, including its containers, screens, segments, buttons, conditional rules, and associated metadata. [application/json]
    > Represents the response body containing the wizard configuration for the requested identifier.
    - `wizards` (array of object) [maxItems=1] **REQ** — Represents the list of wizards in the response. For this operation, the array contains exactly one wizard object corresponding to the requested identifier.
      - `created_time` (string/date-time) **REQ** — Represents the timestamp when Zoho CRM created the wizard.
      - `modified_time` (string/date-time) **REQ** — Represents the timestamp when Zoho CRM last modified the wizard.
      - `display_label` (string) **REQ** [maxLen=255] — Represents the display label of the wizard, translated into the available locale where applicable.
      - `portal_user_types` (array of object) [maxItems=50, nullable] **REQ** — Represents the client portal user types for which the wizard is available.
        - `display_label` (string) **REQ** [maxLen=255] — Represents the display label of the portal user type.
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the portal user type.
        - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the portal user type.
      - `module` (object) **REQ** — Represents the Zoho CRM module associated with the wizard.
        - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the Zoho CRM module associated with the wizard.
        - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the Zoho CRM module associated with the wizard.
      - `name` (string) **REQ** [maxLen=30] — Represents the API name of the wizard.
      - `modified_by` (object) **REQ** — Represents the user who last modified the wizard.
        - `name` (string) **REQ** [maxLen=255] — Name of the user who last modified the wizard.
        - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the user who last modified the wizard.
      - `profiles` (array of object) [maxItems=50, nullable] **REQ** — Represents the Zoho CRM profiles for which the wizard is available.
        - `display_label` (string) **REQ** [maxLen=255] — Represents the display label of the profile, translated into the available locale where applicable.
        - `name` (string) **REQ** [maxLen=255] — Name of the profile.
        - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the profile.
      - `active` (boolean) **REQ** — Indicates whether the wizard is currently active.

Possible values:
true - The wizard is active and available for use in the CRM module.
false - The wizard is inactive and not available for use.
      - `source` (string) [maxLen=50, enum=['crm', 'platform_plugin', 'marketplace_plugin']] — Indicates the source that originated the wizard.
      - `containers` (array of object) [maxItems=7] **REQ** — Represents the list of containers associated with the wizard. Each container links a specific layout to the screens and segments that define the wizard flow for that layout.
        - `layout` (object) **REQ** — Represents the layout from which wizard fields are sourced for this container.
          - `display_label` (string) **REQ** [maxLen=255] — Represents the display label of the layout, translated into the user's locale where available.
          - `name` (string) **REQ** [maxLen=50] — Represents the name of the layout associated with the wizard container.
          - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the layout. Refer to the [Get Layouts](layouts.yaml#$.paths./settings/layouts.get) endpoint for details.
        - `chart_data` (object) **REQ** — Represents the metadata that describes the visual flow between screens in the wizard canvas, including the color palette applied to the canvas and the connections between screens.
          - `nodes` (array of object) [maxItems=75] **REQ** — Represents the list of visual nodes on the wizard canvas, where each node corresponds to a screen in the wizard flow.
            - `pos_x` (integer/int32) **REQ** — Represents the X-coordinate position, in pixels, of the node on the wizard canvas.
            - `pos_y` (integer/int32) **REQ** — Represents the Y-coordinate position, in pixels, of the node on the wizard canvas.
            - `start_node` (boolean) **REQ** — Indicates whether this node is the starting screen in the wizard flow.
Possible values:
true - The node is the starting screen of the wizard flow.
false - The node is not the starting screen of the wizard flow.
            - `screen` (object) **REQ** — Represents the wizard screen associated with this node in the flow chart.
              - `display_label` (string) **REQ** [maxLen=255] — Represents the display label of the screen associated with the node.
              - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the screen associated with the node.
          - `connections` (array of object) [maxItems=75, nullable] **REQ** — Represents the list of connections between source and target screens that define the navigation flow within the wizard.
            - `source_screen` (object) **REQ** — Represents the screen from which the connection originates in the wizard flow, identifying the starting point of the transition.
              - `display_label` (string) **REQ** [maxLen=255] — Represents the display label of the source screen as it appears in the wizard canvas.
              - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the source screen from which the connection originates.
            - `target_screen` (object) **REQ** — Represents the screen to which the connection points in the wizard flow, identifying the destination of the transition.
              - `display_label` (string) **REQ** [maxLen=255] — Represents the display label of the target screen as it appears in the wizard canvas.
              - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the target screen to which the connection points.
            - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the connection between the source screen and the target screen in the wizard flow.
          - `color_palette` (object) — Represents the color palette applied to the wizard canvas, defining the colors used for visual elements such as button backgrounds.
            - `button_background` (array of string) [maxItems=10] — Represents the list of hex color values applied to button backgrounds in the wizard canvas.
              items: [maxLen=7]
        - `screens` (array of object) [maxItems=75] **REQ** — Represents the list of screens included in the wizard container. Each screen groups one or more segments presented to the user during the wizard flow.
          - `display_label` (string) **REQ** [maxLen=255] — Display label of the screen.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the screen within the wizard container.
          - `id` (string/int64) **REQ** [maxLen=19] — Numeric unique identifier of the screen.
          - `conditional_rules` (array of object) [maxItems=50, nullable] — Represents the list of conditional rules evaluated on the screen. Returns null when no conditional rules are configured for the screen.
            - `query_id` (string/int64) **REQ** [maxLen=19] — Represents the unique numeric identifier of the conditional rule.
            - `execute_on` (string) **REQ** [maxLen=50, enum=['create_edit', 'create', 'edit']] — Represents the event on which the conditional rule executes, for example 'create_edit'.
            - `criteria` (object) — Represents the criteria expression evaluated to determine whether the conditional rule actions are triggered.
              - `comparator` (string) **REQ** [maxLen=50] — Indicates the comparator used to evaluate the criteria expression. Possible values include not_equal, equal, is_empty, and is_not_empty.
              - `field` (object) **REQ** — Represents the field against which the criteria expression is evaluated.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field used in the criteria expression.
                - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the field used in the criteria expression.
              - `type` (string) **REQ** [maxLen=50] — Represents the type of the criteria applied in the conditional rule evaluation, for example 'value'.
              - `value` (string) **REQ** [maxLen=255] — Represents the value used in the criteria comparison during conditional rule evaluation, for example ''.
            - `actions` (array of object) [maxItems=50] **REQ** — Represents the list of actions executed when the conditional rule criteria are satisfied on the screen.
              - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique numeric identifier of the conditional rule action.
              - `type` (string) **REQ** [maxLen=50] — Indicates the type of action to perform on the targeted field or segment. Possible values include set_mandatory, make_read_only, hide, and show.
              - `field` (object) — Represents the wizard screen field to which the conditional rule action is applied. This object is present only for field-targeting action types.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the wizard screen field on which the conditional rule action is executed.
                - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique numeric identifier of the wizard screen field on which the conditional rule action is executed.
              - `segment` (object) — Represents the segment on which the action is applied. Present only for segment-targeting actions.
                - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the segment on which the action is executed.
                - `display_label` (string) [maxLen=255] — Represents the display label of the segment on which the action is executed.
              - `value` (string) [maxLen=2000] — Represents the value applied to the field by the action. Present only for field-value actions.
              - `exempted_profiles` (array of object) [maxItems=500] — Represents the list of CRM profiles that are exempted from the conditional rule action and will not have the action applied to them.
                - `id` (string/int64) [maxLen=19] — Represents the unique numeric identifier of the CRM profile that is exempted from the conditional rule action.
                - `name` (string) [maxLen=255] — Represents the display name of the CRM profile that is exempted from the conditional rule action.
              - `exempted_portal_user_types` (array of object) [maxItems=500] — Represents the list of client portal user types that are exempted from the conditional rule action on the screen.
                - `id` (string/int64) [maxLen=19] — Represents the unique numeric identifier of the portal user type that is exempted from the conditional rule action.
                - `name` (string) [maxLen=255] — Represents the display name of the portal user type that is exempted from the conditional rule action.
          - `segments` (array of object) [maxItems=75] **REQ** — Represents the segments that group fields, buttons, and other elements displayed on the screen.
            - `sequence_number` (integer/int32) **REQ** — Represents the sequential position of the segment within the screen, determining its display order.
            - `display_label` (string) **REQ** [maxLen=255] — Display label of the segment.
            - `column_count` (integer/int32) **REQ** — Represents the number of columns used to arrange elements within the segment layout.
            - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the segment.
            - `type` (string) **REQ** [maxLen=50, enum=['composite', 'fields', 'subforms', 'text_label', 'widget', 'buttons']] — Represents the type of the segment, for example 'composite', 'text_label', or 'buttons'.
            - `tab_traversal` (string) [enum=['left_to_right', 'top_to_bottom']] — Represents the traversal order for elements within the segment, used for keyboard navigation.
            - `elements` (array of object) [maxItems=200] — Represents the collection of field elements contained within the segment, present when the segment is of a composite type.
              - `sequence_number` (integer/int32) **REQ** — Represents the position of the element within the segment, determining the display order.
              - `type` (string) **REQ** [maxLen=50, enum=['field', 'query_component']] — Represents the type of element within the segment, for example 'field'.
              - `resource` (object) **REQ** — Represents the field resource referenced by this element, linking the element to its associated data field definition.
                - `name` (string) **REQ** [maxLen=255] — Represents the API name of the field resource associated with this element.
                - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the field resource associated with this element.
            - `name` (string) [maxLen=255] — Represents the name of the segment. Present for text_label and buttons segments.
            - `content` (string) [maxLen=2000] — Represents the static content of the segment, applicable to segments of the text_label type.
            - `buttons` (array of object) [minItems=1, maxItems=50] — Represents the buttons displayed inside this segment. Present for segments of the buttons type.
              - `color` (string) **REQ** [maxLen=7] — Represents the text color of the button, typically expressed as a hexadecimal color value.
              - `shape` (string) **REQ** [enum=['square', 'capsule', 'round']] — Represents the visual shape of the button as rendered in the wizard interface.
              - `visibility` (string) **REQ** [enum=['hide', 'disable', 'show']] — Indicates the visibility behavior of the button, controlling whether the button is displayed or hidden within the wizard segment.
              - `resource` (object) — Resource associated with the button, if any.
                - `id` (string/int64) [maxLen=19] — Represents the unique numeric identifier of the resource associated with the button.
                - `name` (string) [maxLen=255] — Represents the name of the resource associated with the button.
              - `criteria` (object) — Represents the criteria controlling the visibility or behavior of the button, defining the conditions under which the button is active or displayed.
                - `comparator` (string) [maxLen=50] — Represents the comparator used in the criteria to evaluate the relationship between the field and the value.
                - `field` (object) — Represents the field against which the criteria is evaluated when determining the visibility or behavior of the button.
                - `type` (string) [maxLen=50] — Represents the type of criteria applied to the button, indicating the nature of the condition being evaluated.
                - `value` (string) [maxLen=255] — Represents the value used in the comparison when evaluating the criteria associated with the button.
              - `profiles` (array of object) [maxItems=40, nullable] — Represents the profiles for which this button is available.
                - `id` (string/int64) [maxLen=19] — Represents the unique identifier of the profile.
                - `name` (string) [maxLen=255] — Internal name of the profile.
                - `display_label` (string) [maxLen=255] — Display label of the profile.
              - `target_screen` (object) — Represents the screen to which the wizard navigates when this button is activated. Returns null for buttons that perform a save operation without navigation.
                - `name` (string) **REQ** [maxLen=255] — Represents the name of the target screen to which the button navigates.
                - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique numeric identifier of the target screen to which the button navigates.
              - `type` (string) **REQ** [enum=['save', 'transition'], nullable] — Represents the type of action performed by the button within the wizard segment.
              - `message` (object) — Represents the message configuration used when this button performs a save or summary action.
                - `title` (string) [maxLen=255] — Title of the acknowledgement message.
                - `content` (string) [maxLen=2000] — Body content of the acknowledgement message.
              - `transition` (object) — Represents the automation transition configuration applied when this button is activated. Returns null when no transition is configured.
                - `id` (string/int64) [maxLen=19] — Represents the unique numeric identifier of the automation transition associated with the button.
              - `sequence_number` (integer/int32) **REQ** — Represents the sequential position of the button within its parent segment, determining the display order.
              - `display_label` (string) **REQ** [maxLen=255] — Represents the display label of the button, shown to the user as the visible text or title of the button.
              - `background_color` (string) **REQ** [maxLen=7] — Represents the background color of the button, typically expressed as a hexadecimal color value.
              - `name` (string) **REQ** [maxLen=255] — Represents the name of the button.
              - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the button.
              - `category` (string) **REQ** [enum=['wizard_button', 'custom_button']] — Represents the category of the button, used to classify or group the button by its functional purpose.
              - `show_summary_on` (string) [maxLen=50, enum=['create', 'edit', 'create_and_edit', None], nullable] — Indicates the condition or event upon which a summary screen is displayed, when a summary screen is configured for the button.
            - `widget` (object) — Represents the widget resource linked to this segment. Required when the segment type is 'widget'.
              - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the widget linked to the segment.
              - `name` (string) [maxLen=255] — Represents the name of the widget linked to the segment.
        - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the container layout.
      - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the wizard.
      - `created_by` (object) **REQ** — Represents the user who created the wizard.
        - `name` (string) **REQ** [maxLen=255] — Name of the user who created the wizard.
        - `id` (string/int64) **REQ** [maxLen=19] — Represents the unique identifier of the user who created the wizard.

- **204**: The request succeeded. No content returns in the response body.

- **400**: The request was malformed or contained invalid parameters.
**Resolution:** The request URL and parameters must use valid values. Refer to the API documentation for the required format. [application/json]
    > Represents the error response returned when the request contains invalid or missing parameters.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the request, indicating that the request failed.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned when a required parameter is missing.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message returned when a required parameter is missing.
        - `details` (object) **REQ** — Represents additional information about the missing parameter that caused the error.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing parameter that caused the validation error.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the request, indicating that the request failed.
        - `code` (string) **REQ** [enum=['EXPECTED_PARAM_MISSING']] — Represents the error code returned when a required query parameter is missing.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message returned when expected parameters are missing from the request.
        - `details` (object) **REQ** — Represents additional details about the missing expected parameters.
          - `param_names` (array of string) [minItems=1, maxItems=50] **REQ** — Represents the list of expected parameter names that are missing from the request.
            items: [maxLen=255]
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the request, indicating that the request failed.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned when the module specified in the request is invalid.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the validation failure.
        - `details` (object) **REQ** — Represents additional details about the error. Returns an empty object when no additional details are available.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the request, indicating that the request failed.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the wizard identifier in the request is invalid.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the validation failure.
        - `details` (object) **REQ** — Represents additional details about the invalid field that caused the validation error.
          - `api_name` (string) [maxLen=255] — Represents the API name of the invalid field that caused the validation error.
          - `json_path` (string) [maxLen=255] — Represents the JSON path pointing to the invalid field in the request.

- **401**: Authentication credentials are missing or invalid.
**Resolution:** A new access token must be generated with the required scope for this API. [application/json]
    > Represents the error response returned when authentication credentials are missing or invalid.
    oneOf:
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code returned when the OAuth access token does not include the required scope.
        - `details` (object) **REQ** — Represents additional details about the authentication error. Returns an empty object when no additional details are available.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the request, indicating that the request failed.
        - `code` (string) **REQ** [enum=['INVALID_TOKEN']] — Represents the error code returned when the OAuth access token is invalid or has expired.
        - `details` (object) **REQ** — Represents additional details about the authentication error. Returns an empty object when no additional details are available.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the authentication failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the request, indicating that the request failed.

- **403**: Permission denied to retrieve wizard details.
**Resolution:** The Zoho CRM administrator must grant the required permission to the user's profile. [application/json]
    > Represents the error response returned when the user lacks the required permission to perform the operation.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned when the user does not have permission to perform the operation.
    - `details` (object) **REQ** — Represents additional details about the permissions required to perform the operation.
      - `permissions` (array of string) [maxItems=50] **REQ** — Represents the list of permissions required to access this resource.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the permission denial.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request, indicating that the request failed.

- **404**: The requested wizard resource was not found.
**Resolution:** The wizard ID and layout ID in the request must correspond to existing resources in the Zoho CRM organization. [application/json]
    > Represents the error response returned when the requested wizard resource is not found.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the request, indicating that the request has failed.
        - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code returned when the URL pattern is invalid or the requested resource does not exist.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message explaining why the requested resource was not found.
        - `details` (object) **REQ** — Additional information about the error, if available.

**Scopes:** ZohoCRM.settings.wizards.READ

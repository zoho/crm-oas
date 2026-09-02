# GET /settings/global_picklists/{id}/actions/pick_list_values_associations
**Operation:** `getPickListValuesAssociations` — Get Picklist Value Associations
> To the list of features like blueprints, workflows create, workflow convert, workflow task, ABM, etc in which a particular picklist value is used.

**Parameters:**
- `id` (path, string/int64, required): Numeric id of the global picklist. Use the [Get All Global Picklists](global_picklists.yaml#$.paths./settings/global_picklists.get) resource to retrieve global picklist IDs.

- `picklist_value_id` (query, string/int64, required): The ID of the picklist value to retrieve associations for. Use the [Get All Global Picklists](global_picklists.yaml#$.paths./settings/global_picklists.get) resource to retrieve picklist value IDs.


**Responses:**

- **200**: Successful response containing picklist value associations with various features like blueprints, workflows, orchestrations, etc. [application/json]
    > Response object containing picklist value associations.
    - `pick_list_values_associations` (array of object) [maxItems=100] **REQ** — Array of picklist value associations grouped by association type.
      - `resources` (array of object) [maxItems=100] **REQ** — Array of resources associated with the picklist value.
        - `name` (string) **REQ** [maxLen=255] — Name of the resource.
        - `details` (object) **REQ** — Details about the resource associations.
          oneOf:
              - `module` (object) **REQ** — Module details for blueprint.
                - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
                - `id` (string/int64) **REQ** — Id of the resource.
                - `plural_label` (string) **REQ** [maxLen=25] — Plural label of the module.
              - `actions` (array of object) [maxItems=100] **REQ** — Array of actions associated with the orchestration or workflow.
                - `module` (object) **REQ** — Module details for the action.
                  - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
                  - `id` (string/int64) **REQ** — Id of the resource.
                - `transition` (object) — Transition details for orchestration actions.
                  - `name` (string) **REQ** [maxLen=255] — Name of the transition.
                  - `id` (string/int64) **REQ** — Id of the resource.
                - `id` (string/int64) **REQ** — Id of the resource.
                - `type` (string) **REQ** [maxLen=100] — Type of action.
              type: array of object [maxItems=100]
                - `name` (string) **REQ** [maxLen=255] — Name of the task or field update.
                - `id` (string/int64) **REQ** — Id of the resource.
                - `type` (string) **REQ** [maxLen=100] — Type of association (Workflow, Orchestration, etc.).
                - `transition` (object) — Transition details for orchestration tasks.
                  - `name` (string) **REQ** [maxLen=255] — Name of the transition.
                  - `id` (string/int64) **REQ** — Id of the resource.
        - `id` (string/int64) **REQ** — Id of the resource.
      - `type` (string) **REQ** [maxLen=100] — Type of association (field_update, task, blueprint, orchestration, workflow, etc.).

- **204**: if the picklist value is not associated with any features.

- **400**: Bad Request - Invalid data, missing parameters, or not allowed actions. [application/json]
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Error code indicating the type of error.
        - `details` (object) **REQ** — Additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** [const=2] — Index in the resource path indicating the error location.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error response.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code indicating missing parameter.
        - `details` (object) **REQ** — Additional details about the missing parameter.
          - `param` (string) **REQ** [maxLen=100] — Name of the missing parameter.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error response.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid data.
        - `details` (object) **REQ** — Additional details about the invalid parameter.
          - `param_name` (string) **REQ** [maxLen=100] — Name of the invalid parameter.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error response.

- **403**: Forbidden [application/json]
    > Error response object containing code, message, details, and status.
    - `code` (string) **REQ** [maxLen=50] — Error code indicating the type of error.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `details` (object) **REQ** — Additional details about the error.
      - `permissions` (array of string) [maxItems=1] — List of permissions required to access the resource.
        items: [enum=['Crm_Implied_Customize_Zoho_CRM']]
    - `status` (string) **REQ** [maxLen=100, enum=['error']] — Status of the error response.

- **500**: Internal Server Error [application/json]
    > Internal server error response object containing code, message, details, and status.
    - `code` (string) **REQ** [maxLen=50] — Error code indicating the type of error.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `details` (object) **REQ** — Additional details about the error.
    - `status` (string) **REQ** [enum=['error']] — Status of the error response.

**Scopes:** ZohoCRM.settings.global_picklist.ALL

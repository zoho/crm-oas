# GET /settings/blueprints/process_configurations
**Operation:** `getBlueprintProcessConfigurationMeta` — Blueprints Process Configurations
> To retrieve the metadata of the Blueprint process configuration in your Zoho CRM organization, such as the number of configured Blueprints, the supported features and their limits, and the supported owner models.

**Parameters:**
- `X-CRM-ORG` (header, integer/int32, optional) [enum=[1234567]] {style=simple, explode=False}: Specify the organization ID in the request header to identify the target Zoho CRM organization.

**Responses:**

- **200**: Returns the Blueprint process configuration details for the Zoho CRM organization, including the number of configured Blueprints, supported features, feature limits, and supported owner models. — Schema: `BlueprintProcessConfigurationsResponse` [application/json]
    > Represents the response body for the Blueprint process configurations request. Contains the configuration overview for the Zoho CRM organization.
    schema: `BlueprintProcessConfigurationsResponse`
    - `blueprints` (object `BlueprintProcessConfigurationOverview`) **REQ** — Represents the Blueprint process configuration overview for the Zoho CRM organization, including usage counts, feature limits, supported features and owner models, and the last seen module reference.
      schema: `BlueprintProcessConfigurationOverview`
      - `common_transitions_per_blueprint` (integer/int32) **REQ** — Represents the maximum number of common transitions that can be configured for each Blueprint.
      - `total_blueprint_configured` (integer/int32) **REQ** — Represents the total number of Blueprints configured in the Zoho CRM organization.
      - `supported_features` (array of string) [maxItems=5] **REQ** — Contains the list of features supported in Blueprint configuration.
        items: [maxLen=255]
      - `maximum_allowed_blueprints` (integer/int32) **REQ** — Represents the maximum number of Blueprints that can be configured in the Zoho CRM organization.
      - `active_blueprint_configured` (integer/int32) **REQ** — Represents the number of Blueprints with an active status in the Zoho CRM organization.
      - `last_seen_module` (object `BlueprintLastSeenModuleReference`) **REQ** — Represents the module most recently accessed in the Blueprint settings of the Zoho CRM UI, including the module API name and ID.
        schema: `BlueprintLastSeenModuleReference`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module most recently accessed in the Blueprint settings of the Zoho CRM UI.
        - `id` (string) **REQ** [maxLen=255, nullable] — Represents the ID of the module most recently accessed in the Blueprint settings of the Zoho CRM UI. Returns **null** when the module is All.
      - `supported_owner_models` (array of string) [maxItems=6] **REQ** — Contains the types of owners that can be configured as Blueprint and transition owners.
        items: [maxLen=255]
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The API is not supported for the selected domain.
**Resolution:** The API must be called from a supported data center. Refer to the **supported_domains** array in the response for the list of available domains. [application/json]
    > Represents the error response returned when the API is not supported for the selected domain. Contains the error code, message, status, and the list of supported domains.

    oneOf:
      - `APINotSupportedError` — Represents the error response returned when the API is not supported for the selected domain. Includes the error code, message, status, and a list of domains where the API is supported.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code identifying the failure reason.
Possible values:
**API_NOT_SUPPORTED** - The API is not supported for the selected domain.
        - `details` (object) **REQ** — Contains the details of the error, including the domains where the API is supported.
          - `supported_domains` (array of string) [maxItems=25] **REQ** — Lists the domains where this API is supported.
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=['api not supported']] — Represents the error message describing the failure.
Possible values:
**api not supported** - The API is not supported for the current domain.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request failed.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: No permission to access the Blueprint process configuration. Resolution: The CRM administrator must grant the required permission to the user's CRM profile. [application/json]
    > Represents the error response returned when the user does not have permission to access the Blueprint process configuration. Contains the error code, message, status, and permission details.
    oneOf:
      - `PermissionDeniedError` — Represents the error response returned when the caller lacks permission to access the Blueprint process configurations resource. Includes the error code, message, status, and the required permissions.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code identifying the failure reason.
Possible values:
**NO_PERMISSION** - The user does not have the required permission.
        - `details` (object) **REQ** — Contains the details of the error, including the permissions required for the operation.
          - `permissions` (array of string) [maxItems=25] **REQ** — Lists the permissions required to perform the operation.
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=['No permission']] — Represents the error message describing the failure.
Possible values:
**No permission** - The user's Zoho CRM profile lacks the required permission.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request failed.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.blueprint.READ

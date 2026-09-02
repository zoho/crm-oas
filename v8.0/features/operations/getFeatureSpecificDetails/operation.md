# GET /__features/{feature}
**Operation:** `getFeatureSpecificDetails` — Specific Feature
> To retrieve the detailed information for a specific feature in your Zoho CRM organization, including its usage limits, consumption details, and sub-feature components.

**Parameters:**
- `feature` (path, string, required) [maxLen=25]: Specify the API name of the feature for which you want to retrieve detailed information.
- `module` (query, string, optional) [maxLen=25]: Specify the API name of the CRM module to filter features that are specific to that module. Refer to the [Get Modules](modules.json#$.paths./settings/modules.get) resource for valid values.

**Responses:**

- **200**: Returns the detailed information for the requested feature, including its usage limits, consumption details, and sub-feature components. [application/json]
    > Represents the response structure for a successful single feature retrieval, containing the detailed information for the requested feature.
    - `__features` (array of object) [maxItems=1] **REQ** — Represents the list containing the detailed information for the requested feature. Always returned in the response.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the unique API identifier for the feature, such as **custom_field** or **encrypt_field**. Always returned in the response.
      - `parent_feature` (object) **REQ** — Represents the parent feature of the current feature, when applicable. Always returned in the response.
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the parent feature. Always returned in the response.
      - `details` (object) **REQ** — Represents the limits and usage details for the feature, including available count, usage limits, and current consumption. Always returned in the response.
        - `available_count` (object) — Represents the number of feature instances available for use in the organization.
          - `total` (integer/int32) **REQ** — Represents the total number of available instances for the feature. Always returned in the response.
        - `limits` (object) **REQ** — Represents the maximum usage limits for the feature, including the absolute total limit and the edition-level ceiling. Always returned in the response.
          - `total` (integer/int32) **REQ** — Represents the absolute maximum count for the feature across all editions. Always returned in the response.
          - `edition_limit` (integer/int32) — Represents the maximum count for the feature allowed by the current subscription edition.
        - `used_count` (object) — Represents the current usage counts for the feature in the organization.
          - `total` (integer/int32) **REQ** — Represents the total number of feature instances currently in use. Always returned in the response.
          additionalProperties: any
      - `components` (array of object) [maxItems=200, nullable] **REQ** — Represents the list of sub-feature components for the feature. Each component includes its own API name, module support flag, and usage limit details. Always returned in the response.
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the component within the feature. Always returned in the response.
        - `module_supported` (boolean) **REQ** — Indicates whether the component is supported for the specified module. Possible values: true - The component is supported for the module. false - The component is not supported for the module. Always returned in the response.
        - `details` (object) **REQ** — Represents the usage limits and consumption details for the component. Always returned in the response.
          - `limits` (object) — Represents the usage limits configured for the component. Always returned in the response.
            - `total` (integer/int32) **REQ** — Represents the absolute maximum count for the component, independent of the subscription edition. Always returned in the response.
            - `edition_limit` (integer/int32) — Represents the maximum count for the component allowed by the current subscription edition.
            additionalProperties: any
          - `used_count` (object) — Represents the current usage counts for the component.
            oneOf:
                - `total` (integer/int32) **REQ** — total count
                additionalProperties: any
                type: integer/int32 — used count of the feature
        - `feature_label` (string) **REQ** [maxLen=255] — Represents the display label of the component for presentation in the CRM interface. Always returned in the response.
        additionalProperties: any
      - `module_supported` (boolean) **REQ** — Indicates whether the feature is supported for the CRM module specified in the request. Possible values: true - The feature is supported for the specified module. false - The feature is not supported for the specified module. Always returned in the response.
      - `feature_label` (string) **REQ** [maxLen=255, nullable] — Represents the display label of the feature for presentation in the CRM interface. Always returned in the response.
      additionalProperties: any
    additionalProperties: any

- **204**: Indicates that the specified feature is not available for the current organization's edition.

- **400**: The module API name in the request is invalid, or the request contains invalid data. Resolution: The request parameters must include a valid module API name and properly formatted values. [application/json]
    > Represents the error response structure returned when the request contains an invalid module name or invalid data.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request. Possible values: error - The request resulted in a validation error. Always returned in the response.
    - `code` (string) **REQ** [enum=['INVALID_MODULE', 'INVALID_DATA']] — Represents the error code indicating the type of validation failure. Possible values: INVALID_MODULE - The module API name in the request is not valid. INVALID_DATA - The request contains invalid data. Always returned in the response.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the validation failure. Always returned in the response.
    - `details` (object) **REQ** — Represents additional details about the validation error. Always returned in the response.
    additionalProperties: any

**Scopes:** ZohoCRM.features.READ

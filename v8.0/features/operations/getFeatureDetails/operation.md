# GET /__features
**Operation:** `getFeatureDetails` — Features
> To retrieve the list of all features available in your Zoho CRM organization for the current subscription edition, along with their usage limits and component details.

**Parameters:**
- `module` (query, string, optional) [maxLen=25]: Specify the API name of the CRM module to filter features that are specific to that module. Refer to the [Get Modules](modules.json#$.paths./settings/modules.get) resource for valid values.
- `api_names` (query, string, optional) [enum=[7 values]]: Specify the feature API names to filter the response. To retrieve details of more than one feature, provide the names in comma-separated format. Possible values: custom_field - Feature API name for the custom field feature. custom_field,encrypt_field,unique_field,private_fields,external_field,personal_health_fields - Feature API names for multiple features specified together. encrypt_field - Feature API name for the encrypt field feature. external_field - Feature API name for the external field feature. personal_health_fields - Feature API name for the personal health fields feature. private_fields - Feature API name for the private fields feature. unique_field - Feature API name for the unique field feature.
- `per_page` (query, string, optional) [enum=['10']]: Specify the number of features to return per page. Possible values: 10 - Returns ten features per page.
- `page` (query, string, optional) [enum=['1', '2']]: Specify the page number to retrieve features from the corresponding results page. Possible values: 1 - Retrieves features from page one. 2 - Retrieves features from page two.

**Responses:**

- **200**: Returns the list of features available for the current organization's edition. [application/json]
    > Represents the response structure for a successful feature list retrieval, containing the array of available features and pagination metadata.
    - `__features` (array of object) [maxItems=200] **REQ** — Represents the list of feature objects available for the current edition. Always returned in the response.
      - `api_name` (string) **REQ** [maxLen=255, nullable] — Represents the unique API identifier for the feature, such as **custom_field** or **encrypt_field**. Always returned in the response.
      - `parent_feature` (object) **REQ** — Represents the parent feature of the current feature, when applicable. Always returned in the response.
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the parent feature. Always returned in the response.
      - `details` (object) **REQ** — Represents the limits and usage details for the feature, including available count, usage limits, and current consumption. Always returned in the response.
        - `available_count` (object) — Represents the number of feature instances available for use in the organization.
          - `total` (integer/int32) **REQ** — Represents the total number of available instances for the feature. Always returned in the response.
        - `limits` (object) — Represents the maximum usage limits for the feature, including the absolute total limit and the edition-level ceiling.
          - `total` (integer/int32) **REQ** — Represents the absolute maximum count for the feature across all editions. Always returned in the response.
          - `edition_limit` (integer/int32) — Represents the maximum count for the feature allowed by the current subscription edition.
        - `used_count` (object) — Represents the used count of the feature
          oneOf:
              - `total` (integer/int32) **REQ** — Represents the total count
              additionalProperties: any
              type: integer/int32 — Represents the used count of the feature
      - `components` (array of object) [maxItems=200, nullable] **REQ** — Represents the list of sub-feature components for the feature. Each component includes its own API name, module support flag, and usage limit details. Always returned in the response.
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the component within the feature. Always returned in the response.
        - `module_supported` (boolean) **REQ** — Indicates whether the component is supported for the specified module. Possible values: true - The component is supported for the module. false - The component is not supported for the module. Always returned in the response.
        - `details` (object) **REQ** — Represents the usage limits and consumption details for the component. Always returned in the response.
          - `limits` (object) — Represents the usage limits configured for the component. Always returned in the response.
            - `total` (integer/int32) **REQ** — Represents the absolute maximum count for the component, independent of the subscription edition. Always returned in the response.
            - `edition_limit` (integer/int32) — Represents the maximum count for the component allowed by the current subscription edition.
            additionalProperties: any
          - `used_count` (object) — Represents theused count of the feature
            oneOf:
                - `total` (integer/int32) **REQ** — Represents the total count
                additionalProperties: any
                type: integer/int32 — Represents the used count of the feature
        - `feature_label` (string) **REQ** [maxLen=255] — Represents the display label of the component for presentation in the CRM interface. Always returned in the response.
        additionalProperties: any
      - `module_supported` (boolean) **REQ** — Indicates whether the feature is supported for the CRM module specified in the request. Possible values: true - The feature is supported for the specified module. false - The feature is not supported for the specified module. Always returned in the response.
      - `feature_label` (string) **REQ** [maxLen=255, nullable] — Represents the display label of the feature for presentation in the CRM interface. Always returned in the response.
      additionalProperties: any
    - `info` (object) — Represents the pagination metadata for the response, including the current page number, page size, total feature count, and whether more records are available.
      - `per_page` (integer/int32) **REQ** — Represents the number of feature records included per page in the response. Always returned in the response.
      - `count` (integer/int32) **REQ** — Represents the number of feature records returned in the current page. Always returned in the response.
      - `page` (integer/int32) **REQ** — Represents the current page number in the paginated response. Always returned in the response.
      - `more_records` (boolean) **REQ** — Indicates whether additional feature records are available beyond the current page. Possible values: true - More feature records are available on subsequent pages. false - The current page contains the last set of feature records. Always returned in the response.
      additionalProperties: any
    additionalProperties: any

- **204**: Indicates that no features are available for the current organization's edition, or the specified feature does not exist.

- **400**: The module API name in the request is invalid, or the request contains invalid data. **Resolution**: The request parameters must include a valid module API name and properly formatted values. [application/json]
    > Represents the error response structure returned when the request contains an invalid module name or invalid data.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request. Possible values: error - The request resulted in a validation error. Always returned in the response.
    - `code` (string) **REQ** [enum=['INVALID_MODULE', 'INVALID_DATA']] — Represents the error code indicating the type of validation failure. Possible values: INVALID_MODULE - The module API name in the request is not valid. INVALID_DATA - The request contains invalid data. Always returned in the response.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the validation failure. Always returned in the response.
    - `details` (object) **REQ** — Represents additional details about the validation error. Always returned in the response.
      - `param_name` (string) [maxLen=25] — Represents the name of the parameter that caused the validation error.
    additionalProperties: any

**Scopes:** ZohoCRM.features.READ

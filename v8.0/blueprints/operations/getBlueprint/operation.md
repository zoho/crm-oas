# GET /settings/blueprints
**Operation:** `getBlueprint` — Get blueprints
> To retrieve the list of blueprints configured in your Zoho CRM organization.

**Parameters:**
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Represents the custom header used to identify the calling service.
- `page` (query, integer/int32, optional) [min=1] {style=form, explode=True}: Represents the page number to be accessed.
- `per_page` (query, integer/int32, optional) [min=1, max=200] {style=form, explode=True}: Represents the number of items to be returned per page.
- `module` (query, string, optional) [maxLen=3000] {style=form, explode=True}: Represents the name of the module to filter the results. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name.
- `status` (query, string, optional) [maxLen=3000] {style=form, explode=True}: Represents the status of the Blueprint to filter the results.
- `layout_id` (query, integer/int32, optional) {style=form, explode=True}: Represents the ID of the layout to filter the results. Use the [Get Layouts Metadata API](layouts.yaml#$.paths./settings/layouts.get) to retrieve the Layout ID.
- `sort_by` (query, string, optional) [maxLen=3000] {style=form, explode=True}: Represents the API name of the field based on which the list should be sorted.
- `sort_order` (query, string, optional) [enum=['asc', 'desc']] {style=form, explode=True}: Represents the order in which the list should be sorted.

**Responses:**

- **200**: Returns the list of blueprints retrieved from your Zoho CRM organization. — Schema: `GetBlueprintListResponse` [application/json]
    > Represents the response returned when the Blueprint list is successfully retrieved.
    schema: `GetBlueprintListResponse`
    - `blueprints` (array of object `BlueprintListItem`) [maxItems=50] **REQ** — Represents the list of blueprints returned in the response.
      schema: `BlueprintListItem`
      - `layout` (object `ChartDataBase5`) **REQ** — Represents the details of the layout associated with the Blueprint.
        schema: `ChartDataBase5`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the layout.
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the layout.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the layout.
      - `status` (string) **REQ** [maxLen=255] — Represents the status of the Blueprint.
      - `field` (object `CriteriaFieldRef`) **REQ** — Represents the field referenced in the criteria.
        schema: `CriteriaFieldRef`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field.
        - `field_label` (string) **REQ** [maxLen=255] — Represents the label of the field.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the field.
      - `continuous` (boolean) **REQ** — Indicates whether the Blueprint is configured as continuous.
      - `module` (object `BlueprintModuleSpec`) **REQ** — Represents the details of the module for which the Blueprint is configured.
        schema: `BlueprintModuleSpec`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module for which the Blueprint is configured.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the module for which the Blueprint is configured.
        - `precedence` (integer/int32) **REQ** — Represents the precedence order assigned to the module for which the Blueprint is configured.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the Blueprint.
      - `modified_by` (object `ModifiedByDetail`) **REQ** — Represents the details of the user who last modified the record.
        schema: `ModifiedByDetail`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who last modified the record.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user who last modified the record.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the Blueprint.
      - `created_by` (object `ChartDataBase0`) **REQ** — Represents the details of the user who created the Blueprint.
        schema: `ChartDataBase0`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who created the Blueprint.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user who created the Blueprint.
      - `api_name` (string) [maxLen=255] — Represents the API name of the Blueprint.
      - `description` (string) [maxLen=1000, nullable] — Represents the description of the Blueprint.
      - `criteria` (object `BlueprintEntryCriteriaResponse`) — Contains details of blueprint entry criteria
        schema: `BlueprintEntryCriteriaResponse`
        - `comparator` (string) [maxLen=12, nullable] — Represents the comparator used to evaluate the criteria field against its configured value.
        - `field` (object `CriteriaFieldResponseDetail`) — Contains field details of criteria
          schema: `CriteriaFieldResponseDetail`
          - `id` (string) **REQ** [maxLen=25, pattern=[0-9]+] — Represents the unique ID of the field for which the Blueprint is configured.
          - `api_name` (string) [maxLen=100, nullable] — Represents the API name of the field for which the Blueprint is configured.
          - `field_label` (string) [maxLen=100, nullable] — Represents the label of the field for which the Blueprint is configured.
        - `type` (string) [maxLen=100, nullable] — Represents the type of criteria used to determine whether a record satisfies the Blueprint entry conditions.
        - `value` (string) [maxLen=3, nullable] — Represents the value configured for the criteria field used to evaluate the Blueprint entry condition.
      - `pipeline` (object `PipelineReference`) — Contains details of the pipeline for which blueprint is configured
        schema: `PipelineReference`
        - `name` (string) [maxLen=255, nullable] — Represents the name of the pipeline.
        - `display_value` (string) [maxLen=100, nullable] — Represents the display value of the pipeline.
        - `id` (string) **REQ** [maxLen=25, pattern=[0-9]+] — Represents the unique ID of the pipeline.
        - `api_name` (string) [maxLen=100, nullable] — Represents the API name of the pipeline.
      - `owner` (object) — Represents the list of users or groups configured as owners of the Blueprint.
        oneOf:
            type: array of object `OwnerItemBase` [maxItems=25]
              schema: `OwnerItemBase`
              - `resources` (array of object `ChartDataBase3`) [maxItems=25, nullable] — Represents the list of resources associated with the owner.
                schema: `ChartDataBase3`
                - `id` (string) [maxLen=255] — Represents the unique ID of the resource.
                additionalProperties: any
              - `type` (string) [maxLen=255] — Represents the type of the owner.
              additionalProperties: any
            type: null — Null value for owner field
    - `info` (object `BlueprintListPaginationInfo`) **REQ** — Represents the pagination details of the Blueprint list.
      schema: `BlueprintListPaginationInfo`
      - `per_page` (integer/int32) **REQ** — Represents the number of Blueprint records included per page.
      - `count` (integer/int32) **REQ** — Represents the number of Blueprint records returned in the current page.
      - `page` (integer/int32) **REQ** — Represents the current page number of the Blueprint list.
      - `more_records` (boolean) **REQ** — Indicates whether more Blueprint records are available beyond the current page.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request contains an invalid parameter value.
**Resolution:** The query parameter values provided in the request must be valid. Verify that the **module**, **status**, **sort_by**, **sort_order**, and **layout_id** parameter values match the accepted values for this endpoint. [application/json]
    oneOf:
      - `InvalidModuleParameterError` — Represents the error returned when the module given in the parameter is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned by this response.

Possible values:
INVALID_MODULE - Indicates that the module given seems to be invalid.
        - `details` (object) **REQ** — Represents the details object with validation information about the error.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter associated with the error.
        - `message` (string) **REQ** [enum=['the module given seems to be invalid']] — Represents the error message returned by this response.

Possible values:
the module given seems to be invalid - Indicates that the module given seems to be invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
      - `InvalidStatusParameterError` — Represents the error returned when the status query parameter value given is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that the status given seems to be invalid.
        - `details` (object) **REQ** — Represents the details object with validation information about the error.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter associated with the error.
        - `message` (string) **REQ** [enum=['the status given seems to be invalid', 'the value given is invalid']] — Represents the error message returned by this response.

Possible values:
the status given seems to be invalid - Indicates that the status given seems to be invalid.
the value given is invalid - Indicates that the value given is invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
      - `InvalidSortByParameterError` — Represents the error returned when the sort_by value given in the parameter is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that the sort by value given seems to be invalid.
        - `details` (object) **REQ** — Represents the details object with validation information about the error.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter associated with the error.
        - `message` (string) **REQ** [enum=['the sort by value given seems to be invalid']] — Represents the error message returned by this response.

Possible values:
the sort by value given seems to be invalid - Indicates that the sort by value given seems to be invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
      - `InvalidSortOrderParameterError` — Represents the error returned when the sort_order value given in the parameter is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that the sort order given seems to be invalid.
        - `details` (object) **REQ** — Represents the details object with validation information about the error.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter associated with the error.
        - `message` (string) **REQ** [enum=['the sort order given seems to be invalid']] — Represents the error message returned by this response.

Possible values:
the sort order given seems to be invalid - Indicates that the sort order given seems to be invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
      - `ErrorResponseFilterInvalid` — Represents the error returned when the filter given in the parameters is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the specified filter is invalid.

Possible values:
INVALID_DATA - Indicates that the provided filter is invalid.
        - `details` (object) **REQ** — Represents the details object with validation information about the invalid filter.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter that has an invalid filter.
        - `message` (string) **REQ** [enum=['the filter given seems to be invalid']] — Represents the error message returned when the specified filter is invalid.

Possible values:
the filter given seems to be invalid - Indicates that the provided filter does not meet the expected format.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
      - `RequiredHeaderMissingError` — Represents the error returned when the required X-CRM-ORG header is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_HEADER_MISSING']] — Represents the error code returned by this response.

Possible values:
REQUIRED_HEADER_MISSING - Indicates that one of the expected headers is missing.
        - `details` (object) **REQ** — Represents the details object with validation information about the error.
          - `header_name` (string) **REQ** [maxLen=255] — Represents the name of the missing header.
        - `message` (string) **REQ** [enum=['One of the expected headers is missing']] — Represents the error message returned by this response.

Possible values:
One of the expected headers is missing - Indicates that one of the expected headers is missing.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
      - `InvalidModuleIdError` — Represents the error returned when the module ID given in the query parameter is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned by this response.

Possible values:
INVALID_DATA - Indicates that the ID given seems to be invalid.
        - `details` (object) **REQ** — Represents the details object with validation information about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path associated with the error.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned by this response.

Possible values:
the id given seems to be invalid - Indicates that the ID given seems to be invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to retrieve blueprints.
**Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `NoPermissionError` [application/json]
    > Represents the error returned when the user does not have permission to perform this action.
    schema: `NoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned by this response.

Possible values:
NO_PERMISSION - Indicates that the request contains invalid or unexpected data.
    - `details` (object) **REQ** — Represents the details object with validation information about the error.
      - `permissions` (array of string) [maxItems=50] **REQ** — Represents the list of permissions required to perform this action.
        items: [maxLen=100]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message returned by this response.

Possible values:
permission denied - Indicates that permission denied.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

Possible values:
error - Indicates that the request could not be completed due to an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.blueprint.READ

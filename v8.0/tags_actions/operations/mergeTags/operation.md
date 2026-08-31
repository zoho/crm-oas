# POST /settings/tags/{id}/actions/merge
**Operation:** `mergeTags` — Merge Tags
> Merges two tags into one, combining their associated records and metadata. The tag specified in the path parameter (id) is the master tag that will remain after the merge. The conflict_id in the request body specifies the tag to be merged into the master tag.

**Parameters:**
- `id` (path, string, required) [maxLen=19]: Unique identifier of the record or tag. Use the [Get Tags API](tags.yaml#$.paths./settings/tags.get) to retrieve tag IDs.


**Schemas:**
`NoPermissionError`:
  > Error indicating that the user does not have permission to perform the operation.
  - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code
  - `details` (object) **REQ** — Error details with validation information
    - `permissions` (array of string) [maxItems=25] **REQ** — List of required permissions
      items: [maxLen=255]
  - `message` (string) **REQ** [enum=['permission denied']] — Error message
  - `status` (string) **REQ** [enum=['error']] — Error status

**Request Body** — application/json `PostmergeRequest`
> Request body containing the tag to merge into the master tag.
  > Request body schema for merging tags.
  - `tags` (array of object `TagsNested`) [maxItems=1] **REQ** — Array containing the tag to merge (Required)
    schema: `TagsNested`
    - `name` (string) [maxLen=25, nullable] — Tag name
    - `modified_time` (string/date-time) [maxLen=25, nullable] — Last modification timestamp of the tag
    - `color_code` (string) [maxLen=7, nullable] — Color code of the tag
    - `conflict_id` (string) [maxLen=19, nullable] — ID of the tag to be merged into the master tag

**Responses:**

- **200**: OK - Tags merged successfully. — Schema: `PostmergeResponse200` [application/json]
    > Success response when tags are merged successfully.
    schema: `PostmergeResponse200`
    - `tags` (array of object `TagsNested2`) [maxItems=1] — Array containing the merged tag details
      schema: `TagsNested2`
      - `code` (string) [maxLen=255] — Status code of the merge operation
      - `details` (object `DetailsNested2`) — Nested schema for details in merge response.
        schema: `DetailsNested2`
        - `created_time` (string) [maxLen=255] — Creation timestamp of the tag
        - `modified_time` (string) [maxLen=255] — Last modification timestamp of the tag
        - `modified_by` (object `ModifiedByNested`) — Nested schema for modified_by user details.
          schema: `ModifiedByNested`
          - `name` (string) [maxLen=255] — Name of the user who last modified the resource
          - `id` (string) [maxLen=255] — Unique identifier of the user
        - `id` (string) [maxLen=255] — Unique identifier of the tag
        - `created_by` (object `CreatedByNested`) — Nested schema for created_by user details.
          schema: `CreatedByNested`
          - `name` (string) [maxLen=255] — Name of the user who created the resource
          - `id` (string) [maxLen=255] — Unique identifier of the user
        - `color_code` (string) [maxLen=255, nullable] — Color code of the tag
        - `rid` (string/uuid) — Resource ID
      - `message` (string) [maxLen=255] — Human-readable message about the merge result
      - `status` (string) [maxLen=255] — Status of the merge operation

- **400**: Bad Request - The request cannot be processed due to invalid syntax or validation errors. Review the error details and correct the issues before retrying. [application/json]
    > Error response for status 400
    oneOf:
      - `TagInvalidDataTypeError` — Error indicating that a tag field has an invalid data type.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `expected_data_type` (string) [maxLen=255] — Expected data type for the field
          - `api_name` (string) **REQ** [maxLen=255] — API name of the field with invalid data
          - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the field with invalid data
        - `message` (string) **REQ** [enum=['invalid data', 'invalid tag id']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidRequestMethodError` — Error indicating that the HTTP request method is invalid.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['The http request method type is not a valid one']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
        - `tags` (array of object) [maxItems=25] **REQ** — Array of tag error objects for validation failures
          oneOf:
            - `MergeTagInvalidIdError` — Error returned when the master tag ID in the URL path is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details identifying the invalid field
                - `api_name` (string) **REQ** [maxLen=255] — Name of the invalid field
                - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the invalid field
                additionalProperties: any
              - `message` (string) **REQ** [enum=['invalid data', 'Invalid data', 'Invalid data type']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `NoPermissionError` — Error indicating that the user does not have permission to perform the operation.

- **403**: Forbidden - The client does not have access rights to perform the operation. [application/json]
    > Wrapped error response with tag-level permission errors
    - `tags` (array of object `NoPermissionError`) [maxItems=25] **REQ** — Array of permission error objects

**Scopes:** ZohoCRM.settings.tags.all

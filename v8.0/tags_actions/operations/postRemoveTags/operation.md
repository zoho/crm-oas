# POST /{module}/actions/remove_tags
**Operation:** `postRemoveTags` — Remove Tags from Records
> Removes tags from one or more records in the specified module.

**Parameters:**
- `module` (query, string, optional) [maxLen=100]: The API name of the module to perform the operation on. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module API names.

- `module` (path, string, required) [maxLen=100]: The API name of the module to perform the operation on. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module API names.


**Schemas:**
`TagsNested1`:
  > Nested schema for tag details in responses.
  - `name` (string) [maxLen=255] — Tag name
  - `id` (string) [maxLen=255] — Unique identifier of the tag
  - `color_code` (string) [maxLen=255, nullable] — Color code of the tag
  - `rid` (string/uuid) — Resource ID

**Request Body** — application/json `PostremovetagsRequest`
> Request body containing the tags to remove and the record IDs.
  > Request body schema for removing tags from records.
  - `ids` (string) [maxLen=99, enum=['["3060320000002496003"]'], nullable] — JSON array string of record IDs to remove tags from. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve record IDs.

  - `tags` (array of object `TagsNested`) [maxItems=1] **REQ** — Array of tags to remove from the records (Required)
    schema: `TagsNested`
    - `name` (string) [maxLen=25, nullable] — Tag name
    - `modified_time` (string/date-time) [maxLen=25, nullable] — Last modification timestamp of the tag
    - `color_code` (string) [maxLen=7, nullable] — Color code of the tag
    - `conflict_id` (string) [maxLen=19, nullable] — ID of the tag to be merged into the master tag

**Responses:**

- **200**: OK - Tags removed successfully. — Schema: `PostremovetagsResponse200` [application/json]
    > Success response when tags are removed from records successfully.
    schema: `PostremovetagsResponse200`
    - `data` (array of object `DataNested`) [maxItems=20] — Array of operation results for each record
      schema: `DataNested`
      - `code` (string) [maxLen=255] — Status code of the operation
      - `details` (object `DetailsNested`) — Nested schema for operation details in responses.
        schema: `DetailsNested`
        - `modifiedTime` (string) [maxLen=255] — Last modified time of the record
        - `id` (string) [maxLen=255] — Unique identifier of the record
        - `affected_data` (null) — Affected data in the operation
        - `tags` (array of object `TagsNested1`) [maxItems=10] — Tags associated with the record
        - `not_added_tags` (array of object `TagsNested1`) [maxItems=10] — Tags that were not added to the record
      - `message` (string) [maxLen=255] — Human-readable message about the operation result
      - `status` (string) [maxLen=255] — Status of the operation (e.g., success, error)
    - `locked_count` (string) [maxLen=255] — Number of records that were locked and could not be updated

- **400**: Bad Request - The request cannot be processed due to invalid syntax or validation errors. Review the error details and correct the issues before retrying. [application/json]
    > Error response for status 400
    oneOf:
        - `data` (array of object `RecordLockedError`) [maxItems=25] **REQ** — Array of error objects for records that failed the operation
          schema: `RecordLockedError`
          - `code` (string) **REQ** [enum=['RECORD_LOCKED']] — Error code
          - `details` (object) **REQ** — Error details with validation information
            - `action` (string) **REQ** [maxLen=255] — Action that was attempted on the locked record
            - `id` (string) **REQ** [maxLen=255] — Unique identifier of the locked record
          - `message` (string) **REQ** [enum=['Sorry, you cannot perform this operation as the record is locked.']] — Error message
          - `status` (string) **REQ** [enum=['error']] — Error status
        - `locked_count` (string) [maxLen=10] — Number of records that are locked and could not be updated
      - `TagsInvalidDataError` — Error indicating invalid data type for the tags field.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `maximum_length` (integer/int32) — Maximum allowed length for the field
          - `api_name` (string) **REQ** [maxLen=255] — API name of the field with invalid data
          - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the field with invalid data
          - `expected_data_type` (string) [maxLen=255] — Expected data type for the field
        - `message` (string) **REQ** [maxLen=255] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidModuleNameError` — Error indicating that the specified module name is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `ModuleTagsNotSupportedError` — Error indicating that the specified module does not support tags.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['the given module is not supported for this api']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidRequestMethodError` — Error indicating that the HTTP request method is invalid.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['The http request method type is not a valid one']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
        - `tags` (array of object) [maxItems=25] **REQ** — Array of error objects for tag field validation failures
          oneOf:
            - `TagFieldInvalidDataTypeError` — Error indicating that a tag field has an invalid data type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) **REQ** [maxLen=255] — Expected data type for the field
                - `api_name` (string) **REQ** [maxLen=255] — API name of the field with invalid data type
                - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the field with invalid data type
              - `message` (string) **REQ** [enum=['Invalid data type']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `TagFieldMaxLengthError` — Error indicating that a tag field exceeds the maximum allowed length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `maximum_length` (integer/int32) **REQ** — Maximum allowed length for the field
                - `api_name` (string) **REQ** [maxLen=255] — API name of the field exceeding max length
                - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the field exceeding max length
              - `message` (string) **REQ** [enum=['Invalid data']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status

- **403**: Forbidden - The client does not have access rights to perform the operation. — Schema: `NoPermissionError` [application/json]
    > Error response for status 403
    schema: `NoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code
    - `details` (object) **REQ** — Error details with validation information
      - `permissions` (array of string) [maxItems=25] **REQ** — List of required permissions
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status

**Scopes:** ZohoCRM.modules.ALL

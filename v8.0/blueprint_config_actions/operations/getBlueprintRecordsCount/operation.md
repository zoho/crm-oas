# GET /settings/blueprints/{blueprintId}/actions/records_count
**Operation:** `getBlueprintRecordsCount` — Retrieve Blueprint stage record counts

> To retrieve the number of records at each Blueprint stage for a specific Blueprint in your Zoho CRM organization.


**Parameters:**
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Specify the name of the service making the API call. Possible values:
automation - Identifies the automation service as the caller.
- `blueprintId` (path, string/bigint, required) [pattern=^[0-9]+]: Specify the unique ID of the Blueprint whose stage-level record counts are to be retrieved.


**Responses:**

- **200**: Returns the record count at each stage of the specified Blueprint.
 — Schema: `BlueprintRecordsCountListResponse` [application/json]
    > Represents the response returned for the records count action. Contains an array of Blueprint entries, each with the current record count.
    schema: `BlueprintRecordsCountListResponse`
    - `blueprints` (array of object `BlueprintRecordsCountItem`) [maxItems=1] **REQ** — Contains the list of Blueprint items with their respective record counts returned in the response.
      schema: `BlueprintRecordsCountItem`
      - `records_count` (integer/int32) **REQ** — Represents the total number of records currently associated with the Blueprint.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The Blueprint ID supplied in the request path is invalid.
**Resolution:** Verify that the Blueprint ID is a valid numeric identifier and resubmit the request.
 [application/json]
    > Represents the error response returned when the Blueprint ID supplied in the request path is invalid. Contains an error code of INVALID_DATA, a message indicating that the ID is invalid, and details identifying the offending path segment index.

    oneOf:
      - `InvalidProcessIDErrorResponse` — Represents an error response returned when the process identifier in the request URL is invalid. Includes error code INVALID_DATA and the invalid path segment index in the details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for this response. Possible values:
INVALID_DATA - Indicates that the provided data is invalid.
        - `details` (object) **REQ** — Contains additional information about the error, including the index of the invalid resource path segment.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the invalid resource path segment in the request URL.
        - `message` (string) **REQ** [enum=['id seems to be invalid']] — Represents the error message returned when the provided process ID is invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values:
error - Indicates the request failed.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.blueprint.READ

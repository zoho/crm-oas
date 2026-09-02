# POST /{moduleApiName}/{recordId}/actions/share
**Operation:** `createShareRecords` — Share a record
> To share a specific record in a module with one or more users, roles, or groups. A record can be shared with up to 10 users, 5 roles, and 5 groups.
> **Note**:
> - The records can be shared to other users in the organization only if certain conditions are met. For simplicity, let us assume that User A shares a record with User B. Now, User A can share the record successfully only if:
>    - User B is a **confirmed** and **active** user.
>    - User B **does not already have access** to that particular record.
>    - User B has access to that particular module. For instance, to share a contact, User B must have access to the Contacts module.
> - You cannot share the records in Calls, Meetings, Tasks, and Linking modules directly. They can be shared as related lists.
> - The users who have profiles with **share** permission can share any records that they have access to, except the records that are shared to them. To check the same, go to Setup > Users and Control > Security Control > Choose the profile > Tool Permissions. Check if **share** is enabled. It is enabled by default for Standard and Administrator Profiles.
> - The details of the records that form many-to-many relationships (with multi-select lookup) cannot be shared.
> - A record can be shared only with **10 users**, **5 groups**, and **5 roles**.
> - Once the record gets shared successfully, the user who initiated the share operation can be notified via email.


**Parameters:**
- `moduleApiName` (path, string, required) [maxLen=50]: Specify the API name of the module that owns the record. Refer to the [Get Modules API](modules.yaml#$.paths./settings/modules.get) for valid values.
- `recordId` (path, string/int64, required): Specify the unique ID of the record. Refer to the [Get Records API](record.yaml#$.paths./{module}.get) for valid values.

**Schemas:**
`ActivityModuleRelatedIssueErrorResponse`:
  > Represents the error response returned when **share_related_records** is set on a module that does not support sharing related records.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code returned by the API. 
  - `details` (object) **REQ** — Represents the additional information about the response. 
    - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the parameter that caused the error.
    - `json_path` (string) **REQ** [maxLen=100] — Represents the JSON path of the parameter that caused the error.
  - `message` (string) **REQ** [enum=['cannot share the related records']] — Represents the response message returned by the API.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call. 
`CreateAndUpdateSuccessResponse`:
  > Represents the per-entry success result of a share record create or update operation.
  - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code returned by the API. 
  - `details` (object) **REQ** — Represents the additional information about the response. 
  - `message` (string) **REQ** [enum=['record will be shared successfully']] — Represents the response message returned by the API. 
  - `status` (string) **REQ** [enum=['success']] — Represents the status of the API call. 
`InvalidShareWithIdErrorResponse`:
  > Represents the error response returned when the recipient ID in **shared_with** is invalid or when the record cannot be shared with the specified entity.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code returned by the API. 
  - `details` (object) **REQ** — Represents the additional information about the response. 
    - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the parameter that caused the error.
    - `json_path` (string) **REQ** [maxLen=100] — Represents the JSON path of the parameter that caused the error.
  - `message` (string) **REQ** [enum=[5 values]] — Represents the response message returned by the API. 

**Possible values**: 
- invalid data
- invalid user Id
- invalid role Id
- invalid group Id
- cannot share to the user

  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call. 
`InvalidShareWithValueErrorResponse`:
  > Represents the error response returned when the **shared_with** object in a share entry is invalid due to a dependent field mismatch.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code returned by the API. 
  - `details` (object) **REQ** — Represents the additional information about the response. 
    - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the parameter that caused the error.
    - `json_path` (string) **REQ** [maxLen=100] — Represents the JSON path of the parameter that caused the error.
    - `dependee` (object) **REQ** — Represents the details of the parameter on which this parameter depends.
      - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the parameter that caused the error.
      - `json_path` (string) **REQ** [maxLen=100] — Represents the JSON path of the parameter that caused the error.
  - `message` (string) **REQ** [enum=['invalid data']] — Represents the response message returned by the API. 
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call. 
`InvalidTypeErrorResponse`:
  > Represents the error response returned when the `type` or `permission` field in a share entry does not match the expected pattern.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code returned by the API. 
  - `details` (object) **REQ** — Represents the additional information about the response. 
    - `api_name` (string) **REQ** [enum=['type', 'permission']] — Represents the API name of the parameter that caused the error. 

**Possible values**: 
- type
- permission

    - `json_path` (string) **REQ** [maxLen=100] — Represents the JSON path of the parameter that caused the error.
    - `regex` (string) **REQ** [enum=['private|public', 'read_only|read_write|full_access']] — Represents the regular expression pattern expected for the parameter value. 
  - `message` (string) **REQ** [enum=['invalid data']] — Represents the response message returned by the API. 
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call. 
`MandatoryNotFound`:
  > Represents the error response returned when a mandatory field is missing from the share entry.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the response code returned by the API. 
  - `details` (object) **REQ** — Represents the additional information about the response. 
    - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the parameter that caused the error.
    - `json_path` (string) **REQ** [maxLen=100] — Represents the JSON path of the parameter that caused the error.
  - `message` (string) **REQ** [enum=['required field not found']] — Represents the response message returned by the API. 
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call. 
`ShareLimitExceedErrorResponse`:
  > Represents the error response returned when the share entry exceeds the per-record sharing limit for the recipient type.
  - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the response code returned by the API.
  - `details` (object) **REQ** — Represents the additional information about the response.
    - `limit` (integer/int32) — Represents the maximum number of share records allowed for the entity type.
    - `api_name` (string) [enum=['type']] — Represents the API name of the parameter that caused the error.
    - `json_path` (string) [maxLen=100] — Represents the JSON path of the parameter that caused the error.
  - `message` (string) **REQ** [maxLen=100] — Represents the response message returned by the API.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.

**Request Body** (required) — application/json
> The request body contains the data required to perform the operation.
  > Represents the request body.
  - `share` (array of object) [maxItems=20] **REQ** — Specify the list of share entries to apply. Each entry defines a recipient, the access level, and the type of sharing. You can provide a maximum of **20** entries in a single request.
    - `type` (string) **REQ** [enum=['private', 'public']] — Specify the type of sharing to apply to the record. 

**Possible values**: 
- private 
- public

    - `share_related_records` (boolean) — Specify whether to share the related records along
with the record. 


**Possible values**: 

- true

- false

    - `permission` (string) **REQ** [enum=['read_only', 'read_write', 'full_access']] — Specify the level of access to grant for the shared
record. 

**Possible values**: 

- read_only

- read_write

- full_access

    - `shared_with` (object) **REQ** — Specify the details of the entity (user, role, or group) with which to share the record.
      oneOf:
          - `type` (string) **REQ** [enum=['roles']] — type of entity with whom the record is shared
          - `id` (string) **REQ** [maxLen=19] — Represents the ID of the role with whom the record is being shared.
          - `type` (string) **REQ** [enum=['groups']] — type of entity with whom the record is shared
          - `id` (string) **REQ** [maxLen=19] — Represents the ID of the group with whom the record is being shared.
          - `type` (string) **REQ** [enum=['users']] — type of entity with whom the record is shared
          - `id` (string) **REQ** [maxLen=19] — Represents the ID of the user with whom the record is being shared.
  - `notify_shared_members` (boolean) — Specify whether to send a notification to the members with
whom the record is shared. 

**Possible values**: 

- true

- false

  - `notify_on_completion` (boolean) — Specify whether to send an email notification to the record
owner once the share action is completed. 

**Possible values**: 

- true

- false


**Responses:**

- **201**: Returns a per-entry success result for each share entry created on the record. [application/json]
    > Represents the success response of the API request.
    - `share` (array of object `CreateAndUpdateSuccessResponse`) [maxItems=20] **REQ** — Represents details of each share record creation result.

- **207**: Returns a per-entry result for each share entry in the request, where each entry is either a success or a specific error. [application/json]
    > Represents the response of partial success.
    - `share` (array of object) [maxItems=20] — Represents the details of each share record creation result.
      oneOf:
        - `CreateAndUpdateSuccessResponse` — Represents the per-entry success result of a share record create or update operation.
        - `items` — Each string represents the per-entry result for one share entry, which can be either a success or a specific error.
          oneOf:
            - `MandatoryNotFound` — Represents the error response returned when a mandatory field is missing from the share entry.
            - `InvalidTypeErrorResponse` — Represents the error response returned when the `type` or `permission` field in a share entry does not match the expected pattern.
            - `InvalidShareWithValueErrorResponse` — Represents the error response returned when the **shared_with** object in a share entry is invalid due to a dependent field mismatch.
            - `InvalidShareWithIdErrorResponse` — Represents the error response returned when the recipient ID in **shared_with** is invalid or when the record cannot be shared with the specified entity.
            - `ActivityModuleRelatedIssueErrorResponse` — Represents the error response returned when **share_related_records** is set on a module that does not support sharing related records.
            - `ShareLimitExceedErrorResponse` — Represents the error response returned when the share entry exceeds the per-record sharing limit for the recipient type.

- **400**: Returns an error response when the request URL, path parameters, or share entries fail validation. — Schema: `CreateAndUpdateShareRecordsBadRequest` [application/json]
    > bad request response
    oneOf:
      - `CreateAndUpdateBadResponseWithShareArray` — Represents the bad request response in which the errors are reported per share entry under the **share** array.
        - `share` (array of object) [maxItems=20] **REQ** — Represents the list of error responses for the share record creation.
          oneOf:
            - `MandatoryNotFound` — Represents the error response returned when a mandatory field is missing from the share entry.
            - `InvalidTypeErrorResponse` — Represents the error response returned when the `type` or `permission` field in a share entry does not match the expected pattern.
            - `InvalidShareWithValueErrorResponse` — Represents the error response returned when the **shared_with** object in a share entry is invalid due to a dependent field mismatch.
            - `InvalidShareWithIdErrorResponse` — Represents the error response returned when the recipient ID in **shared_with** is invalid or when the record cannot be shared with the specified entity.
            - `ActivityModuleRelatedIssueErrorResponse` — Represents the error response returned when **share_related_records** is set on a module that does not support sharing related records.
            - `ShareLimitExceedErrorResponse` — Represents the error response returned when the share entry exceeds the per-record sharing limit for the recipient type.
      - `CreateAndUpdateBadResponseWithoutShareArray` — Represents the bad request response in which the failure applies to the entire request rather than to individual share entries.
        oneOf:
          - `InvalidRecordIdErrorResponse` — Represents the error response returned when the record ID in the request URL is invalid or does not belong to the specified module.
            - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code returned by the API.
            - `details` (object) **REQ** — Represents the additional information about the response.
              - `resource_path_index` (integer/int32) **REQ** [default=1] — Represents the index of the URL path segment that caused the
error. Default value: **1**.

            - `message` (string) **REQ** [enum=['ENTITY_ID_INVALID']] — Represents the response message returned by the API. 
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.
          - `InvalidModuleNameErrorResponse` — Represents the error response returned when the module API name in the request URL is invalid or not supported.
            - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the response code returned by the API.
            - `details` (object) **REQ** — Represents the additional information about the response.
              - `resource_path_index` (integer/int32) **REQ** [default=0] — Represents the index of the URL path segment that caused the
error. Default value: **0**.

            - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the response message returned by the API.
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.
          - `MaximumLengthErrorResponse` — Represents the error response returned when the `share` array in the request exceeds the maximum allowed length.
            - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code returned by the API. 
            - `details` (object) **REQ** — Represents the additional information about the response. 
              - `api_name` (string) **REQ** [enum=['share']] — Represents the API name of the parameter that caused the error. 
              - `json_path` (string) **REQ** [enum=['$.share']] — Represents the JSON path of the parameter that caused the error.
              - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the parameter.
            - `message` (string) **REQ** [enum=['invalid data']] — Represents the response message returned by the API.
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.
          - `UnsupportedModule` — Represents the error response returned when the module specified in the request URL is not supported by the share records API.
            - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the response code returned by the API.
            - `details` (object) **REQ** — Represents the additional information about the response.
              - `resource_path_index` (integer/int32) — Represents the index of the URL path segment that caused the error.
            - `message` (string) **REQ** [maxLen=200] — Represents the response message returned by the API.
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.
          - `AmbiguousShareErrorResponse` — Represents the error response returned when a public share request contains more than one JSON object, which causes ambiguity during processing.
            - `code` (string) [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the response code returned by the API. 
            - `details` (object) — Represents the additional information about the response. 
              - `ambiguity_due_to` (array of object) [maxItems=20] — Represents the list of reasons that caused the ambiguity during processing.
                - `api_name` (string) [maxLen=100] — Represents the API name of the parameter that caused the error.
                - `json_path` (string) [maxLen=100] — Represents the JSON path of the parameter that caused the error.
            - `message` (string) [enum=['For public sharing more than one json object is given']] — Represents the response message returned by the API. 
            - `status` (string) [enum=['error']] — Represents the status of the API call. 

- **403**: Returns an error response when the user does not have permission to perform the share create or when the share operation is blocked by an org-level restriction. [application/json]
    > Represents the response when the user does not have enough permissions.
    oneOf:
      - `CommonForbiddenErrorResponse` — Represents the forbidden error response returned when the user does not have permission to access the API.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the response code returned by the API.
        - `details` (object) **REQ** — Represents the additional information about the response.
        - `message` (string) **REQ** [enum=['permission denied - access the api', 'permission denied']] — Represents the response message returned by the API. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.
      - `SchedularAlreadyRunningErrorResponse` — Represents the error response returned when a share operation cannot be processed because a previous share operation on the record is still in progress.
        - `code` (string) **REQ** [enum=['CANNOT_PROCESS']] — Represents the response code returned by the API.
        - `details` (object) **REQ** — Represents the additional information about the response.
        - `message` (string) **REQ** [enum=['Scheduler is running']] — Represents the response message returned by the API. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.
      - `SharingSharedRecordErrorResponse` — Represents the error response returned when a record that was already shared with the current user cannot be shared again with other users.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code returned by the API.
        - `details` (object) **REQ** — Represents the additional information about the response.
        - `message` (string) **REQ** [enum=['Shared record cannot be shared to other users']] — Represents the response message returned by the API.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.
      - `RecordLevelSharingNotSupportedForModuleErrorResponse` — Represents the error response returned when record-level sharing is not supported for the module specified in the request URL.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the response code returned by the API.
        - `details` (object) **REQ** — Represents the additional information about the response.
        - `message` (string) **REQ** [enum=['Record Level Sharing is not supported for this module']] — Represents the response message returned by the API.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.
      - `NotifyMembersWithoutFeeds` — Represents the error response returned when **notify_shared_members** is requested but Feeds is not enabled or is not supported for the share type.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the response code returned by the API.
        - `details` (object) **REQ** — Represents the additional information about the response.
          - `api_name` (string) [enum=['notify_shared_members']] — Represents the API name of the parameter that caused the error.
          - `json_path` (string) [enum=['$.notify_shared_members']] — Represents the JSON path of the notify_shared_members parameter that caused the error. 
        - `message` (string) **REQ** [enum=[2 values]] — Represents the response message returned by the API. 

**Possible values**: 
- Feeds is not enabled for this org.
- Feeds Notification is not allowed for this type.

        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.
      - `RecordForbiddenErrorResponse` — Represents the forbidden error response returned when the user does not have the required record-level permissions in the specified module.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the response code returned by the API.
        - `details` (object) **REQ** — Represents the additional information about the response.
          - `permissions` (array of string) [maxItems=1] **REQ** — Represents the list of permissions that the user is missing.
            items: [maxLen=200]
        - `message` (string) **REQ** [enum=['permission denied']] — Represents the response message returned by the API.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API call.

**Scopes:** ZohoCRM.share.leads.CREATE, ZohoCRM.share.contacts.CREATE, ZohoCRM.share.accounts.CREATE, ZohoCRM.share.deals.CREATE, ZohoCRM.share.products.CREATE, ZohoCRM.share.tasks.CREATE, ZohoCRM.share.events.CREATE, ZohoCRM.share.calls.CREATE, ZohoCRM.share.quotes.CREATE, ZohoCRM.share.invoices.CREATE, ZohoCRM.share.campaigns.CREATE, ZohoCRM.share.vendors.CREATE, ZohoCRM.share.pricebooks.CREATE, ZohoCRM.share.salesorders.CREATE, ZohoCRM.share.purchaseorders.CREATE, ZohoCRM.share.solutions.CREATE, ZohoCRM.share.cases.CREATE, ZohoCRM.share.bundles.CREATE, ZohoCRM.share.custom.CREATE

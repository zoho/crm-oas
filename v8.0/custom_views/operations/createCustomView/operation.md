# POST /settings/custom_views
**Operation:** `createCustomView` — CustomView creation
> To create one or more Custom Views for a specified module in your Zoho CRM organization.

**Tags:** Custom Views

**Parameters:**
- `module` (query, string, required) [maxLen=25]: Specify the API name of the module for which to manage Custom Views. Refer to the Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module IDs.resource for valid values.

**Schemas:**
`ApiNameDetail`:
  > Represents the API name details for a field in the request or response.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field.
`BetweenFilterCriterionRequest`:
  > Represents a filter criterion for the between and not_between comparators. The value must be an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields. Resolve the data_type from the field's FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `field` (object) **REQ** — Represents the target field definition to which the range filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['between', 'not_between']] — Represents the range comparison operator applied to the criterion, indicating whether the field value falls within or outside the specified bounds.
Possible values:
between - Matches records where the field value falls within the specified range.
not_between - Matches records where the field value falls outside the specified range.
  - `value` (array of object) [minItems=2, maxItems=2] **REQ** — Contains the two boundary values — [lower_bound, upper_bound] — against which the field is evaluated for the between or not_between comparator.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`ComparatorValueMismatch`:
  > Error schema returned when the comparator value itself does not satisfy the dependency validation rules imposed by the dependee field. Carries error code DEPENDENT_MISMATCH and includes details identifying the criterion field with the invalid comparator value, its dependee field (api_name, json_path), and the criterion field own api_name and json_path.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code identifying the comparator dependency mismatch condition. Possible values: DEPENDENT_MISMATCH.
  - `details` (object) **REQ** — Object containing diagnostic detail about the dependency mismatch, including the criterion field with the invalid comparator value (api_name, json_path) and the dependee field that imposed the violated validation rule (dependee.api_name, dependee.json_path).
    - `dependee` (object) **REQ** — Identifies the dependee field whose value determines the validation rules applied to the comparator of the criterion field in error. Contains the API name and JSON path of the dependee field.
      - `api_name` (string) **REQ** [maxLen=256] — API name of the dependee field whose value imposed the violated validation rule on the criterion field comparator.
      - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the dependee field within the request body.
    - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field whose comparator value does not satisfy the dependency rule imposed by the dependee field.
    - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the criterion field with the invalid comparator value within the request body.
  - `message` (string) **REQ** [maxLen=512] — Descriptive message providing details about the comparator value mismatch error.
  - `status` (string) **REQ** [enum=['error']] — Status of the response indicating the outcome of the request. Possible values: error.
`CustomViewCreateFailureItem`:
  oneOf:
    - `InvalidDataForUpdateCV` — Represents the error details returned when the request contains invalid field values for a Custom View update.
    - `MandatoryNotFoundForUpdateCVById` — Represents the error details returned when a required field is missing from a Custom View update request.
    - `DuplicateDataForUpdateCVById` — Represents the error details returned when the request contains duplicate values for a field that requires unique values.
    - `NotAllowedForUpdateCVById` — Represents the error details returned when the update request contains a field that cannot be modified.
    - `SpecialCharacterNotAllowed` — Represents the error details returned when a field value in the request contains special characters that are not allowed.
    - `InvalidIndexFav` — Represents the error details returned when the favorite index value in the request is invalid.
    - `InvalidIdFav` — Represents the error details returned when the Custom View ID in the favorite operation request is invalid.
    - `NotAllowedDetailsUpdate` — Represents the error details returned when a resource cannot be updated due to active associations.
    - `LimitExceededForCreateCV` — Represents the error response returned when the request exceeds the maximum number of Custom Views allowed.
    - `FieldComparatorValueMissing` — Represents the error response returned when a criterion comparator cannot be applied because the comparator value supplied by the dependee field is absent. Carries error code DEPENDENT_FIELD_MISSING along with details identifying both the field in error and the dependee field whose value is missing.
    - `FieldComparatorMismatch` — Error schema returned when the comparator value supplied for a criterion field does not match the valid comparator values determined by its dependee field. Contains the error code DEPENDENT_MISMATCH and a details object identifying the criterion field, its dependee field, and the list of supported comparator values.
    - `FieldValueMismatch` — Represents the error response returned when the data type of the value supplied for a criterion field does not match the expected data type determined by the dependee field. Returned with error code DEPENDENT_MISMATCH. Contains details identifying the mismatched criterion field, its dependee field, and the expected data type.
    - `ComparatorValueMismatch` — Error schema returned when the comparator value itself does not satisfy the dependency validation rules imposed by the dependee field. Carries error code DEPENDENT_MISMATCH and includes details identifying the criterion field with the invalid comparator value, its dependee field (api_name, json_path), and the criterion field own api_name and json_path.
    - `InvalidComparator` — Error schema returned when the comparator specified in a criterion field is not one of the allowed comparator values for the given field type. Returned with error code INVALID_DATA. The details object identifies the offending field by API name and JSON path, and enumerates the supported comparator values.
    - `LookupLimitExceeded` — Represents the error response returned when the count of lookup fields used in criterion expressions exceeds the allowed limit. The error code is LOOKUP_LIMIT_EXCEEDED. The details object contains a used_in array (minItems: 1, maxItems: 10) in which each entry identifies an affected location by name and provides the relevant lookup fields and the applicable lookup limit.
`CustomViewPostSuccessResponse`:
  > Represents the successful creation response for a Custom View, including the status, code, message, and ID details.
  - `status` (string) **REQ** [enum=['success']] — Represents the status of the create response.
Possible values:
**success** - The operation was successful.
  - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the success code for the create operation.
Possible values:
**SUCCESS** - The Custom View creation completed successfully.
  - `details` (object `IdDetail`) **REQ** — Represents the ID details for a created or affected resource.
  - `message` (string) **REQ** [maxLen=255] — Represents the success message for the create operation.
`DataTypeMismatchError`:
  > Represents the error details returned when a field value in the request does not match the expected data type.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with the data type mismatch.
  - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path of the field with the data type mismatch.
  - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field.
`DuplicateDataForUpdateCVById`:
  > Represents the error details returned when the request contains duplicate values for a field that requires unique values.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
  - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the duplicate data issue.
  - `details` (object) **REQ** — Represents the additional details about the duplicate field.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with the duplicate value.
    - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path pointing to the duplicate field in the request body.
  - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code for the duplicate data error.
Possible values:
**DUPLICATE_DATA** - The request contains duplicate values for a field that requires unique values.
`EqualFilterCriterionRequest`:
  > Represents a filter criterion for the equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders. Accepts scalar or array values. Resolve the data_type from the field's FieldSchema.
  - `field` (object) **REQ** — Represents the target field definition to which the equal filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['equal']] — Represents the equal comparison operator applied to the criterion.
Possible values:
equal - Matches records where the field value equals the specified filter value.
  - `value` (object) **REQ** — Represents the filter value used in the equal comparator. Accepts a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueGeneralPredefined` (string) [enum=['${EMPTY}', '${NOTEMPTY}']] — Represents a predefined placeholder value applicable to any field data_type with the equal comparator.
Possible values:
${EMPTY} - Matches records where the field has no value.
${NOTEMPTY} - Matches records where the field has any non-empty value.
      - `SimpleFilterCriterionValueDateTimePredefined` (string) [enum=[22 values]] — Represents a predefined placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator.
      - `SimpleFilterCriterionValueNDaysPredefined` (string) [maxLen=255, pattern=^\$\{(LAST_N_|NEXT_N_)(DAYS|WEEKS|MONTHS|YEARS):([0-9]+)\}$] — Represents a predefined N-period range placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator. Follows the pattern ${NEXT_N_<PERIOD>:<n>} or ${LAST_N_<PERIOD>:<n>}, where PERIOD is DAYS, WEEKS, MONTHS, or YEARS and n is a positive integer. The current period is always excluded from the range.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`EqualityFilterCriterionRequest`:
  oneOf:
    - `EqualFilterCriterionRequest` — Represents a filter criterion for the equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders. Accepts scalar or array values. Resolve the data_type from the field's FieldSchema.
    - `NotEqualFilterCriterionRequest` — Represents a filter criterion for the not_equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
`FieldComparatorMismatch`:
  > Error schema returned when the comparator value supplied for a criterion field does not match the valid comparator values determined by its dependee field. Contains the error code DEPENDENT_MISMATCH and a details object identifying the criterion field, its dependee field, and the list of supported comparator values.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code identifying the type of field comparator mismatch condition. Possible values: DEPENDENT_MISMATCH.
  - `details` (object) **REQ** — Detailed information about the field comparator mismatch, including the API name and JSON path of the criterion field in error, the dependee field that governs valid comparator values, and the array of supported comparator values.
    - `dependee` (object) **REQ** — The dependee field whose value determines which comparator values are valid for the criterion field that raised the DEPENDENT_MISMATCH error. Contains the API name and JSON path of the dependee field.
      - `api_name` (string) **REQ** [maxLen=256] — API name of the dependee field that determines the valid comparator values for the criterion field in error.
      - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the dependee field within the request body.
    - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the criterion field whose comparator value does not match any of the supported values determined by the dependee field.
    - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path locating the criterion field whose comparator value does not match any of the supported values determined by the dependee field.
    - `supported_values` (array of string) [minItems=1, maxItems=100] **REQ** — Contains the comparator values that are valid for the criterion field, as determined by the dependee field.
      items: [maxLen=256]
  - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the comparator mismatch condition for the criterion field.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: error.
`FieldComparatorValueMissing`:
  > Represents the error response returned when a criterion comparator cannot be applied because the comparator value supplied by the dependee field is absent. Carries error code DEPENDENT_FIELD_MISSING along with details identifying both the field in error and the dependee field whose value is missing.
  - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code that identifies the category of failure for this error response.
Possible values:
DEPENDENT_FIELD_MISSING - Indicates that the comparator value required from the dependee criterion field is absent, preventing the comparator from being evaluated.
  - `details` (object) **REQ** — Contains detailed information about the criterion field that caused the error and the dependee field whose comparator value is missing, including the API name and JSON path for each.
    - `dependee` (object) **REQ** — Represents the dependee criterion field — that is, the field whose value determines what the current comparator accepts — and whose missing comparator value triggered this error. Contains the API name and JSON path of that dependee field.
      - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the dependee criterion field whose comparator value is absent and caused the evaluation failure.
      - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path that locates the dependee criterion field within the request body, identifying where the missing comparator value was expected.
    - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field that triggered the DEPENDENT_FIELD_MISSING error.
    - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the criterion field in error within the request body.
  - `message` (string) **REQ** [maxLen=512] — Error message describing the DEPENDENT_FIELD_MISSING condition returned in the response envelope.
  - `status` (string) **REQ** [enum=['error']] — Status of the response. Possible values: error.
`FieldValueMismatch`:
  > Represents the error response returned when the data type of the value supplied for a criterion field does not match the expected data type determined by the dependee field. Returned with error code DEPENDENT_MISMATCH. Contains details identifying the mismatched criterion field, its dependee field, and the expected data type.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code identifying the type of error condition encountered. Possible values: DEPENDENT_MISMATCH.
  - `details` (object) **REQ** — Contains detailed information about the data type mismatch, including the criterion field that raised the error, the dependee field whose value determines the expected data type, and the expected data type itself.
    - `dependee` (object) **REQ** — Represents the dependee field whose value determines the expected data type for the criterion field that raised the mismatch error. Contains the API name and JSON path of the dependee field.
      - `api_name` (string) **REQ** [maxLen=256] — API name of the dependee field that determines the expected data type for the criterion field in error.
      - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the dependee field within the request body.
    - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field whose value does not match the expected data type.
    - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the criterion field whose value contains the data type mismatch.
    - `expected_data_type` (string) **REQ** [maxLen=256] — Data type expected for the criterion field value, as determined by the dependee field.
  - `message` (string) **REQ** [maxLen=512] — Descriptive message providing details about the field value mismatch error.
  - `status` (string) **REQ** [enum=['error']] — Status of the response. Possible values: error.
`FilterCriterionRequest`:
  oneOf:
    - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
    - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
`FilterFieldBase`:
  > Represents the base field reference used in filter operations, containing minimal required properties. The field's data_type is not part of this object; resolve it from the corresponding FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `id` (string/int64) — Represents the unique ID of the field used for filter operations.
  - `api_name` (string) **REQ** — Represents the API name of the field used for filter application. Supports relationship notation, for example, Deals__r.Stage.
  additionalProperties: any
`GroupedFilterCriterionRequest`:
  > Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group` (array of object) [minItems=2, maxItems=25] **REQ** — Contains an array of filter conditions grouped together and evaluated with the specified logical operator.
    oneOf:
      - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
      - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group_operator` (string) **REQ** [enum=['AND', 'OR', 'and', 'or']] — Represents the logical operator applied between the filter conditions in the group.
Possible values:
AND - All conditions in the group must be satisfied.
OR - At least one condition in the group must be satisfied.
and - Equivalent to AND; all conditions in the group must be satisfied.
or - Equivalent to OR; at least one condition in the group must be satisfied.
`IdDetail`:
  > Represents the ID details for a created or affected resource.
  - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique ID of the created or affected resource.
`InvalidComparator`:
  > Error schema returned when the comparator specified in a criterion field is not one of the allowed comparator values for the given field type. Returned with error code INVALID_DATA. The details object identifies the offending field by API name and JSON path, and enumerates the supported comparator values.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code identifying the category of error. Possible values: INVALID_DATA.
  - `details` (object) **REQ** — Contains structured information about the invalid comparator error. Identifies the offending criterion field by API name and JSON path, and provides the list of supported comparator values valid for the given field type.
    - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field for which an invalid comparator was specified.
    - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the criterion field with the invalid comparator within the request body.
    - `supported_values` (array of string) [minItems=1, maxItems=100] **REQ** — Contains the comparator values that are valid for the criterion field type.
      items: [maxLen=256]
  - `message` (string) **REQ** [maxLen=512] — Descriptive error message conveying the nature of the invalid comparator condition to the caller.
  - `status` (string) **REQ** [enum=['error']] — Status of the response indicating the outcome of the request. Possible values: error.
`InvalidDataForUpdateCV`:
  > Represents the error details returned when the request contains invalid field values for a Custom View update.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
  - `message` (string) **REQ** [maxLen=255, enum=[5 values]] — Represents the error message describing the invalid data.
  - `details` (object) **REQ** — Represents the additional details about the invalid field.
    oneOf:
      - `SimpleFieldError` — Represents the error details for an invalid or missing field, including the API name and JSON path.
      - `ApiNameDetail` — Represents the API name details for a field in the request or response.
      - `DataTypeMismatchError` — Represents the error details returned when a field value in the request does not match the expected data type.
      - `InvalidTypeRegexValidationError` — Represents the validation error details returned when a field value fails regex pattern validation due to an incorrect data type.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the invalid data error.
Possible values:
**INVALID_DATA** - The request contains invalid field values.
`InvalidIdFav`:
  > Represents the error details returned when the Custom View ID in the favorite operation request is invalid.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
  - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid ID.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the invalid ID error.
Possible values:
**INVALID_DATA** - The Custom View ID in the request is invalid.
  - `details` (object) **REQ** — Represents the additional details about the invalid Custom View ID.
    - `id` (string/int64) **REQ** [maxLen=25] — Represents the invalid Custom View ID.
`InvalidIndexFav`:
  > Represents the error details returned when the favorite index value in the request is invalid.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
  - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid favorite index.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the invalid index error.
Possible values:
**INVALID_DATA** - The favorite index value in the request is invalid.
  - `details` (object `ApiNameDetail`) **REQ** — Represents the API name details for a field in the request or response.
`InvalidTypeRegexValidationError`:
  > Represents the validation error details returned when a field value fails regex pattern validation due to an incorrect data type.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field for which the regex pattern validation failed.
  - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the field that failed regex pattern validation.
  - `regex` (string) **REQ** [maxLen=255] — Represents the expected regex pattern that the field value was required to match.
  - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the field to pass regex pattern validation.
`LimitExceededForCreateCV`:
  > Represents the error response returned when the request exceeds the maximum number of Custom Views allowed.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
  - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the Custom View limit.
  - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code for the limit exceeded error.
Possible values:
**LIMIT_EXCEEDED** - The maximum number of Custom Views allowed for the edition has been reached.
  - `details` (object) **REQ** — Represents the additional details for this error type. No structured detail data exists for this error.
`LookupLimitExceeded`:
  > Represents the error response returned when the count of lookup fields used in criterion expressions exceeds the allowed limit. The error code is LOOKUP_LIMIT_EXCEEDED. The details object contains a used_in array (minItems: 1, maxItems: 10) in which each entry identifies an affected location by name and provides the relevant lookup fields and the applicable lookup limit.
  - `code` (string) **REQ** [enum=['LOOKUP_LIMIT_EXCEEDED']] — Identifies the error code that signals the lookup field limit has been exceeded. Possible values: LOOKUP_LIMIT_EXCEEDED.
  - `details` (object) **REQ** — Provides structured information about the locations where the lookup field count exceeded the allowed limit. The required used_in array contains objects that each specify a location name (such as "criteria" or "cross_filters"), the lookup fields in use, and the applicable lookup limit.
    - `used_in` (array of object) [minItems=1, maxItems=10] **REQ** — Lists the locations (for example, "criteria" or "cross_filters") where lookup field usage exceeded the allowed limit. Each entry in the array contains a location name, the lookup fields involved, and the applicable lookup limit. The array contains between 1 and 10 items.
      - `name` (string) **REQ** [maxLen=256] — Identifies the location — such as criteria or cross_filters — where the lookup field count exceeded the allowed limit.
      - `lookup_fields` (array of object) [minItems=1, maxItems=100] **REQ** — Lists the lookup fields present in the specified location that contributed to exceeding the allowed lookup field limit. Contains between 1 and 100 entries, each identifying a single lookup field by its API name.
        - `api_name` (string) **REQ** [maxLen=256] — Specifies the API name of a lookup field that was counted against the lookup field limit for the specified location.
      - `lookup_limit` (integer/int32) **REQ** — Specifies the maximum number of lookup fields permitted in the associated location, such as criteria or cross_filters.
  - `message` (string) **REQ** [maxLen=512] — Contains a descriptive error message explaining why the lookup field limit was exceeded.
  - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the request. Possible values: error.
`MandatoryNotFoundForUpdateCVById`:
  > Represents the error details returned when a required field is missing from a Custom View update request.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
  - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing required field.
  - `details` (object) **REQ** — Represents the additional details about the missing required field.
    oneOf:
      - `SimpleFieldError` — Represents the error details for an invalid or missing field, including the API name and JSON path.
      - `ApiNameDetail` — Represents the API name details for a field in the request or response.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for the missing required field.
Possible values:
**MANDATORY_NOT_FOUND** - A required field is missing from the update request.
`MultiSelectLookupFilterCriterionRequest`:
  > Represents a filter criterion for the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup. The value must be an array of SimpleFilterCriterionValueObjectRequest lookup objects.
  - `field` (object) **REQ** — Represents the target field definition to which the multi-select lookup filter criterion is applied. The field must have a data_type of multiuserlookup or multiselectlookup.
  - `comparator` (string) **REQ** [enum=['include_all', 'include_any', 'exclude_all', 'exclude_any']] — Represents the multi-select lookup comparison operator applied to the criterion. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
Possible values:
include_all - Matches records that include all specified lookup values.
include_any - Matches records that include at least one of the specified lookup values.
exclude_all - Matches records that exclude all specified lookup values.
exclude_any - Matches records that exclude at least one of the specified lookup values.
  - `value` (array of object `SimpleFilterCriterionValueObjectRequest`) [minItems=1, maxItems=5] **REQ** — Contains an array of lookup object references used in the multi-select comparison.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`NotAllowedDetails`:
  > Represents the details of associations that prevent the deletion of a Custom View, including the association type and the list of associated resources.
  - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique ID of the Custom View that cannot be deleted.
  - `associations` (array of object) [maxItems=50] **REQ** — Represents the list of associations that prevent the deletion of the Custom View.
    - `type` (string) **REQ** [maxLen=50] — Represents the association type, indicating the feature or module the resource belongs to.
    - `resources` (array of object) [maxItems=100] **REQ** — Represents the list of resources associated with this association type.
      - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique identifier of the associated resource.
      - `name` (string) **REQ** [maxLen=255] — Represents the display name of the associated resource.
`NotAllowedDetailsUpdate`:
  > Represents the error details returned when a resource cannot be updated due to active associations.
  - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the update is not allowed.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
  - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the not allowed update.
Possible values:
**NOT_ALLOWED** - The resource cannot be updated because it has active associations.
  - `details` (object `NotAllowedDetails`) **REQ** — Represents the details of associations that prevent the deletion of a Custom View, including the association type and the list of associated resources.
`NotAllowedForUpdateCVById`:
  > Represents the error details returned when the update request contains a field that cannot be modified.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
  - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the update is not allowed.
  - `details` (object) **REQ** — Represents the additional details about the field that triggered the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the NOT_ALLOWED error.
    - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path pointing to the field that triggered the NOT_ALLOWED error.
  - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the not allowed update.
Possible values:
**NOT_ALLOWED** - The specified field cannot be updated.
`NotEqualFilterCriterionRequest`:
  > Represents a filter criterion for the not_equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the not-equal filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['not_equal']] — Represents the not-equal comparison operator applied to the criterion.
Possible values:
not_equal - Matches records where the field value does not equal the specified filter value.
  - `value` (object) **REQ** — Represents the filter value used in the not_equal comparator. Accepts a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`OrderingFilterCriterionRequest`:
  > Represents a filter criterion for the less_than, less_equal, greater_than, and greater_equal comparators. The value must be a scalar; arrays and objects are not supported. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the ordering filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['less_than', 'less_equal', 'greater_than', 'greater_equal']] — Represents the ordering comparison operator applied to the criterion.
Possible values:
less_than - Matches records where the field value is less than the specified filter value.
less_equal - Matches records where the field value is less than or equal to the specified filter value.
greater_than - Matches records where the field value is greater than the specified filter value.
greater_equal - Matches records where the field value is greater than or equal to the specified filter value.
  - `value` (object) **REQ** — Represents the scalar filter value used in the ordering comparator. Arrays and objects are not supported for ordering comparators.
    anyOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`SetFilterCriterionRequest`:
  > Represents a filter criterion for the in and not_in comparators. The value must be an array of primitive values. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text-based types, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the set filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['in', 'not_in']] — Represents the set membership comparison operator applied to the criterion.
Possible values:
in - Matches records where the field value is in the specified set of values.
not_in - Matches records where the field value is not in the specified set of values.
  - `value` (array of object) [minItems=1, maxItems=500] **REQ** — Contains an array of primitive filter values used in the set comparison.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`SimpleFieldError`:
  > Represents the error details for an invalid or missing field, including the API name and JSON path.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
  - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path pointing to the invalid field in the request.
`SimpleFilterCriterionRequest`:
  oneOf:
    - `EqualityFilterCriterionRequest` — Represents an equality filter criterion that dispatches to either the EqualFilterCriterionRequest or NotEqualFilterCriterionRequest schema based on the comparator value.
    - `TextFilterCriterionRequest` — Represents a filter criterion for the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value must be a string scalar or array; use SimpleFilterCriterionValueString for text-based field types. Object and Boolean values are not supported. Resolve the data_type from the field's FieldSchema.
    - `OrderingFilterCriterionRequest` — Represents a filter criterion for the less_than, less_equal, greater_than, and greater_equal comparators. The value must be a scalar; arrays and objects are not supported. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `BetweenFilterCriterionRequest` — Represents a filter criterion for the between and not_between comparators. The value must be an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields. Resolve the data_type from the field's FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
    - `SetFilterCriterionRequest` — Represents a filter criterion for the in and not_in comparators. The value must be an array of primitive values. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text-based types, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `MultiSelectLookupFilterCriterionRequest` — Represents a filter criterion for the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup. The value must be an array of SimpleFilterCriterionValueObjectRequest lookup objects.
`SimpleFilterCriterionValueObjectBase`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (string/int64) — Represents the unique ID of the lookup module record.
  - `name` (string) [maxLen=255] — Represents the display name of the lookup module record.
  additionalProperties: any
`SimpleFilterCriterionValueObjectPredefined`:
  oneOf:
      - `name` (string) **REQ** [enum=['${CURRENTUSER}']] — Represents the predefined placeholder for the currently logged-in user.
Possible values:
${CURRENTUSER} - Represents the currently logged-in user.
      - `id` (string) **REQ** [enum=['${CURRENTUSERROLE}']] — Represents the predefined placeholder for the logged-in user's role record ID.
Possible values:
${CURRENTUSERROLE} - Represents the role of the currently logged-in user.
      - `name` (string) [maxLen=255] — Represents an optional display label for the predefined role, such as Logged in User Role.
      additionalProperties: any
`SimpleFilterCriterionValueObjectRequest`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (object) **REQ**
  - `name` (string) [maxLen=255] — Represents the display name of the lookup module record.
  additionalProperties: any
`SpecialCharacterNotAllowed`:
  > Represents the error details returned when a field value in the request contains special characters that are not allowed.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
  - `message` (string) **REQ** [maxLen=255, enum=['Special Characters are not allowed']] — Represents the error message indicating that special characters are not allowed.
Possible values:
**Special Characters are not allowed** - The field value contains invalid special characters.
  - `code` (string) **REQ** [enum=['INVALID_DATAS']] — Represents the error code for the special character error.
Possible values:
**INVALID_DATAS** - The request contains special characters that are not allowed.
  - `details` (object `SimpleFieldError`) **REQ** — Represents the error details for an invalid or missing field, including the API name and JSON path.
`TextFilterCriterionRequest`:
  > Represents a filter criterion for the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value must be a string scalar or array; use SimpleFilterCriterionValueString for text-based field types. Object and Boolean values are not supported. Resolve the data_type from the field's FieldSchema.
  - `field` (object) **REQ** — Represents the target field definition to which the text filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['like', 'not_like', 'starts_with', 'ends_with', 'contains', 'not_contains']] — Represents the text comparison operator applied to the criterion.
Possible values:
like - Matches records where the field value contains the specified pattern.
not_like - Matches records where the field value does not contain the specified pattern.
starts_with - Matches records where the field value begins with the specified string.
ends_with - Matches records where the field value ends with the specified string.
contains - Matches records where the field value contains the specified string.
not_contains - Matches records where the field value does not contain the specified string.
  - `value` (object) **REQ** — Represents the string filter value used in the text comparator. Accepts a scalar string or an array of string values.
    oneOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.

**Request Body** (required) — application/json
> The request body must contain a custom_views array with one or more objects, each specifying the configuration for a new Custom View.
  > Represents the request body envelope for creating one or more Custom Views.
  - `custom_views` (array of object `CustomViewPostItem`) [maxItems=200] **REQ** — Specify the list of Custom Views to create.
    schema: `CustomViewPostItem`
    - `name` (string) **REQ** [maxLen=50] — Represents the name of the Custom View.
    - `access_type` (string) **REQ** [enum=['shared', 'public', 'only_to_me']] — Represents the access type for the Custom View.
Possible values:
**shared** - The view is shared with selected users, roles, groups, or territories.
**public** - The view is accessible to all users in the organization.
**only_to_me** - The view is private and accessible only to the creator.
    - `category` (string) [enum=['public_views', 'other_users_views', 'shared_with_me', 'created_by_me']] — Represents the category for the Custom View.
Possible values:
**public_views** - Views accessible to all users in the organization.
**other_users_views** - Views created by other users in the organization.
**shared_with_me** - Views shared with the current user.
**created_by_me** - Views created by the current user.
    - `locked` (boolean) — Indicates whether the Custom View is locked.
Possible values:
**true** - The view is locked.
**false** - The view is not locked.
    - `favorite` (integer/int32) [nullable] — Represents the favorite order for the Custom View. A null value indicates the view is not marked as a favorite.
    - `criteria` (object `CustomViewCriterionRequest`) — Represents the filter criteria of the Custom View
      oneOf:
        - `FilterCriterionRequest` — Represents the top-level filter criterion for data selection, supporting both simple field-based filters and complex grouped filters with logical operators.
          type: null — No criteria applied - the custom view returns all records
    - `cross_filters` (object `CustomViewCrossFilterCriterionRequest`) — Represents the cross-filter criteria of the Custom View
      oneOf:
        - `CrossFiltersRequest` — Represents a list of cross-filter objects that filter Custom View records based on related module records' criteria.
          type: array of object [minItems=0, maxItems=3]
            - `include_objects` (boolean) **REQ** — Indicates whether records with matching related records are included in the results.
            - `relation` (object `ChildRelationshipReference`) **REQ** — Represents the reference to a child relationship module. The api_name property is required to identify the child relationship.
              schema: `ChildRelationshipReference`
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the child relationship module used to identify the relationship.
              - `id` (string/int64) [maxLen=25] — Represents the unique ID of the child relationship module record.
              - `$disrupted` (boolean) — Indicates whether the related module relationship referenced by this criterion is in a disrupted state, typically due to an unresolvable or deleted relationship definition.
            - `criteria` (object `FilterCriterionRequest`) **REQ** — Represents the top-level filter criterion for data selection, supporting both simple field-based filters and complex grouped filters with logical operators.
          type: null — No cross-filter criteria applied
    - `shared_to` (array of object) [maxItems=250, nullable] — Represents the list of users, roles, groups, or territories the Custom View is shared with.
      - `name` (string) [maxLen=255] — Name of the user/group
      - `id` (string/int64) **REQ** [maxLen=25] — ID of the user/group
      - `type` (string) **REQ** [enum=['territories', 'roles', 'groups', 'users']] — Represents the type of the shared-to entity.
Possible values:
**territories** - The view is shared with a territory.
**roles** - The view is shared with a role.
**groups** - The view is shared with a group.
**users** - The view is shared with a specific user.
      - `subordinates` (boolean) [nullable] — Specify true if subordinates are included, false otherwise
    - `sort_by` (object) — Represents the field used to sort the records in the Custom View.
      oneOf:
        - `FieldReference` — Represents a reference to a field in the Custom View, identified by its API name and unique ID.
          - `api_name` (string) [maxLen=255, nullable] — Represents the API name of the field. A null value indicates no field is selected.
          - `id` (string/int64) [maxLen=25, nullable] — Represents the unique ID of the field. A null value indicates no field is selected.
          type: null — No sort is applied
    - `sort_order` (object) — Represents the sort order applied to the records in the Custom View.
      oneOf:
          type: string [enum=['asc', 'desc']] — Represents the sort order for the Custom View.
Possible values:
**asc** - Ascending order.
**desc** - Descending order.
          type: null — Represents no sort order applied to the Custom View.
    - `wrap_text` (boolean) — Indicates whether text wrapping is enabled for the Custom View.
Possible values:
**true** - Text wrapping is enabled.
**false** - Text wrapping is disabled.
    - `fields` (array of object) [maxItems=250] **REQ** — Represents the list of fields included in the Custom View, each with display and pin configuration details.
      - `api_name` (string) [maxLen=255, nullable] — Represents the API name of the field included in the Custom View.
      - `id` (string/int64) [maxLen=25, nullable] — Represents the unique ID of the field included in the Custom View.
      - `_pin` (boolean) — Indicates whether the field is pinned in the Custom View.
Possible values:
**true** - The field is pinned.
**false** - The field is not pinned.
      - `_width` (integer/int32) — Represents the display width of the field in pixels.
      - `_pin_order` (integer/int32) — Represents the order of the pinned field within the Custom View.

**Responses:**

- **201**: Returns the details of the Custom Views created successfully. [application/json]
    > Represents the bulk create success response schema for Custom View creation.
    - `custom_views` (array of object `CustomViewPostSuccessResponse`) [maxItems=200] **REQ** — Represents the list of Custom Views created successfully.

- **207**: Returns a multi-status response when the bulk creation partially succeeded. Each item indicates whether the creation succeeded or failed for that Custom View. [application/json]
    > Represents the multi-status response for bulk Custom View creation, containing a mix of success and failure items.
    - `custom_views` (array of object) [minItems=2, maxItems=200] **REQ** — Represents the list of Custom View creation results, including both successful and failed items.
      oneOf:
        - `CustomViewPostSuccessResponse` — Represents the successful creation response for a Custom View, including the status, code, message, and ID details.
        - `CustomViewCreateFailureItem` — Represents the creation failure details for a Custom View, containing the error code, status, message, and additional context.

- **400**: The request contains invalid data or a required parameter is missing. Resolution: Verify that all required fields are present and contain valid values. [application/json]
    > Represents the error response for an invalid create Custom View request.
    oneOf:
      - `RequiredParameterMissingResponse` — Flat error: required query parameter missing
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for the missing required parameter.
Possible values:
**REQUIRED_PARAM_MISSING** - A required query parameter is absent from the request.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing parameter.
        - `details` (object) **REQ** — Represents the details of the missing parameter.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the missing required parameter.
      - `UrlErrorResponseForCustomView` — Flat error: URL/module validation failures
        oneOf:
          - `UnableToParseDataTypeError` — Data type could not be parsed from the request
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
            - `code` (string) **REQ** [enum=['UNABLE_TO_PARSE_DATA_TYPE']] — Represents the error code for the data type parse failure.
Possible values:
**UNABLE_TO_PARSE_DATA_TYPE** - The server could not parse the data type from the request.
            - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the data type parse failure.
            - `details` (object) **REQ** — Represents the additional details about the data type parse failure.
          - `InvalidUrlPatternError` — Request URL does not match any known pattern
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
            - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code for the invalid URL pattern.
Possible values:
**INVALID_URL_PATTERN** - The request URL does not match any known pattern.
            - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the URL pattern issue.
            - `details` (object) **REQ** — Represents the additional details about the URL pattern error.
          - `InvalidModuleError` — The specified module is invalid or does not exist
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
            - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for the invalid module error.
Possible values:
**INVALID_MODULE** - The specified module does not exist or is invalid.
            - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid module.
            - `details` (object) **REQ** — Represents the additional details about the invalid module error.
              - `param_name` (string) [maxLen=255] — Name of the invalid parameter
      - `CustomViewCreateFailureResponse` — Wrapped error: per-item creation failures inside custom_views array
        - `custom_views` (array of object `CustomViewCreateFailureItem`) [maxItems=200] **REQ** — Represents the list of Custom View creation failure items, one entry per failed Custom View.

- **401**: Authentication failed or the OAuth access token does not include the required scope. Resolution: A new access token must be generated with the ZohoCRM.settings.custom_views.CREATE scope. [application/json]
    > Represents the error response for an unauthorized create Custom View request.
    oneOf:
      - `AuthenticationError` — Represents the error response returned when the authentication ticket is invalid or missing.
        - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the authentication failure.
Possible values:
**AUTHENTICATION_FAILURE** - The authentication ticket is invalid or missing.
        - `details` (object) **REQ** — Represents the error details containing validation information about the authentication failure.
        - `message` (string) **REQ** [enum=['Authentication failed']] — Represents the error message for the authentication failure.
Possible values:
**Authentication failed** - The provided authentication credentials are invalid or missing.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an authentication error.
      - `UnauthorizedResponse` — Represents the error response returned when the request is unauthorized due to an OAuth scope mismatch.
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code for the OAuth scope mismatch.
Possible values:
**OAUTH_SCOPE_MISMATCH** - The access token does not include the required scope for this operation.
        - `message` (string) **REQ** [maxLen=1024] — Represents the error message indicating the request is unauthorized due to an OAuth scope mismatch.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an authorization error.
        - `details` (object) **REQ** [maxProperties=0] — Represents the additional details for this error. An empty object indicates no additional details are available.
      - `CvProfilePermissionError` — Represents the error response returned when the user does not have the required profile permission to perform the operation.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered a permission error.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the permission denial.
        - `details` (object) **REQ** — Represents the additional details about the permission error.
          - `permissions` (array of string) [maxItems=25] — List of CRM permission keys that are missing for the operation
            items: [maxLen=255]
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the permission denial.
Possible values:
**NO_PERMISSION** - The user does not have the required profile permission to perform the operation.

- **403**: Permission denied to create Custom Views for this module. Resolution: The CRM administrator must grant the required permission to the user's profile. [application/json]
    > Represents the error response for a forbidden create Custom View request.
    oneOf:
      - `ModuleForbiddenErrorResponse` — Represents the error response returned when the user does not have the required permissions for the specified module.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the permission error.
Possible values:
**NO_PERMISSION** - The user does not have the required permission for this module.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the permission denial.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered a permission error.
        - `details` (object) **REQ** — Represents the additional details about the permission error, including the required permissions.
          - `permissions` (array of string) [maxItems=50] **REQ** — Represents the list of permissions required to perform the action on this module.
            items: [maxLen=255]
      - `ForbiddenErrorResponse` — Represents the error response returned when permission is denied for accessing or modifying locked Custom Views.
        - `custom_views` (array of object) [maxItems=200] **REQ** — Represents the list of permission error details for each Custom View in the request.
          - `code` (string) **REQ** [maxLen=50, enum=['NO_PERMISSION']] — Represents the error code identifying the permission issue.
Possible values:
**NO_PERMISSION** - The user does not have permission to access or modify the Custom View.
          - `details` (object `SimpleFieldError`) **REQ** — Represents the error details for an invalid or missing field, including the API name and JSON path.
          - `message` (string) **REQ** [maxLen=200] — Represents the error message describing the permission denial for this Custom View.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered a permission error.

**Scopes:** ZohoCRM.settings.custom_views.CREATE

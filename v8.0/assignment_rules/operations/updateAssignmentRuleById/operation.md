# PUT /settings/automation/assignment_rules/{id}
**Operation:** `updateAssignmentRuleById` — Update a Specific Assignment Rule
> To update a single Assignment Rule in your Zoho CRM organization.

**Parameters:**
- `id` (path, string, required) [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$]: Specify the request path param ID value for the request. Use the [Assignment Rule API](assignment_rules.yaml#$.paths./settings/automation/assignment_rules.get) to retrieve the Assignment Rule ID.
- `module` (query, string, required) [maxLen=100]: Specify the param query module required schema value for the request. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name.

**Schemas:**
`AssignToRequestObject`:
  oneOf:
    - `ZiaSuggestedUsersTypeAssignToRequestObject` — Assigns ownership using Zia AI suggestions. No resource configuration needed.
    - `RoleTypeAssignToRequestObject` — Assigns ownership to a role. All users under the specified role are eligible for assignment.
    - `GroupTypeAssignToRequestObject` — Assigns ownership to a group. All users within the specified group are eligible for assignment.
    - `ProfileTypeAssignToRequestObject` — Assigns ownership to a profile. All users under the specified profile are eligible for assignment.
    - `UsersTypeAssignToRequestObject` — Defines the criteria and list of users eligible for record assignment upon entering the current rule entry.
    - `CriteriaTypeAssignToRequestObject` — Defines the criteria and list of users eligible for record assignment upon entering the current rule entry.
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
`CriteriaTypeAssignToRequestObject`:
  > Defines the criteria and list of users eligible for record assignment upon entering the current rule entry.
  - `type` (string) **REQ** [maxLen=255, enum=['criteria']] — Defines which set of users should be considered for assignment.
Possible values:
**criteria** - Represents criteria.
  - `criteria` (object) **REQ** [nullable] — Defines the criteria of the users who is considered for owner assignment for records entering the current rule entry.
`DetailsWithExpectedDataTypeInfo`:
  > Error details.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
  - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type returned for the Assignment Rule operation. 
`DetailsWithInvalidFieldInfo`:
  > Error details.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
`DetailsWithMaximumLengthInfo`:
  > Error details.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
  - `maximum_length` (integer/int32) **REQ** — Represents the maximum length returned for the Assignment Rule operation. 
`DetailsWithMinimumLengthInfo`:
  > Error details.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
  - `minimum_length` (integer/int32) **REQ** — Represents the minimum length returned for the Assignment Rule operation. 
`DetailsWithResourcePathIndexInfo`:
  > Error details.
  - `resource_path_index` (integer/int32) **REQ** [enum=[3]] — Index of the invalid request path parameter.
Possible values:
**3** - Represents 3. 
`DetailsWithSupportedValuesInfo`:
  > Error details.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
  - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the supported values returned for the Assignment Rule operation. 
    items: [maxLen=255]
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
`ErrorResponseInvalidData`:
  > Invalid data.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**INVALID_DATA** - Represents invalid data.
  - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
    oneOf:
      - `DetailsWithResourcePathIndexInfo` — Error details.
      - `DetailsWithExpectedDataTypeInfo` — Error details.
      - `DetailsWithMinimumLengthInfo` — Error details.
      - `DetailsWithMaximumLengthInfo` — Error details.
      - `DetailsWithSupportedValuesInfo` — Error details.
      - `DetailsWithInvalidFieldInfo` — Error details.
  - `message` (string) **REQ** [maxLen=255] — Represents the message that describes the result of the Assignment Rule operation.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
`FilterCriterionRequest`:
  oneOf:
    - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
    - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
`FilterFieldBase`:
  > Represents the base field reference used in filter operations, containing minimal required properties. The field's data_type is not part of this object; resolve it from the corresponding FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `id` (string/int64) — Represents the unique ID of the field used for filter operations.
  - `api_name` (string) **REQ** — Represents the API name of the field used for filter application. Supports relationship notation, for example, Deals__r.Stage.
  additionalProperties: any
`FollowupActionsRequestObject`:
  oneOf:
    - `TaskTypeFollowupActionRequestObject` — Followup action that creates a task after ownership assignment.
`GroupResourceRequestObject`:
  > Details of the group to assign
  - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — Specify the ID of the group. Refer to the [User Groups](user_groups.yaml#$.paths./settings/user_groups.get) resource for valid values.
`GroupTypeAssignToRequestObject`:
  > Assigns ownership to a group. All users within the specified group are eligible for assignment.
  - `type` (string) **REQ** [enum=['group']] — Assign to type IDentifier. Must be 'group'.
Possible values:
**group** - Represents group.
  - `resource` (object `GroupResourceRequestObject`) **REQ** — Details of the group to assign
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
`ProfileResourceRequestObject`:
  > Details of the profile to assign
  - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — Specify the iD of the profile. Refer to the [Profiles API](profiles.yaml#$.paths./settings/profiles.get) resource for valid values.
`ProfileTypeAssignToRequestObject`:
  > Assigns ownership to a profile. All users under the specified profile are eligible for assignment.
  - `type` (string) **REQ** [enum=['profile']] — Assign to type IDentifier. Must be 'profile'.
Possible values:
**profile** - Represents profile.
  - `resource` (object `ProfileResourceRequestObject`) **REQ** — Details of the profile to assign
`RecordCriteriaSchema`:
  oneOf:
    - `FilterCriterionRequest` — Represents the top-level filter criterion for data selection, supporting both simple field-based filters and complex grouped filters with logical operators.
      type: null — To remove criteria from an existing rule entry, set criteria as null in update request.
`RoleResourceRequestObject`:
  > Details of the role to assign
  - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — Specify the iD of the role. Refer to the [Roles](roles.yaml#$.paths./settings/roles.get) resource for valid values.
`RoleTypeAssignToRequestObject`:
  > Assigns ownership to a role. All users under the specified role are eligible for assignment.
  - `type` (string) **REQ** [enum=['role']] — Assign to type IDentifier. Must be 'role'.
Possible values:
**role** - Represents role.
  - `resource` (object `RoleResourceRequestObject`) **REQ** — Details of the role to assign
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
`TaskResourceRequestObject`:
  > Task resource reference for followup action.
  - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — Specify the iD of the task.
`TaskTypeFollowupActionRequestObject`:
  > Followup action that creates a task after ownership assignment.
  - `type` (string) **REQ** [enum=['tasks']] — Followup action type. Must be 'tasks'.
Possible values:
**tasks** - Represents tasks.
  - `resources` (array of object `TaskResourceRequestObject`) [minItems=1, maxItems=1] — Specify the list of task resources to execute as followup.
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
`UserResourceRequestObject`:
  > User resource reference for Assignment Rule entry.
  - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — Specify the iD of the user. Refer to the [Users API](users.yaml#$.paths./users.get) resource for valid values.
`UsersTypeAssignToRequestObject`:
  > Defines the criteria and list of users eligible for record assignment upon entering the current rule entry.
  - `type` (string) **REQ** [enum=['users']] — If assign to type is users.
Possible values:
**users** - Represents users.
  - `resources` (array of object `UserResourceRequestObject`) [minItems=1, maxItems=50] **REQ** — Defines the list of users details.
`ZiaSuggestedUsersTypeAssignToRequestObject`:
  > Assigns ownership using Zia AI suggestions. No resource configuration needed.
  - `type` (string) **REQ** [enum=['zia_suggested_users']] — Assign to type IDentifier. Must be 'zia_suggested_users'.
Possible values:
**zia_suggested_users** - Represents zia suggested users.

**Request Body** — application/json `RequestBodySchemaForUpdate`
> The request body must contain an **assignment_rules** array with one object. Specify the Assignment Rule fields or rule entries to update.
  > Request body for creating Assignment Rule.
  - `assignment_rules` (array of object) [minItems=1, maxItems=1] **REQ** — Array of Assignment Rule objects to be created.
    - `api_name` (string) [maxLen=100, minLen=1] — Specify the aPI name of the rule.
    - `name` (string) [maxLen=100, minLen=1] — Specify the name to be displayed for the Assignment Rule.
    - `description` (string) [maxLen=250] — Purpose of the Assignment Rule.
    - `rule_entries` (array of object) [minItems=1, maxItems=200] — Specify the list of rule entries for creation, update or deletion. To delete an existing rule entry, provide the ID of the rule entry to be deleted and set _delete field as null in the request body. To update an existing rule entry, provide the ID of the rule entry to be updated along with the fields to be updated in the request body. To create a new rule entry, do not provide ID field and provide details of the new rule entry in the request body.
      oneOf:
        - `RuleEntryDeleteRequestObject` — Rule entry request object to delete.
          - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — ID of the resource.
          - `_delete` (null) **REQ** — To delete an existing rule entry, provide the ID of the rule entry to be deleted and set _delete field as null in the request body.
        - `RuleEntryUpdateRequestObject` — Rule entry request object to update.
          - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — ID of the resource.
          - `criteria` (object `RecordCriteriaSchema`) — Defines the record criteria based on which records will be filtered and assignment logic defined for current rule entry will be applied. If criteria is not provided or is null, all records entering current rule entry will be assigned based on current rule entry's assignment logic.
          - `assign_to` (object `AssignToRequestObject`) — This field defines the set of users to whom the records that enter the current rule entry must be assigned.  (Required)
          - `user_availability_based_on` (array of string) [maxItems=2, nullable] — Defines additional availability checks to be performed before choosing a user as owner. A user is assigned as owner only if it satisfies the mentioned availability conditions.
            items: [enum=['online_status', 'shift_timing']]
          - `followup_actions` (array of object `FollowupActionsRequestObject`) [minItems=1, maxItems=1, nullable] — Defines the list of different actions to be executed after owner assignment.
          - `allow_agent_user` (boolean) — Indicates whether Digital Employee (agent) users are eligible for assignment in this rule entry.
        - `RuleEntryCreateRequestObject` — Defines entries with matching and assignment logic for record processing.
          - `criteria` (object `RecordCriteriaSchema`) — Defines the record criteria based on which records will be filtered and assignment logic defined for current rule entry will be applied. If criteria is not provided or is null, all records entering current rule entry will be assigned based on current rule entry's assignment logic.
          - `assign_to` (object `AssignToRequestObject`) **REQ** — This field defines the set of users to whom the records that enter the current rule entry must be assigned.  (Required)
          - `user_availability_based_on` (array of string) [maxItems=2, nullable] — Defines additional availability checks to be performed before choosing a user as owner. A user is assigned as owner only if it satisfies the mentioned availability conditions.
            items: [enum=['online_status', 'shift_timing']]
          - `followup_actions` (array of object `FollowupActionsRequestObject`) [minItems=1, maxItems=1, nullable] — Defines the list of different actions to be executed after owner assignment.
    - `default_assignee` (object `DefaultAssigneeRequestObject`) — Fallback assignee when no rule entry matches. Currently supports user type. Additional types (for example, queue) may be added in future versions.
      oneOf:
        - `UserTypeDefaultAssigneeRequestObject` — Configures a specific user or the currently logged-in user as the default assignee.
          - `type` (string) **REQ** [enum=['user']] — Default assignee type. Must be 'user'.
Possible values:
**user** - Represents user.
          - `resource` (object) **REQ** — Specify the resource for the Assignment Rule request.
            oneOf:
              - `UserResourceRequestObject` — Specific user to set as the default assignee
                - `api_name` (string) [enum=['${CURRENTUSER}']] — Set ${CURRENTUSER} to use the logged-in user as the default assignee.
Possible values:
**${CURRENTUSER}** - Represents ${currentuser}.

**Responses:**

- **200**: Returns the Assignment Rule response details for the completed operation. — Schema: `SuccessResponse` [application/json]
    > Successful API operation completed.
    schema: `SuccessResponse`
    - `assignment_rules` (array of object `SuccessObject`) [minItems=1, maxItems=1] — Represents the Assignment Rules returned for the Assignment Rule operation.
      schema: `SuccessObject`
      - `code` (string) [enum=['SUCCESS']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**SUCCESS** - Represents success.
      - `details` (object) — Represents additional details about the Assignment Rule operation result.
        - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — ID of the resource.
        - `rule_entries` (array of object) [minItems=1, maxItems=200] — Represents the rule entries returned for the Assignment Rule operation.
          - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — ID of the resource.
      - `message` (string) [maxLen=255] — Represents the message that describes the result of the Assignment Rule operation.
      - `status` (string) [enum=['success']] — Represents the status of the Assignment Rule operation.
Possible values:
**success** - Represents success.

- **400**: The request contains invalid, missing, or unsupported data.
**Resolution:** The request must include valid Assignment Rule data and valid parameter values for this operation. [application/json]
    > Error response for invalid data.
    oneOf:
      - `ErrorResponseRequiredParamMissing` — Required param missing.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**REQUIRED_PARAM_MISSING** - Represents required param missing.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          - `param_name` (string) [maxLen=255] — Represents the param name returned for the Assignment Rule operation.
        - `message` (string) **REQ** [enum=['One of the expected param is missing']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**One of the expected param is missing** - Represents one of the expected param is missing.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseInvalidModule` — Error response when module given is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**INVALID_MODULE** - Represents invalid module.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          - `param_name` (string) **REQ** [enum=['module']] — Represents the param name returned for the Assignment Rule operation.
Possible values:
**module** - Represents module. 
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**the module name given seems to be invalid** - Represents the module name given seems to be invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseFeatureNotSupported` — Feature not supported.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_SUPPORTED']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**FEATURE_NOT_SUPPORTED** - Represents feature not supported.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
        - `message` (string) **REQ** [enum=['Assignment rules not supported for current edition']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**Assignment rules not supported for current edition** - Represents Assignment Rules not supported for current edition.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseModuleNotSupported` — Error response for a module that is valid but unsupported in Assignment Rule processes.
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**NOT_SUPPORTED** - Represents not supported.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          - `param_name` (string) **REQ** [enum=['module']] — Represents the param name returned for the Assignment Rule operation.
Possible values:
**module** - Represents module. 
        - `message` (string) **REQ** [enum=['Module not supported in assignment rules']] — Represents the error message returned when the specified module does not support Assignment Rules.
Possible values:
**Module not supported in assignment rules** - Indicates that Assignment Rules are not supported for the specified module.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseInvalidData` — Invalid data.
        - `assignment_rules` (array of object) [maxItems=25] **REQ** — Array of error objects. 
          oneOf:
            - `ErrorResponseCannotRemove` — Assignment rule must contain atleast one rule entry.
              - `code` (string) **REQ** [enum=['CANNOT_REMOVE']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**CANNOT_REMOVE** - Represents cannot remove.
              - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
                - `api_name` (string) [enum=['rule_entries']] — Represents the API name returned for the Assignment Rule operation. Possible values: **rule_entries** - Represents rule entries.
                - `json_path` (string) [enum=['$.assignment_rules[0].rule_entries']] — Represents the JSON path returned for the Assignment Rule operation. Possible values: **$.assignment_rules[0].rule_entries** - Represents $.Assignment Rules[0].rule entries.
              - `message` (string) **REQ** [maxLen=100] — Represents the message that describes the result of the Assignment Rule operation.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
            - `ErrorResponseLimitExceeded` — Limit exceeded.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**LIMIT_EXCEEDED** - Represents limit exceeded.
              - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
                - `limit` (integer/int32) **REQ** — Represents the limit returned for the Assignment Rule operation. 
                - `api_name` (string) [maxLen=255] — Represents the API name returned for the Assignment Rule operation.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation.
              - `message` (string) **REQ** [enum=['limit exceeded']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**limit exceeded** - Represents limit exceeded.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
            - `ErrorResponseDuplicateData` — Duplicate data.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**DUPLICATE_DATA** - Represents duplicate data.
              - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
                - `api_name` (string) [enum=['api_name', 'name']] — Represents the API name returned for the Assignment Rule operation. Possible values: **api_name** - Represents API name. **name** - Represents name.
                - `json_path` (string) [enum=['$.assignment_rules[0].api_name', '$.assignment_rules[0].name']] — Represents the JSON path returned for the Assignment Rule operation. Possible values: **$.assignment_rules[0].api_name** - Represents $.Assignment Rules[0].API name. **$.assignment_rules[0].name** - Represents $.Assignment Rules[0].name.
              - `message` (string) **REQ** [maxLen=255] — Represents the message that describes the result of the Assignment Rule operation.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
            - `ErrorResponseInvalidData` — Invalid data.
            - `ErrorResponseDependentMismatch` — Dependent mimatch.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**DEPENDENT_MISMATCH** - Represents dependent mismatch.
              - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
                - `dependee` (object) — Represents the dependee returned for the Assignment Rule operation.
                  - `param_name` (string) [enum=['module']] — Nested detail field: param_name.
Possible values:
**module** - Represents module.
                - `api_name` (string) [maxLen=255] — Represents the API name returned for the Assignment Rule operation.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation.
              - `message` (string) **REQ** [enum=['dependent mismatch']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**dependent mismatch** - Represents dependent mismatch.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
            - `ErrorResponseMandatoryNotFound` — Mandatory not found.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**MANDATORY_NOT_FOUND** - Represents mandatory not found.
              - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
                - `api_name` (string) [maxLen=255] — Represents the API name returned for the Assignment Rule operation.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation.
              - `message` (string) **REQ** [maxLen=255] — Represents the message that describes the result of the Assignment Rule operation.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
            - `ErrorResponseExpectedFieldsMissing` — Expected fields missing.
              - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**EXPECTED_FIELD_MISSING** - Represents expected field missing.
              - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
                - `expected_fields` (array of object) [maxItems=25] — Represents the expected fields returned for the Assignment Rule operation.
                  - `api_name` (string) [maxLen=255] — Nested detail field: API_name.
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path.
              - `message` (string) **REQ** [maxLen=255] — Represents the message that describes the result of the Assignment Rule operation.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
            - `ErrorResponseDependentFieldMissing` — Dependent field missing.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**DEPENDENT_FIELD_MISSING** - Represents dependent field missing.
              - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
                - `dependee` (object) — Represents the dependee returned for the Assignment Rule operation.
                  - `api_name` (string) [maxLen=255] — Nested detail field: API_name.
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path.
                - `api_name` (string) [maxLen=255] — Represents the API name returned for the Assignment Rule operation.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation.
              - `message` (string) **REQ** [maxLen=255] — Represents the message that describes the result of the Assignment Rule operation.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.

- **403**: Permission denied for the Assignment Rule operation.
**Resolution:** The CRM administrator must grant the required Assignment Rule permission for the specified module, and the OAuth token must include the required scope. — Schema: `Possible403ErrorResponsesInManagingAR` [application/json]
    > Error response for forbidden access.
    oneOf:
      - `ErrorResponseNoPermissionToAccessAPI` — If current user does not have permission to access API.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**NO_PERMISSION** - Represents no permission.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          - `permissions` (array of string) [minItems=1, maxItems=1] **REQ** — Represents the list of required permissions. 
            items: [enum=['Crm_Implied_Api_Access']]
        - `message` (string) **REQ** [enum=['permission denied']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**permission denied** - Represents permission denied.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseNoPermissionToManageAR` — If current user does not have permission to manage Assignment Rules of given module.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**NO_PERMISSION** - Represents no permission.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          - `permissions` (array of string) [minItems=1, maxItems=1] **REQ** — Represents the list of required permissions. 
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=[1 values]] — Represents the error message for insufficient permission to manage Assignment Rules for the specified module.
Possible values:
**User does not have sufficient permission to manage assignment rules of given module** - Indicates that the user lacks the required Assignment Rule management permission for the module.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseNoPermissionToManageAROfPrivateModule` — If current user is neither the org admin nor the admin of the given private module.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**NO_PERMISSION** - Represents no permission.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
        - `message` (string) **REQ** [enum=['User is neither the org admin nor the admin of the given private module']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**User is neither the org admin nor the admin of the given private module** - Represents user is neither the org admin nor the admin of the given private module.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.

**Scopes:** ZohoCRM.settings.assignment_rules.UPDATE

# GET /settings/custom_views/{id}
**Operation:** `getCustomViewById` — Get Custom View By Id
> To retrieve the details of a specific Custom View for a module in your Zoho CRM organization, using the Custom View ID.

**Tags:** Custom Views

**Parameters:**
- `id` (path, string/int64, required) [maxLen=25]: Specify the unique ID of the Custom View. Use the [Get Custom View API](custom_views.yaml#$.paths./settings/custom_views.get) to retrieve the custom view IDs.
- `module` (query, string, required) [maxLen=25]: Specify the API name of the module for which to manage Custom Views. Refer to the Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module IDs.resource for valid values.
- `include_inner_details` (query, string, optional) [maxLen=50]: Specify whether to include the inner details of criteria and cross filters in the response.
Possible values:
**inner_details** - Includes the full criteria and cross filter details in the response.

**Schemas:**
`BetweenFilterCriterionResponse`:
  > Represents the response for a filter criterion using the between and not_between comparators. The value is an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the range filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['between', 'not_between']] — Represents the range comparison operator returned for the criterion, indicating whether the field value falls within or outside the specified bounds.
Possible values:
between - Matches records where the field value falls within the specified range.
not_between - Matches records where the field value falls outside the specified range.
  - `value` (array of object) [minItems=2, maxItems=2] **REQ** — Contains the two boundary values — [lower_bound, upper_bound] — against which the field was evaluated for the between or not_between comparator.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the between filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`EqualFilterCriterionResponse`:
  > Represents the response for a filter criterion using the equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime; SimpleFilterCriterionValueNumber for integer, currency, or double; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup, ownerlookup, or userlookup; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the equal filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['equal']] — Represents the equal comparison operator returned for the criterion.
Possible values:
equal - Matches records where the field value equals the specified filter value.
  - `value` (object) **REQ** — Represents the filter value returned for the equal comparator. Contains a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueGeneralPredefined` (string) [enum=['${EMPTY}', '${NOTEMPTY}']] — Represents a predefined placeholder value applicable to any field data_type with the equal comparator.
Possible values:
${EMPTY} - Matches records where the field has no value.
${NOTEMPTY} - Matches records where the field has any non-empty value.
      - `SimpleFilterCriterionValueDateTimePredefined` (string) [enum=[22 values]] — Represents a predefined placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator.
      - `SimpleFilterCriterionValueNDaysPredefined` (string) [maxLen=255, pattern=^\$\{(LAST_N_|NEXT_N_)(DAYS|WEEKS|MONTHS|YEARS):([0-9]+)\}$] — Represents a predefined N-period range placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator. Follows the pattern ${NEXT_N_<PERIOD>:<n>} or ${LAST_N_<PERIOD>:<n>}, where PERIOD is DAYS, WEEKS, MONTHS, or YEARS and n is a positive integer. The current period is always excluded from the range.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'value', 'pre_defined', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the equal filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`EqualityFilterCriterionResponse`:
  oneOf:
    - `EqualFilterCriterionResponse` — Represents the response for a filter criterion using the equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime; SimpleFilterCriterionValueNumber for integer, currency, or double; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup, ownerlookup, or userlookup; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
    - `NotEqualFilterCriterionResponse` — Represents the response for a filter criterion using the not_equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text-based types; SimpleFilterCriterionValueNumber for numeric types; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup types; and SimpleFilterCriterionValueObjectPredefined for predefined user or role placeholders.
`FilterCriterionResponse`:
  oneOf:
    - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
    - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
`FilterFieldBase`:
  > Represents the base field reference used in filter operations, containing minimal required properties. The field's data_type is not part of this object; resolve it from the corresponding FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `id` (string/int64) — Represents the unique ID of the field used for filter operations.
  - `api_name` (string) **REQ** — Represents the API name of the field used for filter application. Supports relationship notation, for example, Deals__r.Stage.
  additionalProperties: any
`GroupedFilterCriterionResponse`:
  > Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group` (array of object) [minItems=2, maxItems=25] **REQ** — Contains an array of filter conditions grouped together and evaluated with the specified logical operator.
    oneOf:
      - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
      - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group_operator` (string) **REQ** [enum=['AND', 'OR', 'and', 'or']] — Represents the logical operator applied between the filter conditions in the group.
Possible values:
AND - All conditions in the group must be satisfied.
OR - At least one condition in the group must be satisfied.
and - Equivalent to AND; all conditions in the group must be satisfied.
or - Equivalent to OR; at least one condition in the group must be satisfied.
  - `$disrupted` (boolean) — Indicates whether the grouped filter criterion is in a disrupted state, typically due to an invalid or unresolvable condition within the group.
`MultiSelectLookupFilterCriterionResponse`:
  > Represents the response for a filter criterion using the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
  - `field` (object) **REQ** — Represents the target field definition to which the multi-select lookup filter criterion was applied. The field has a data_type of multiuserlookup or multiselectlookup.
  - `comparator` (string) **REQ** [enum=['include_all', 'include_any', 'exclude_all', 'exclude_any']] — Represents the multi-select lookup comparison operator returned for the criterion. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
Possible values:
include_all - Matches records that include all specified lookup values.
include_any - Matches records that include at least one of the specified lookup values.
exclude_all - Matches records that exclude all specified lookup values.
exclude_any - Matches records that exclude at least one of the specified lookup values.
  - `value` (array of object `SimpleFilterCriterionValueObjectResponse`) [minItems=1, maxItems=500] **REQ** — Contains an array of lookup object references returned for the multi-select comparison.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the multi-select lookup filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`NotEqualFilterCriterionResponse`:
  > Represents the response for a filter criterion using the not_equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text-based types; SimpleFilterCriterionValueNumber for numeric types; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup types; and SimpleFilterCriterionValueObjectPredefined for predefined user or role placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the not-equal filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['not_equal']] — Represents the not-equal comparison operator returned for the criterion.
Possible values:
not_equal - Matches records where the field value does not equal the specified filter value.
  - `value` (object) **REQ** — Represents the filter value returned for the not_equal comparator. Contains a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'value', 'pre_defined', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the not-equal filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`OrderingFilterCriterionResponse`:
  > Represents the response for a filter criterion using the less_than, less_equal, greater_than, and greater_equal comparators. The value is a scalar; arrays and objects are not valid.
  - `field` (object) **REQ** — Represents the target field definition to which the ordering filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['less_than', 'less_equal', 'greater_than', 'greater_equal']] — Represents the ordering comparison operator returned for the criterion.
Possible values:
less_than - Matches records where the field value is less than the specified filter value.
less_equal - Matches records where the field value is less than or equal to the specified filter value.
greater_than - Matches records where the field value is greater than the specified filter value.
greater_equal - Matches records where the field value is greater than or equal to the specified filter value.
  - `value` (object) **REQ** — Represents the scalar filter value returned for the ordering comparator.
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
  - `$disrupted` (boolean) — Indicates whether the ordering filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`SetFilterCriterionResponse`:
  > Represents the response for a filter criterion using the in and not_in comparators. The value is an array of primitive values.
  - `field` (object) **REQ** — Represents the target field definition to which the set filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['in', 'not_in']] — Represents the set membership comparison operator returned for the criterion.
Possible values:
in - Matches records where the field value is in the specified set of values.
not_in - Matches records where the field value is not in the specified set of values.
  - `value` (array of object) [minItems=1, maxItems=500] **REQ** — Contains an array of primitive filter values returned for the set comparison.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the set filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`SimpleFilterCriterionResponse`:
  oneOf:
    - `EqualityFilterCriterionResponse` — Represents the response for an equality filter criterion that dispatches to either the EqualFilterCriterionResponse or NotEqualFilterCriterionResponse schema based on the comparator value.
    - `TextFilterCriterionResponse` — Represents the response for a filter criterion using the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value is a string scalar or array; SimpleFilterCriterionValueString applies to text-based field types.
    - `OrderingFilterCriterionResponse` — Represents the response for a filter criterion using the less_than, less_equal, greater_than, and greater_equal comparators. The value is a scalar; arrays and objects are not valid.
    - `BetweenFilterCriterionResponse` — Represents the response for a filter criterion using the between and not_between comparators. The value is an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `SetFilterCriterionResponse` — Represents the response for a filter criterion using the in and not_in comparators. The value is an array of primitive values.
    - `MultiSelectLookupFilterCriterionResponse` — Represents the response for a filter criterion using the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
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
`SimpleFilterCriterionValueObjectResponse`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (object) **REQ**
  - `name` (object) **REQ**
  additionalProperties: any
`TextFilterCriterionResponse`:
  > Represents the response for a filter criterion using the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value is a string scalar or array; SimpleFilterCriterionValueString applies to text-based field types.
  - `field` (object) **REQ** — Represents the target field definition to which the text filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['like', 'not_like', 'starts_with', 'ends_with', 'contains', 'not_contains']] — Represents the text comparison operator returned for the criterion.
Possible values:
like - Matches records where the field value contains the specified pattern.
not_like - Matches records where the field value does not contain the specified pattern.
starts_with - Matches records where the field value begins with the specified string.
ends_with - Matches records where the field value ends with the specified string.
contains - Matches records where the field value contains the specified string.
not_contains - Matches records where the field value does not contain the specified string.
  - `value` (object) **REQ** — Represents the string filter value returned for the text comparator. Contains a scalar string or an array of string values.
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
  - `$disrupted` (boolean) — Indicates whether the text filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`UserReference`:
  > Represents a user reference containing the user ID and display name.
  - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique ID of the user.
  - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user.

**Responses:**

- **200**: Returns the details of the specified Custom View, including its filter criteria, sort configuration, field list, and access control settings. — Schema: `GetCustomViewByIdResponse` [application/json]
    > Get a specific custom view of a module using custom view ID
    schema: `GetCustomViewByIdResponse`
    - `custom_views` (array of object) [maxItems=1] **REQ** — List of custom views
      schema: `CustomViewGetItem`
      - `name` (string) **REQ** [maxLen=50] — Represents the name of the Custom View.
      - `display_value` (string) **REQ** [maxLen=50] — Represents the display label of the Custom View as shown to users.
      - `$modified_criteria` (boolean) — Indicates whether the filter criteria of the Custom View has been modified since it was originally created.
Possible values:
**true** - The criteria has been modified.
**false** - The criteria has not been modified.
      - `access_type` (string) **REQ** [enum=['shared', 'public', 'only_to_me']] — Represents the access type of the Custom View.
Possible values:
**shared** - The view is shared with selected users, roles, groups, or territories.
**public** - The view is accessible to all users in the organization.
**only_to_me** - The view is private and accessible only to the creator.
      - `created_time` (string/date-time) **REQ** [nullable] — Represents the date and time when the Custom View creation occurred.
      - `modified_time` (string/date-time) **REQ** [nullable] — Modification Time of the Custom View
      - `last_accessed_time` (string/date-time) **REQ** [nullable] — Represents the date and time when the Custom View was last accessed. A null value indicates the view has not been accessed.
      - `system_name` (string) **REQ** [maxLen=50, nullable] — Represents the system-defined name of the Custom View. A null value indicates the view does not have a system name.
      - `category` (string) **REQ** [enum=['public_views', 'other_users_views', 'shared_with_me', 'created_by_me']] — Represents the category of the Custom View.
Possible values:
**public_views** - Views accessible to all users in the organization.
**other_users_views** - Views created by other users in the organization.
**shared_with_me** - Views shared with the current user.
**created_by_me** - Views created by the current user.
      - `default` (boolean) **REQ** — Indicates whether the Custom View is set as the default view for the module.
Possible values:
**true** - This is the default view.
**false** - This is not the default view.
      - `system_defined` (boolean) **REQ** — Indicates whether the Custom View is a system-defined view created by Zoho CRM.
Possible values:
**true** - The view is system-defined.
**false** - The view is user-defined.
      - `locked` (boolean) **REQ** — Indicates whether the Custom View is locked and cannot be modified by users.
Possible values:
**true** - The view is locked.
**false** - The view is not locked.
      - `favorite` (integer/int32) **REQ** [nullable] — Represents the favorite order of the Custom View. A null value indicates the view is not marked as a favorite.
      - `offline` (boolean) — Indicates whether the Custom View is available in offline mode.
Possible values:
**true** - The view is available offline.
**false** - The view is not available offline.
      - `criteria` (object `CustomViewCriterionResponse`) **REQ** — Represents the filter criteria of the Custom View
        oneOf:
          - `FilterCriterionResponse` — Represents the top-level filter criterion returned in the response, supporting both simple field-based filters and complex grouped filters with logical operators.
            type: null — No criteria is applied. The custom view returns all records.
      - `cross_filters` (object `CustomViewCrossFilterCriterionResponse`) — Cross-filter criteria of the Custom View
        oneOf:
          - `CrossFiltersResponse` — Represents the list of cross-filter objects returned in the response, applied to the Custom View.
            type: array of object [minItems=0, maxItems=3]
              - `include_objects` (boolean) **REQ** — Indicates whether records with matching related records were included in the filtered results.
              - `relation` (object) **REQ**
                schema: `ChildRelationshipReference`
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the child relationship module used to identify the relationship.
                - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique ID of the child relationship module record.
                - `$disrupted` (boolean) **REQ** — Indicates whether the related module relationship referenced by this criterion is in a disrupted state, typically due to an unresolvable or deleted relationship definition.
              - `criteria` (object `FilterCriterionResponse`) **REQ** — Represents the top-level filter criterion returned in the response, supporting both simple field-based filters and complex grouped filters with logical operators.
            type: null — No cross-filter criteria is applied.
      - `shared_to` (array of object) [maxItems=250, nullable] **REQ** — Represents the list of users, roles, groups, or territories the Custom View is shared with.
        - `name` (string) [maxLen=255] — Name of the user/group
        - `id` (string/int64) **REQ** [maxLen=25] — ID of the user/group
        - `type` (string) **REQ** [enum=['territories', 'roles', 'groups', 'users']] — Represents the type of the shared-to entity.
Possible values:
**territories** - The view is shared with a territory.
**roles** - The view is shared with a role.
**groups** - The view is shared with a group.
**users** - The view is shared with a specific user.
        - `subordinates` (boolean) [nullable] — Specify true if subordinates are included, false otherwise
      - `modified_by` (object) **REQ**
        oneOf:
          - `UserReference` — Represents a user reference containing the user ID and display name.
            type: null — No user associated
      - `created_by` (object) **REQ**
        oneOf:
          - `UserReference` — Represents a user reference containing the user ID and display name.
            type: null — No user associated
      - `fields` (array of object) [maxItems=250] **REQ** — Represents the list of fields included in the Custom View, each with display and pin configuration details.
        - `api_name` (string) [maxLen=255, nullable] — Represents the API name of the field included in the Custom View.
        - `id` (string/int64) [maxLen=25, nullable] — Represents the unique ID of the field included in the Custom View.
        - `_pin` (boolean) — Indicates whether the field is pinned in the Custom View.
Possible values:
**true** - The field is pinned.
**false** - The field is not pinned.
        - `_width` (integer/int32) — Represents the display width of the field in pixels.
        - `_pin_order` (integer/int32) — Represents the order of the pinned field within the Custom View.
      - `sort_by` (object) **REQ** — Represents the field used to sort the records in the Custom View.
        oneOf:
          - `FieldReference` — Represents a reference to a field in the Custom View, identified by its API name and unique ID.
            - `api_name` (string) [maxLen=255, nullable] — Represents the API name of the field. A null value indicates no field is selected.
            - `id` (string/int64) [maxLen=25, nullable] — Represents the unique ID of the field. A null value indicates no field is selected.
            type: null — No sort is applied
      - `sort_order` (object) **REQ** — Represents the sort order applied to the records in the Custom View.
        oneOf:
            type: string [enum=['asc', 'desc']] — Represents the sort order applied to the Custom View.
Possible values:
**asc** - Ascending order.
**desc** - Descending order.
            type: null — Represents no sort order applied to the Custom View.
      - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique ID of the Custom View.
    - `info` (object) **REQ** — Additional information about the response
      schema: `CustomViewInfo`
      - `per_page` (integer/int32) — Represents the number of Custom Views returned per page.
      - `count` (integer/int32) — Represents the total number of Custom Views available for the specified module.
      - `page` (integer/int32) — Represents the current page number of the paginated response.
      - `more_records` (boolean) — Indicates whether more records are available beyond the current page.
Possible values:
**true** - More records are available.
**false** - No more records are available.
      - `default` (string/int64) [maxLen=255] — Represents the ID of the default Custom View for the module.
      - `translation` (object) **REQ** — Represents the localized display labels for the Custom View category names.
        - `public_views` (string) **REQ** [maxLen=255] — Represents the display label for the public views category of Custom Views.
        - `other_users_views` (string) **REQ** [maxLen=255] — Represents the display label for the other users' views category of Custom Views.
        - `shared_with_me` (string) **REQ** [maxLen=255] — Represents the display label for the shared with me category of Custom Views.
        - `created_by_me` (string) **REQ** [maxLen=255] — Represents the display label for the created by me category of Custom Views.

- **204**: No content - the given Custom View ID does not match any existing Custom View in the specified module.

- **400**: The request URL or module is invalid. Resolution: A valid module API name and Custom View ID must be provided in the request. [application/json]
    > Represents the error response for an invalid get Custom View by ID request.
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
      - `ResourcePathIndexErrorResponse` — Flat error: invalid resource path segment
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the invalid resource path.
Possible values:
**INVALID_DATA** - A segment in the resource path is invalid.
        - `details` (object `ResourcePathIndexError`) **REQ** — Represents the error details indicating which segment of the resource path or URL is invalid.
          schema: `ResourcePathIndexError`
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the invalid segment in the resource path.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid resource path segment.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.

- **401**: Authentication failed or the OAuth access token does not include the required scope. Resolution: A new access token must be generated with the ZohoCRM.settings.custom_views.READ scope. [application/json]
    > Represents the error response for an unauthorized get Custom View by ID request.
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

- **403**: Permission denied to retrieve the specified Custom View. Resolution: The CRM administrator must grant the required permission to the user's profile. — Schema: `ModuleForbiddenErrorResponse` [application/json]
    > Represents the error response returned when the user does not have the required permissions for the specified module.
    schema: `ModuleForbiddenErrorResponse`
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

**Scopes:** ZohoCRM.settings.custom_views.READ

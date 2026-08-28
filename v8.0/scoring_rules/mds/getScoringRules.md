# GET /settings/automation/scoring_rules
**Operation:** `getScoringRules` — Scoring Rules
> To retrieve a list of Scoring Rules configured in your Zoho CRM organization.

**Parameters:**
- `module` (query, string, optional) [maxLen=100]: Specifies the API name of the module to filter Scoring Rules by.
- `layout_id` (query, number, optional): Specifies the unique ID of the layout to filter Scoring Rules by.
- `page` (query, integer/int32, optional): Specifies the page number for paginated results.
- `per_page` (query, integer/int32, optional): Specifies the number of Scoring Rules to return per page.
- `name` (query, string, optional) [maxLen=25]: Specifies the name of the Scoring Rule to filter by.
- `fields` (query, string, optional) [maxLen=255]: Comma-separated list of fields to include in the response. If this param is passed, except the mentioned fields, value of other fields will be null. Supported values: field_rules, signal_rules, name, description, active.
- `active` (query, boolean, optional): Filter rules by their active/inactive status. Pass 'true' to retrieve only active rules, 'false' for inactive rules. Omit to retrieve all rules regardless of status.

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

**Responses:**

- **200**: Returns a list of all Scoring Rules configured in the organization, filtered by the provided query parameters. — Schema: `GetScoringRulesListResponse` [application/json]
    > Represents the response body for the list Scoring Rules operation.
    schema: `GetScoringRulesListResponse`
    - `scoring_rules` (array of object `ScoringRuleGET`) [maxItems=300] — Represents an array of Scoring Rule summary objects returned in the list response.
      schema: `ScoringRuleGET`
      - `created_time` (string) [maxLen=255] — Scoring rule created time
      - `has_signal_rules` (boolean) — It defines whether the production scoring rule has any signal rules or not. Applicable only for Leads and Contacts modules rules in Sandbox environment.
      - `custom_fields` (array of object `CustomFieldConfiguration`) [maxItems=6, nullable] — Represents the custom fields configured for this Scoring Rule to hold referenced scores.
        schema: `CustomFieldConfiguration`
        - `id` (string) [maxLen=25] — Represents the unique ID of the custom field associated with the Scoring Rule.
        - `field_label` (string) [maxLen=100] — Represents the display name of the custom field. Required when creating a Scoring Rule.
        - `api_name` (string) [maxLen=100] — Represents the API name of the custom field associated with the Scoring Rule.
        - `reference_field` (object `ReferencedScoreField`) — It will hold the referenced score field info. (Required for POST)
          schema: `ReferencedScoreField`
          - `api_name` (string) [enum=[6 values]] — Specifies the API name of the referenced score field. Required when creating a Scoring Rule.
          - `id` (string) [maxLen=25] — Represents the unique ID of the referenced score field.
          additionalProperties: any
      - `module` (object `ModuleDetails`) **REQ** — module info (Required)
        schema: `ModuleDetails`
        - `api_name` (string) [maxLen=255] — Represents the API name of the module associated with the Scoring Rule.
        - `id` (string) [maxLen=25] — Represents the unique ID of the module associated with the Scoring Rule.
      - `description` (string) [maxLen=500, nullable] — Represents the optional description of the Scoring Rule. This field is nullable.
      - `active` (boolean) — Indicates whether the Scoring Rule is active (`true`) or inactive (`false`).
      - `created_by` (object `CreatedBySchema`) — Nested schema for created_by
        schema: `CreatedBySchema`
        - `name` (string) [maxLen=255] — Full name of the user who created the scoring rule.
        - `id` (string) [maxLen=25] — Unique numeric ID of the user who created the scoring rule.
        - `zuid` (string) [maxLen=255] — Zoho unique ID (ZUID) of the user who created the scoring rule.
      - `layout` (object `LayoutDetails`) — Layout info. If the rule should be created for all layouts, this field can be skipped or set value as null.
        schema: `LayoutDetails`
        - `display_label` (string) [maxLen=255] — Represents the display label of the layout associated with the Scoring Rule.
        - `api_name` (string) [maxLen=255] — Represents the API name of the layout associated with the Scoring Rule.
        - `id` (string) [maxLen=25] — Represents the unique ID of the layout associated with the Scoring Rule.
      - `modified_time` (string) [maxLen=255, nullable] — Represents the date and time when the Scoring Rule was last modified, in ISO 8601 format. This field is nullable.
      - `field_rules` (array of object `FieldScoreConfigurationResponse`) [maxItems=50] — Module field based score configuration can be added here
        schema: `FieldScoreConfigurationResponse`
        - `score` (integer/int32) — Represents the points that should be added for the criteria and this is mandatory
        - `id` (string) [maxLen=255] — Represents the primary key of the field rule (Required in UPDATE).
        - `criteria` (object `FilterCriterionResponse`) — Represents the top-level filter criterion returned in the response, supporting both simple field-based filters and complex grouped filters with logical operators.
          oneOf:
            - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
            - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
      - `name` (string) **REQ** [maxLen=25] — Represents the unique name of the Scoring Rule.
      - `modified_by` (object `ModifiedBySchema`) — Scoring rule modified by
        schema: `ModifiedBySchema`
        - `name` (string) [maxLen=255] — Full name of the user who last modified the scoring rule.
        - `id` (string) [maxLen=25] — Unique numeric ID of the user who last modified the scoring rule.
        - `zuid` (string) [maxLen=255] — Zoho unique ID (ZUID) of the user who last modified the scoring rule.
      - `signal_rules` (array of object `TouchPointScoreConfiguration`) [maxItems=250, nullable] — Touch points based score configurations; applicable only for Leads and Contacts modules
        schema: `TouchPointScoreConfiguration`
        - `score` (integer/int32) — Points that should be added for the signal (Required for CREATE)
        - `id` (string) [maxLen=25] — Signal rule primary key
        - `_delete` (null) — used to delete the signal rule
        - `signal` (object `SignalInformation`) — Touch point signal info (Required for CREATE)
          schema: `SignalInformation`
          - `namespace` (string) [maxLen=255] — Signal namespace
          - `id` (string) [maxLen=25] — Signal id
      - `id` (string) [maxLen=255] — Represents the unique ID of the Scoring Rule.
    - `info` (object `ScoringRulePaginationInfo`) — Nested schema for info
      schema: `ScoringRulePaginationInfo`
      - `per_page` (integer/int32) — no of rules need to be fetched per_page
      - `count` (integer/int32) — Total number of scoring rules returned in the current response page.
      - `page` (integer/int32) — Current page number in the paginated response.
      - `more_records` (boolean) — Indicates whether additional scoring rules are available beyond the current page.

- **204**: No scoring rules are configured

- **400**: Invalid module api_name is passed in module param value — Schema: `InvalidModuleParamErrorResponse` [application/json]
    > Represents an error response returned when an invalid module API name is provided in a query parameter.
    schema: `InvalidModuleParamErrorResponse`
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this error response.
    - `details` (object) **REQ** — Represents additional details about the validation error.
      - `param_name` (string) [maxLen=255] — Represents the name of the query parameter that contains the invalid value.
    - `message` (string) **REQ** [enum=['Please check whether the input values are correct']] — Represents the error message describing the validation issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

**Scopes:** ZohoCRM.settings.scoring_rules.READ

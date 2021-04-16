"""Experimenting with Parsing and editing SQL Files"""
import sys

import sqlparse
import sqlparse.tokens as ttypes
import sqlparse.sql as sql


def file_output(file_name):
    with open(file_name) as file:
        sql_text = file.read()

    return sql_text


def parse_out_editable_pieces(file_name):
    sql_txt = file_output(file_name)
    view_create_commands = [cv for cv in sqlparse.split(sql_txt)
                            if sqlparse.parse(cv)[0].token_first(skip_ws=True, skip_cm=True)
                            .match(ttypes.Keyword.DDL, 'CREATE OR REPLACE')]

    for create in view_create_commands:
        parsed_create = sqlparse.parse(create)[0]
        create_tokens = [t for t in sql.TokenList(parsed_create.tokens)
                  if t.ttype not in (ttypes.Whitespace, ttypes.Whitespace.Newline)]
        create_token_list = sql.TokenList(create_tokens)
        create_union_indexes = []

        # TODO: Find start of Unions
        for index, token in enumerate(create_token_list):
            # Only find SELECT first then UNION ALL
            match_text = 'SELECT' if len(create_union_indexes) == 0 else 'UNION ALL'
            target_type = ttypes.Keyword.DML if len(create_union_indexes) == 0 else ttypes.Keyword

            if token.match(target_type, match_text):
                create_union_indexes.append(index)

        print(create_union_indexes)

        # TODO: group unions into statements
        first_union = create_union_indexes[0]
        union_count = len(create_union_indexes)
        create_union_indexes.reverse()

        for index, union_index in enumerate(create_union_indexes):
            # Find the column declarations
            end = len(create_token_list.tokens)-1 if index == 0 else create_union_indexes[index-1]
            create_token_list.group_tokens(sql.Statement, start=union_index, end=end, include_end=False)
            # token_list.token_next_by(idx=union_location, t=[[sql.IdentifierList]], end=select_locations[(index + 1)])

        # TODO: Iterate through created union statements to find each key
        for tk_index in range(first_union, (first_union+union_count)-1):
            # TODO: grab table name for mapping to update string
            union = create_token_list[tk_index]
            found_key = False
            for line in union:
                # TODO: Identify the list of column names
                if isinstance(line, sql.IdentifierList):
                    # column_list = [t for t in sql.TokenList(token)
                    #                if t.ttype not in (ttypes.Whitespace, ttypes.Whitespace.Newline)]
                    for identifier in line:
                        # TODO: filter down to key
                        if hasattr(identifier, 'tokens'):
                            # Remove comments because the lump into the end of an identifier when split
                            _stripped_values = [t.value for t in identifier.tokens if not isinstance(t, sql.Comment)]
                            if isinstance(identifier, sql.Identifier) and 'channelmix_key' in _stripped_values:
                                found_key = True
                                print(f"Union {tk_index} channelmix key in identifier: {identifier}")
            if not found_key:
                print(f'Key not found for {line}')


#    TODO: How do I update the whole file and rewrite it gracefully?


if __name__ == '__main__':
    parse_out_editable_pieces(sys.argv[1])

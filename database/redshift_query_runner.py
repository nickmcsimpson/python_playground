import sys
from functools import wraps
from pprint import pprint

import psycopg2.extras

from database.function_timer import time_sequence


def query_wrapper(function):
    @wraps(function)
    def connection(*args, **kwargs):
        conn = psycopg2.connect(dbname='dev',
                                host=f"{kwargs.get('domain')}.redshift.amazonaws.com",
                                port=5439,
                                user=kwargs.get('username'),
                                password=kwargs.get('password')
                                )
        # Open a cursor to perform database operations
        """When a connection exits the with block, if no exception has been raised by the block, 
        the transaction is committed. In case of exception the transaction is rolled back.

        When a cursor exits the with block it is closed, releasing any resource eventually associated with it. 
        The state of the transaction is not affected.
        """
        with conn:
            with conn.cursor() as curs:
                function(*args, **kwargs, cursor=curs)
        conn.close()

    return connection


@query_wrapper
@time_sequence
def run_script_with_file_context_manager(file_name, cursor=None, schema='', **kwargs):
    """Open file as context manager and execute as script"""
    with open(file_name) as file:
        try:
            sql_script = file.read().replace('<schema>', schema)
            cursor.executemany(sql_script, {})
            """This likes to fail with no information as to why. Likely because of excess whitespace.
                
                "The current implementation of executemany() is (using an extremely charitable understatement) not 
                particularly performing. These functions can be used to speed up the repeated execution of a statement 
                against a set of parameters. By reducing the number of server roundtrips the performance can be orders 
                of magnitude better than using executemany()."
                
                The primary benefit seems to come for prepared statements and inserts that can be reduced. Our use case,
                may not benefit, and the granularity of adding to the psycopg2 'commit' batch is more beneficial than 
                attampting to execute a full script with no insight into where something fails.
                
                execute_batch is semantically similar:
                "but has a different implementation: Psycopg will join the statements into fewer multi-statement 
                commands, each one containing at most page_size statements, 
                resulting in a reduced number of server roundtrips."
            """

            # psycopg2.extras.execute_batch(sql_script)
        except Exception as e:
            print(e)


@query_wrapper
@time_sequence
def run_queries_with_file_context_manager(file_name, cursor=None,
                                          **kwargs):  # Per docs this is no different than execute many
    """Open file as context manager and execute individually"""
    with open(file_name) as file:
        sql_script = file.read()
        for command in sql_script.split(';'):
            cursor.execute(command)


@query_wrapper
@time_sequence
def run_individual_queries_in_separate_function(file_name, cursor=None, schema='', **kwargs):
    """Open file as context manager and execute individually via function call"""
    with open(file_name) as file:
        sql_script = file.read()
        for command in sql_script.split(';'):
            if command.isspace() or command == '':
                continue
            try:
                run_singular_query(command.replace('<schema>', schema), cursor)
            except ValueError:
                print(f"Can't Format query:\n{command}")

@time_sequence
def run_singular_query(command, cursor=None):
    try:
        cursor.execute(command)
    except Exception as exception:
        print(exception)
        pprint(f"{command}")


@time_sequence
def run_individual_queries_in_separate_transactions(file_name, schema='', **kwargs):
    """Open file as context manager and execute individually via function call unique transactions"""
    with open(file_name) as file:
        sql_script = file.read()
        for command in sql_script.split(';'):
            if command.isspace() or command == '':
                continue
            try:
                run_singular_query_as_transaction(command.replace('<schema>', schema), **kwargs)
            except ValueError:
                print(f"Can't Format query:\n{command}")


@query_wrapper
@time_sequence
def run_singular_query_as_transaction(command, cursor=None, **kwargs):
    try:
        cursor.execute(command)
    except Exception as exception:
        print(exception)
        pprint(f"{command}")


if __name__ == '__main__':
    run_individual_queries_in_separate_transactions(sys.argv[1], schema=sys.argv[2], username=sys.argv[3],
                                         password=sys.argv[4], domain=sys.argv[5])

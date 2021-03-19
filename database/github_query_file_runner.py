import sys

import requests

from database.redshift_query_runner import run_individual_queries_in_separate_function

GITHUB_URL = 'https://api.github.com'

""" Sample Result:
[
    {
        "name": "abacosdw.sql",
        "path": "database/sql/abacosdw.sql",
        "sha": "59afe29932259ac690360afdb0eb7485cf7ada6b",
        "size": 8682,
        "url": "https://api.github.com/repos/nickmcsimpson/python_playground/contents/database/sql/abacosdw.sql?ref=main",
        "html_url": "https://github.com/nickmcsimpson/python_playground/blob/main/database/sql/abacosdw.sql",
        "git_url": "https://api.github.com/repos/nickmcsimpson/python_playground/git/blobs/59afe29932259ac690360afdb0eb7485cf7ada6b",
        "download_url": "https://raw.githubusercontent.com/nickmcsimpson/python_playground/main/database/sql/abacosdw.sql",
        "type": "file",
        "_links": {
            "self": "https://api.github.com/repos/nickmcsimpson/python_playground/contents/database/sql/abacosdw.sql?ref=main",
            "git": "https://api.github.com/repos/nickmcsimpson/python_playground/git/blobs/59afe29932259ac690360afdb0eb7485cf7ada6b",
            "html": "https://github.com/nickmcsimpson/python_playground/blob/main/database/sql/abacosdw.sql"
        }
    }
]
"""


def get_list_of_contents_from_github_folder(org, repo, path):
    r = requests.get(f"{GITHUB_URL}/repos/{org}/{repo}/contents/{path}")
    if r.status_code == 200:
        return r.json()
    else:
        print(r.status_code)

    # 302Found
    # 403ForbiddenResource
    # 404NotFound


def main(path, **kwargs):
    contents = get_list_of_contents_from_github_folder('nickmcsimpson', 'python_playground', path)

    for item in contents:
        print(item.get('name'))

    run_individual_queries_in_separate_function(contents[0].get('download_url'), get_file_from=url_open, **kwargs)


def url_open(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    main(sys.argv[1], schema=sys.argv[2], username=sys.argv[3],
         password=sys.argv[4], domain=sys.argv[5])

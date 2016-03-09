import json
import re
import urllib2


def main():
    read_lines()
    process_lines()


def read_lines():
    """Read each line of the OCR'd text file and append the line to a list."""
    with open("output990/0.txt", "r") as f:
        for line in f:
            lines.append(line.strip())


def process_lines():
    """
    Parse organization title and state abbreviation.

    If line contains a potential address, get name from line before and state
    from line after. Currently the method will only catch
    the organization title "AGA" and the state "MD" from 990 entry
    containing "AGA INSTITUTE" and "BETHESDA, MD".
    """
    for (idx, line) in enumerate(lines):
        if pattern.match(line) and len(lines[idx - 1]) > 0:
            title_line = lines[idx - 1]
            title = title_line.split(" ")[0]

            state_line = lines[idx + 1]
            for txt in state_line.split(" "):
                if len(txt) == 2:
                    state = txt
                    format_request(title, state)
                    # only try the first organization
                    break
            break


def format_request(title, state):
    """Create URL to request to ProPublica 990 explorer API."""
    request = ("https://projects.propublica.org/nonprofits/api/v1/"
               "search.json?q={title}&state%5Bid%5D={state}"
               "&output=flat").format(title=title, state=state)
    search_api(request)


def search_api(request):
    """Send request to ProPublica 990 explorer API."""
    response = urllib2.urlopen(request)
    test_response(response)


def test_response(response):
    """Print EIN values present in ProPublica 990 API response."""
    data = json.loads(response.read())

    for f in data["filings"]:
        print "EIN: {}".format(f["ein"])


if __name__ == "__main__":
    lines = []
    # potential address regex
    pattern = re.compile("\d+ [a-zA-z]+")
    main()

import json
import re
import urllib2


def main():
    read_lines()
    process_lines()


def read_lines():
    with open("output990/0.txt", "r") as f:
        for line in f:
            lines.append(line.strip())


def process_lines():
    # if find potential address line, get name from line before
    # and state from line after
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
    request = ("https://projects.propublica.org/nonprofits/api/v1/"
               "search.json?q={title}&state%5Bid%5D={state}"
               "&output=flat").format(title=title, state=state)
    search_api(request)


def search_api(request):
    response = urllib2.urlopen(request)
    test_response(response)


def test_response(response):
    data = json.loads(response.read())

    for f in data["filings"]:
        print "EIN: {}".format(f["ein"])


if __name__ == "__main__":
    lines = []
    pattern = re.compile("\d+ [a-zA-z]+")
    main()

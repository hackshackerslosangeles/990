#!/bin/bash
docker build -t hackhackerslosangeles/990 docker
docker run -ti -v $(pwd)/source:/bin990 -v $(pwd)/docs:/docs990 -v $(pwd)/output:/output990 hackhackerslosangeles/990 /bin/bash

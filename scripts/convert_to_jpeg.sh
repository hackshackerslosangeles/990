#!/bin/bash
convert -verbose -density 200 -trim $1 -quality 100 $2

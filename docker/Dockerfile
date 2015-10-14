FROM ubuntu:14.04

# SETUP
RUN \
    apt-get update && \
    apt-get -y install build-essential curl git libtool automake wget imagemagick libpng-dev libjpeg-dev libicu-dev libpango1.0-dev libcairo2-dev libtiff-dev && \
    apt-get clean

# MISC
RUN \
    mkdir src

# LEPTONICA
RUN \
    cd /src && \
    wget http://www.leptonica.com/source/leptonica-1.71.tar.gz && \
    tar xvzf leptonica-1.71.tar.gz && \
    cd leptonica-1.71 && \
    ./configure && \
    make && \
    make install

# TESSERACT
RUN \
    cd /src && \
    git clone https://github.com/tesseract-ocr/tesseract.git && \
    cd tesseract && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig

# LANGDATA
RUN \
    cd /src && \
    git clone https://github.com/tesseract-ocr/langdata.git

# TESSDATA
RUN \
    cd /src && \
    git clone https://github.com/tesseract-ocr/tessdata.git && \
    cd tessdata && \
    cp eng.* /usr/local/share/tessdata/

# TESSTRAINIG BUILD
RUN \
    cd /src/tesseract && \
    make training && \
    make training-install

ENV PATH $PATH:/bin990

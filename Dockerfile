# Ubuntu 16.04.6 LTS (Xenial Xerus)
FROM ubuntu:xenial-20200326

# アップデートと必要なパッケージのインストール
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    # aiohttpで必要
    build-essential \
    python3-dev \
    # Python関連
    python3 \
    python3-pip \
    python-dev \
    python-tk \
    pylint \
    pylint3 \
    flake8 \
    language-pack-ja \
    # aiohttp関連
    libffi-dev \
    libssl-dev \
    ca-certificates \
    less \
    vim \
    wget  \
    git \
    curl \
    unzip \
    pkg-config && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*


# 各種インストールの後にやる (aptするライブラリによりエラー表示されることがあるため)
RUN locale-gen ja_JP.UTF-8
ENV LANG=ja_JP.UTF-8 \
    LANGUAGE=ja

# WORKDIRは複数回実行してもOK
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

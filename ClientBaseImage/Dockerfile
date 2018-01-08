FROM bitcoindev

# Clone git repository
RUN git clone https://github.com/a18499/btcregretarget.git ~/bitcoin
WORKDIR /root/bitcoin

# Build bitcoin
RUN ./autogen.sh
RUN ./configure
RUN make -j 4
RUN make install
RUN mkdir number
#RUN echo "rpcuser=test\nrpcpassword=test\nrpcallowip=0.0.0.0/0\n" > src/bitcoin.conf
COPY ./docker-entrypoint.sh /
COPY ./client.py /
WORKDIR /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]



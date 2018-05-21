FROM bitcoindev

# Clone git repository
#RUN git clone https://github.com/a18499/btcregretarget.git ~/bitcoin
RUN git clone https://github.com/raysbuck/ourseed ~/ourseed
WORKDIR /root/ourseed

# Build bitcoin
#RUN ./autogen.sh
#RUN ./configure
#RUN make -j 4
#RUN make install
RUN make

COPY ./docker-entrypoint.sh /root/ourseed
RUN chmod +x /root/ourseed/docker-entrypoint.sh
ENTRYPOINT ["/root/ourseed/docker-entrypoint.sh"]

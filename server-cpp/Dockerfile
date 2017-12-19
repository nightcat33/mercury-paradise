FROM ubuntu:16.04

RUN apt-get update && apt-get install -y apt-utils openssh-server libssl-dev cmake gcc build-essential
RUN apt-get install vim python tcpdump telnet git -y
RUN apt-get install byacc flex -y
RUN apt-get install iproute2 gdbserver less bison valgrind -y

RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile


# poco library
WORKDIR /root
RUN git clone https://github.com/pocoproject/poco.git
WORKDIR /root/poco
RUN mkdir linux_build
WORKDIR /root/poco/linux_build
RUN cmake ..
RUN make
RUN make install




EXPOSE 22 9999 7777
CMD ["/usr/sbin/sshd", "-D"]


FROM alpine:3.15

ENV TIMEZONE=Asia/Shanghai
ENV MYSQL_ROOT_PASSWORD=root

RUN apk update && apk upgrade
RUN apk add --no-cache mariadb mariadb-client \
    apache2 \ 
    apache2-utils \
    curl wget \
    gcc musl-dev make \
    autoconf \
    tzdata \
    php7-apache2 \
    php7-cli \
    php7-pear \
    php7 \
    php7-dev \
    php7-phar \
    php7-zlib \
    php7-zip \
    php7-bz2 \
    php7-ctype \
    php7-curl \
    php7-pdo_mysql \
    php7-mysqli \
    php7-json \
    php7-mcrypt \
    php7-xml \
    php7-dom \
    php7-iconv \
    php7-xdebug \
    php7-session \
    php7-intl \
    php7-gd \
    php7-mbstring \
    php7-apcu \
    php7-opcache \
    php7-tokenizer \
    php7-simplexml \
    memcached

RUN curl -sS https://getcomposer.org/installer | \
    php -- --install-dir=/usr/bin --filename=composer
#
#    sed -i 's#AllowOverride none#AllowOverride All#' /etc/apache2/httpd.conf && \
#    sed -i 's#Require all denied#Require all granted#' /etc/apache2/httpd.conf && \
#    sed -i 's#^DocumentRoot ".*#DocumentRoot "/var/www/localhost/htdocs"#g' /etc/apache2/httpd.conf && \

RUN pecl install memcache-4.0.5.2 && \
    echo "extension=memcache.so" > /etc/php7/conf.d/00_memcache.ini



# configure timezone, mysql, apache
RUN cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    mkdir /var/www/html && \
    cp /var/www/localhost/htdocs/index.html /var/www/html/index.php && \
    echo "${TIMEZONE}" > /etc/timezone && \
    mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld /var/lib/mysql && \
    mkdir -p /run/apache2 && chown -R apache:apache /run/apache2 && chown -R apache:apache /var/www/localhost/htdocs/ && \
    sed -i 's#\#LoadModule rewrite_module modules\/mod_rewrite.so#LoadModule rewrite_module modules\/mod_rewrite.so#' /etc/apache2/httpd.conf && \
    sed -i 's#ServerName www.example.com:80#\nServerName localhost:80#' /etc/apache2/httpd.conf && \
    sed -i 's#/var/www/localhost/htdocs#/var/www/html#' /etc/apache2/httpd.conf && \
    sed -i 's/skip-networking/\#skip-networking/i' /etc/my.cnf.d/mariadb-server.cnf && \
    sed -i '/mariadb\]/a log_error = \/var\/lib\/mysql\/error.log' /etc/my.cnf.d/mariadb-server.cnf && \
    sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/my.cnf.d/mariadb-server.cnf && \
    sed -i '/mariadb\]/a skip-external-locking' /etc/my.cnf.d/mariadb-server.cnf && \
    sed -i '/mariadb\]/a general_log = ON' /etc/my.cnf.d/mariadb-server.cnf && \
    sed -i '/mariadb\]/a general_log_file = \/var\/lib\/mysql\/query.log' /etc/my.cnf.d/mariadb-server.cnf

RUN sed -i 's#display_errors = Off#display_errors = On#' /etc/php7/php.ini && \
    sed -i 's#upload_max_filesize = 2M#upload_max_filesize = 100M#' /etc/php7/php.ini && \
    sed -i 's#post_max_size = 8M#post_max_size = 100M#' /etc/php7/php.ini && \
    sed -i 's#session.cookie_httponly =#session.cookie_httponly = true#' /etc/php7/php.ini && \
    sed -i 's#error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT#error_reporting = E_ALL#' /etc/php7/php.ini


# Configure xdebug
RUN echo "zend_extension=xdebug.so" > /etc/php7/conf.d/xdebug.ini && \ 
    echo -e "\n[XDEBUG]"  >> /etc/php7/conf.d/xdebug.ini && \ 
    echo "xdebug.remote_enable=1" >> /etc/php7/conf.d/xdebug.ini && \  
    echo "xdebug.remote_connect_back=1" >> /etc/php7/conf.d/xdebug.ini && \ 
    echo "xdebug.idekey=PHPSTORM" >> /etc/php7/conf.d/xdebug.ini && \ 
    echo "xdebug.remote_log=\"/tmp/xdebug.log\"" >> /etc/php7/conf.d/xdebug.ini

COPY entry.sh /entry.sh

RUN chmod u+x /entry.sh

WORKDIR /var/www/html

EXPOSE 80
EXPOSE 3306

ENTRYPOINT ["/entry.sh"]
CMD ["mysqld", "--user=root", "--bind-address=0.0.0.0"]

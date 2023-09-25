# install and configure Nginx
package 'nginx' {
  ensure => '1.18.0',
  source => 'apt-get',
}

# set firewall to listening on port 80

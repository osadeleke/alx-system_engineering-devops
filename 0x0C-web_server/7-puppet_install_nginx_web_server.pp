# install and configure Nginx
package { 'nginx':
  ensure => '1.18.0',
}

exec { 'set_hello_world':
  command => 'echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html'
  require => Package['nginx'],
}

exec { 'set_redirect':
  command => "sudo sed -i '\\#root /var/www/html;#a\\\\tlocation /redirect_me/ {\\n\\t\\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\\n\\t}' /etc/nginx/sites-available/default",
  require => require => Package['nginx'],
}

exec { 'restart nginx':
  command => 'sudo service nginx restart',
  require => Exec['set_redirect'],
}

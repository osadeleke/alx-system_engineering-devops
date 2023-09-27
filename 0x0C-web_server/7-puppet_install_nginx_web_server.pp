# install and configure Nginx
package { 'nginx'
  ensure => '1.18.0',
  source => 'apt-get',
}

exec { 'set_hello_world'
  command => 'echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html'
}

exec { 'set_redirect'
  command => "sudo sed -i '\\#root /var/www/html;#a\\\\tlocation /redirect_me/ {\\n\\t\\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\\n\\t}' /etc/nginx/sites-available/default",
}

exec { 'restart nginx'
  command => 'sudo service nginx restart',
}

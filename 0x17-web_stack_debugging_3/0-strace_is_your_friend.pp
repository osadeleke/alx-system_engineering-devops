# replace wrong file path with right file path clearing 500 server error
file { '/var/www/html/wp-settings.php':
  ensure => file,
}

exec { 'find-class':
  command => "sudo sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/wwww/html/wp-settings.php",
  path    => '/bin:/usr/bin', # Specify the path to the 'sed' command
  require => File['/var/www/html/wp-settings.php'], # Ensure the file exists before running the exec
}

service { 'apache2':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/var/www/html/wp-settings.php'], # Restart when the Apache configuration file changes
}
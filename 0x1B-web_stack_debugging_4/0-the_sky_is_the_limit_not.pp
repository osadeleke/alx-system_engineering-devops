# update config to allow more open file
file { '/etc/default/nginx':
  ensure   => file,
  content  => "#This file is managed by puppet\n\nULIMIT=\"-n 4096\"\n",
  notify   => Exec['restart_nginx'],
}

# restart the nginx after changing config
exec { 'restart_nginx':
  command     => '/etc/init.d/nginx restart',
  refreshonly => true,
}
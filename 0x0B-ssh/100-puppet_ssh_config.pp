# set ssh config file to use private key and not authenticate password
exec { 'set_ssh_config':
  command => '/bin/echo "    PasswordAuthentication no" >> /etc/ssh/ssh_config',
}

exec { 'set_ssh_config2':
  command => '/bin/echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}

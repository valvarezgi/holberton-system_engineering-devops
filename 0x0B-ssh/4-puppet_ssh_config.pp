# Client configuration file (w/ Puppet)

file { '/etc/ssh/ssh_config':
  ensure => present,
}->
file_line { 'No password authentication':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication'
}->
file_line { 'Identity file'
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/holberton',
  match => '^IdentityFile'
}

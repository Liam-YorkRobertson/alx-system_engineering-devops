#Allow user holberton to open filesi without error

exec { 'increase_hard_limit':
  command => 'echo "holberton hard nofile 8192" >> /etc/security/limits.conf',
  path    => '/bin:/usr/bin',
}

exec { 'increase_soft_limit':
  command => 'echo "holberton soft nofile 4096" >> /etc/security/limits.conf',
  path    => '/bin:/usr/bin',
}

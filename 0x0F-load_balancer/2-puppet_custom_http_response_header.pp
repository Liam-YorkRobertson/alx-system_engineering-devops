#script that creates a custom HTTP header response

exec { 'update_nginx':
  command => '/usr/bin/apt-get update',
} ->

package { 'nginx':
  ensure => 'present',
} ->

file { '/etc/nginx/nginx.conf':
  ensure  => present,
  content => template('2-puppet_custom_http_response_header/nginx.conf.erb'),
  require => Package['nginx'],
} ->

exec { 'start_nginx':
  command     => '/usr/sbin/service nginx start',
  refreshonly => true,
  subscribe   => File['/etc/nginx/nginx.conf'],
}

#Increases the maximum limit of traffic for nginx

exec { 'nginx_config_fix':
  command => "/bin/sed -i 's/15/4096/' /etc/default/nginx && /etc/init.d/nginx restart",
  path    => '/usr/local/bin:/bin',
}

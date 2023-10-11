# Puppet script to solve server error with help from strace

exec { 'fix-wordpress':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/bin'],
  unless  => 'grep -q "phpp" /var/www/html/wp-settings.php',
}

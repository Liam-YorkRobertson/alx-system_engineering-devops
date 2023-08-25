# executing command to kill a process

exec { 'pkill':
  command  => 'pkill -f killmeow',
  provider => 'shell',
}

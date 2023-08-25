# executing command to kill a process

exec { 'pkill':
  command  => 'pkill killmeow',
  provider => 'shell',
}

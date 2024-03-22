exec { 'install flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => "/usr/bin/pip3 freeze | grep Flask==2.1.0",
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}

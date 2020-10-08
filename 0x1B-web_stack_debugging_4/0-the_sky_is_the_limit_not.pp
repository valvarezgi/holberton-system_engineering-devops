# Change open file limit for Nginx
exec { 'changelimit':
    command => 'sed -i -e "s/15/70000/g" /etc/default/nginx',
    path    => '/bin/',
}

#Restart service 
service { 'nginx':
    ensure    => running,
    subscribe => Exec['changelimit']}

# install 2.1.0 version of flask from pip
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

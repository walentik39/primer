#!/usr/local/bin/perl

use 5.30.0;
use warnings;
use IO::Socket::INET;

my $addr = 'webcode.me:80';
my $req = "HEAD / HTTP/1.0\r\n\r\n";

my $sock = IO::Socket::INET->new(
    Domain => AF_INET,
    PeerAddr => $addr,
) or die "failed to create socket: $!\n";

$sock->send($req, 0);

while (<$sock>) {
    print $_;
}

$sock->close();

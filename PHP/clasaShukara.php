<?php
class login{
    public $host='192.168.0.145';
    public $port='6636';

    public $socket;

    function makeConnection(){
        $this->socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP) or die("Could not create socket\n");
        socket_set_option($this->socket, SOL_SOCKET, SO_KEEPALIVE, 1);
        //socket_bind ($this->socket, $this->host, $this->port);
        return socket_connect($this->socket, $this->host, $this->port) or die ("Could not connect to server\n");
    }

    function sendData($q){
        socket_write($this->socket, $q, strlen($q)) or die("Could not send data to server\n");
    }

    function receiveData(){
        $result = socket_read ($this->socket, 1024000) or die("Could not read server response\n");
        return $result;
    }
    function closeSocket(){
        socket_close($this->socket);
    }
}
?>
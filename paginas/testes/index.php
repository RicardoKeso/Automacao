<?php

function StartPDO(){
	return new PDO('sqlite:../../db/automacao.db', '', '', array(
			PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
	));
}
	
function listar(){
	$dbh = StartPDO();
	$results = $dbh->query('SELECT * FROM gpioControl;');

	print "<b>id - nome - pino - status - output</b></br>";
	foreach($results as $row){
		print $row['id'] . " - " . $row['bcm'] . " - " . $row['board'] . " - " . $row['status'] . " - " . $row['output'] . "</br>";
	}
	$dbh = NULL;
}

function stausPino($pino){
	$dbh = StartPDO();
	$results = $dbh->query('SELECT status FROM gpioControl WHERE output=1 and board == ' . $pino . ";");

	foreach($results as $row){
		$status = $row['status'];
	}
	$dbh = NULL;
	return $status;
}

function atualizarStatus($pino){
	$dbh = StartPDO();
	$status = stausPino($pino);
	$status = (($status == 1) ? 0 : 1);
	$dbh->query("UPDATE gpioControl SET status = " . $status . " WHERE board == " . $pino . ";");
	$dbh = NULL;
}
listar();
?>

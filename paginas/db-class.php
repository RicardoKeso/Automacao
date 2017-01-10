<?php

Class Database {
	private function StartPDO(){
		return new PDO('sqlite:../db/automacao.db', '', '', array(
				PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
		));
	}
	
	private function listar(){
		$dbh = Database::StartPDO();
		$results = $dbh->query('SELECT * FROM gpioControl');
	
		print "<b>id - nome - pino - status - output</b></br>";
		foreach($results as $row){
			print $row['id'] . " - " . $row['bcm'] . " - "	. $row['board'] . " - " . $row['status'] . " - ". $row['output'] . "</br>";
		}
		$dbh = NULL;
	}
	
	public function stausNomePino($pino){
		$dbh = Database::StartPDO();
		$results = $dbh->query('SELECT status, nome FROM gpioControl WHERE output=1 and board == ' . $pino . ";");
	
		foreach($results as $row){
			$retorno[0] = $row['status'];
			$retorno[1] = $row['nome'];
		}
		$dbh = NULL;
		return $retorno;
	}
	
	public function atualizarStatus($pino){
		$inicio = round(microtime(true) * 1000);
		
		$retorno = Database::stausNomePino($pino);
		$dbh = Database::StartPDO();
		$status = (($retorno[0] == 1) ? 0 : 1);
		$dbh->query("UPDATE gpioControl SET alterar=1, status=" . $status . " WHERE board==" . $pino . ";");
		
		$fim = round(microtime(true) * 1000);		
		echo ($fim - $inicio);
		
		$dbh = NULL;
	}
}

?>

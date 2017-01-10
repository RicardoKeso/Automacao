<?php

include("db-class.php");

$db = new Database();
$pino = $_GET["id"];
$pBack = $_GET["pBack"];

if ($pBack == 0){
	$db->atualizarStatus($pino);
}

$retorno = $db->stausNomePino($pino);

if ($retorno[0] == 1){
	echo "<button class=\"botaoGreen\" onclick=\"Botao(this.id, 0)\" id=\"$pino\">$retorno[0]</button>";
} else {
	echo "<button class=\"botaoRed\" onclick=\"Botao(this.id, 0)\" id=\"$pino\">$retorno[0]</button>";
}

?>

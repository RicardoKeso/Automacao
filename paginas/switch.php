<?php

	$id = $_GET["id"];
	$nome = substr($id, -1);
	$flag = 1;
	
	echo $id;
	
	

	/*if ($flag == 0)
		echo "<button class=\"botaoGreen\" onclick=\"Switch(this.id)\" id=\"$id\">$nome . \"sw\" </button>";
	else 
		echo "<button class=\"botaoRed\" onclick=\"Switch(this.id)\" id=\"$id\">$nome</button>";*/

	//shell_exec('touch ../gpio/mudarEstado/7');
	//$valor = shell_exec('cat ../gpio/pinos/7');
	
	
?>

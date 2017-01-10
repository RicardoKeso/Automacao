/*function Switch(id){
	//alert(id)
	$.ajax({
		url: "paginas/switch.php?id=" + id,
		success: function(result){
			$("#"+id).html(result);
		}
	});
};*/

function Botao(id, pBack){
	//alert(id)
	//alert(pBack)
	$.ajax({
		url: "paginas/botao.php?id=" + id + "&pBack=" + pBack,
		success: function(result){
			$("#"+id).html(result);
		}
	});
};

$(document).ready(function() {
	Botao("7", "1");
	Botao("12", "1");
});

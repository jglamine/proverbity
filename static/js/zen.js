$(document).ready(function() {

	$("#quote-button").click(function(){
		$("#quote-button").button("loading");
		$.ajax({
			url: "ajax/random_quote.json",
			dataType: "json",
			success: function(data, textStatus, jqXHR){
				$("#quote-text").html(data.text);
				$("#quote-author").html("—" + data.author);
				// update url
				window.history.pushState(data, "", "/" + data.id);

			},
			complete: function(jqXHR, textStatus){
				$("#quote-button").button("reset");
			}
		});
	});

	window.onpopstate = function(e){
		if (e.state){
			$("#quote-text").html(e.state.text);
			$("#quote-author").html("—" + e.state.author);
		}
	};
});
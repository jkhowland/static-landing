/*modal for sign up*/
$(function() {
	$(".modal-signup").click(function() {
		$("#modal-signup").show();
		$("div.wrapper").show();
		return false;
	});
	$(".modal-close").click(function() {
		$("#modal-signup").hide();
		$("div.wrapper").hide();
	});	
});

/*process images to be responsive*/
$(function () {
	$("img").addClass("img-responsive");
});




/*process images to be responsive*/
$(function () {
	$("img").addClass("img-responsive");
});

/*process retina display*/
$(function() {
	if (window.devicePixelRatio > 1) {
		var lowers = $(".logo").attr('src');	
		var highres = lowers.replace(".", "@2x.");
		$(".logo").attr('src', highres);
	}
});

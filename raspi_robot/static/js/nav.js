
$(document).ready(function() {
	$('li.nav > a').each(function() {
	    if ($(this).prop('href') == window.location.href) {
	      $(this).parent().addClass('current');
	    }
	    else {
	    	$(this).parent().removeClass('current');
	    }
	});
});

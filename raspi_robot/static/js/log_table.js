
function evenRows() {
	$('#log_table_body tr').removeClass('even').filter(':even').addClass('even');
} 

$(document).ready(evenRows);

var MutationObserver = window.MutationObserver || window.WebKitMutationObserver;
var obs = new MutationObserver(evenRows);
obs.observe($('#log_table_body').get(0),{ childList: true, subtree: true });
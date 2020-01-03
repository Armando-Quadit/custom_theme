$(document).ready(function() { 
	'use strict';
	//var website = require('web_editor.snippets.animation');
	var website = openerp.website;
	alert("website", website.openerp_website)
	website.snippet.options.snippet_testimonial_options = website.snippet.Option.extend({
		on_focus: function() {
			alert("On focus!");
		},
	});
});

// alert("Hola mundo");
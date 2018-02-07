		var test = "wow";
		
		jQuery(document).ready(function() {

			
			

			/*jQuery(".dict").click(function(){
				alert("safasf");
			});*/

			jQuery('.notes-area').mouseup(function() {
				var text = getSelectedText();
				//alert(text);
				console.log(text);
				jQuery("#defini").text("loading definitions for "+text);
				 jQuery.ajax({
                                                type: "POST",
                                                data: {textfield : text},
                                                success: function(data) {
                                                jQuery("#defini").text(data);
                                                },
                                                });
				 
				});

			jQuery(".textarbut").click(function(){
				var artext = jQuery("#textar").val();
				console.log(artext)
				alert(artext);
				jQuery.ajax({					
												url: '/textarea',
                                                type: "POST",
                                                data: {textarea : artext},
                                                success: function(data) {
                                                jQuery(".notes-area").text(data);
                                                },
                                                });
			});

			jQuery(".otherbut").click(function(){
				var text = jQuery("#url2").val();
				jQuery.ajax({					
												url: '/textarea',
                                                type: "POST",
                                                data: {textarea : text},
                                                success: function(data) {
                                                jQuery(".notes-area").text(data);
                                                },
                                                });
			});

			jQuery(".txtbut").click(function(){
				jQuery(".nonwiki").css("display","none");
				jQuery(".wiki").css("display", "none");
				jQuery(".simtext").css("display", "inline");

			});

			jQuery(".wikibut").click(function(){
				jQuery(".nonwiki").css("display","none");
				jQuery(".wiki").css("display", "inline");
				jQuery(".simtext").css("display", "none");

			});

			jQuery(".nonwikibut").click(function(){
				jQuery(".nonwiki").css("display","inline");
				jQuery(".wiki").css("display", "none");
				jQuery(".simtext").css("display", "none");

			});


			function getSelectedText() {
				if (window.getSelection) {
					return window.getSelection().toString();
				} else if (document.selection) {
					return document.selection.createRange().text;
				}
				return '';
			}

			jQuery(".button").click(function() {
				var input_string = jquery("#textfield").val();
				jQuery.get('?', input_string);
				return false;
			});
		});

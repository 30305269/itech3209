$( function() 
	{
		$("#addGroup").click(function()
		{
			var addGroup = document.createElement('input');
			$(addGroup).attr("type","text");
			$(addGroup).attr("required","");
			$(addGroup).attr("name","newGroup");
			$(addGroup).attr("class","form-control");
			$(addGroup).attr("placeholder","New Group Title");
			$("#cardGroups").append(addGroup);
		})	
	});
	
$( function() 
	{
		$("#addCard").click(function()
		{
			var addCard = document.createElement('input');
			$(addCard).attr("type","text");
			$(addCard).attr("name","newCard");
			$(addCard).attr("required","");
			$(addCard).attr("class","form-control");
			$(addCard).attr("placeholder","New Card Text");
			$(addCard).required = true;
			$("#cardsList").append(addCard);
		})	
	});	
	
$( function() 
	{
		$(".deleteGroups").change(function () 
		{
			var $this = $(this);
			if ($this.is(':checked'))
			{
				var deleteGroup = document.createElement('input');
				$(deleteGroup).attr("id", $(this).val());
				$(deleteGroup).attr("name", "deleteGroup");
				$(deleteGroup).attr("type", "hidden");
				$(deleteGroup).attr("value", $(this).val());
				$("#cardGroups").append(deleteGroup);
			}
			else 
			{
				$("#cardGroups").find("#" + $(this).val()).remove();
			}	
        });
	});		
	
$( function() 
	{
		$(".deleteCards").change(function () 
		{
			var $this = $(this);
			if ($this.is(':checked'))
			{
				var deleteCard = document.createElement('input');
				$(deleteCard).attr("id", $(this).val());
				$(deleteCard).attr("name", "deleteCard");
				$(deleteCard).attr("type", "hidden");
				$(deleteCard).attr("value", $(this).val());
				$("#cardsList").append(deleteCard);
			}
			else 
			{
				$("#cardsList").find("#" + $(this).val()).remove();
			}	
        });
	});		
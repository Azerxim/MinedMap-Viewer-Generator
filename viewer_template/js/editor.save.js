var JSONLayers = [];

function CancelButton() {
	swal({
		title: "Cancel",
		text: "Are you sure you want to cancel",
		type: "warning",
		showCancelButton: false,
		confirmButtonColor: "#d32300",
		confirmButtonText: "Yes",
		closeOnConfirm: true
	},
	function(){
		location.reload();
	});
}

function generateGeoJson(){
	console.log(JSONLayers);
	
	// Inset actions here

	swal({
		title: "Oops...",
		text: "The operation was not successful",
		type: "error",
		showCancelButton: true,
		confirmButtonColor: "#d32300",
		confirmButtonText: "Ok",
		closeOnConfirm: true
	});
}